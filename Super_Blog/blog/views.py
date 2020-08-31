from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post, Comment
from .forms import ShareByEmailForm, CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
# class PostListView(ListView):
#     """ class-based view """
#     queryset = Post.published.all()
#     context_object_name = 'posts'  # variable name of posts to use in template
#     paginate_by = 3
#     template_name = 'blog/post/list.html'

""" function-based view. uncomment it if you like and comment class-based view"""


def post_list(request, tag_slug=None):
    """ rendering post list """
    object_list = Post.published.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        # give me list of posts which their tags are like the one being clicked!
        # inside prenthes equal=== tag in tags
        object_list = object_list.filter(tags__in=[tag])
    # instaciate paginator with object_list and get 3 posts per each query
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    template = 'blog/post/list.html'
    return render(request, template, {'posts': posts, 'tag': tag})


def post_detail(request, day, month, year, post):
    """ rendering post detail """
    # returns 404 response if there is no post with these info
    # we can get year,month, day from publish field by useing '__'
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    template = 'blog/post/detail.html'

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()

    post_tags_id = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(
        tags__in=post_tags_id).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tag=Count(
        'tags')).order_by('-same_tag', '-publish')[:4]
    return render(request, template, {'post': post,
                                      'comments': comments,
                                      'new_comment': new_comment,
                                      'form': form,
                                      'similar_posts': similar_posts})


def post_share_by_email(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')

    sent = False

    if request.method == 'POST':
        form = ShareByEmailForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            to = cd['to']
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )

            subject = f'{cd["name"]} recommends you to read {post.title}'
            message = f'{cd["name"]} recommends you this post, and comments: {cd["comments"]}\n\n'\
                      f'check url: {post_url}'

            send_mail(subject, message, 'salman@deepclass.ir', [to])
            sent = True
    else:
        form = ShareByEmailForm()
    return render(request, 'blog/post/share_by_email.html', {'post': post,
                                                             'form': form,
                                                             'sent': sent})
