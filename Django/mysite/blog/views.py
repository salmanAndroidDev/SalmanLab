from django.db.models import Count
from taggit.models import Tag
from django.core.mail import send_mail
from .forms import EmailPostForm, CommentForm, SearchForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector, SearchQuery, \
    SearchRank, TrigramSimilarity

# Create your views here.


class PostListView(ListView):
    queryset = Post.published.all()
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request, tag_slug=None):
    object_list = Post.published.all()

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts,
                                                   'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            """
                the save() method in the following line creates an instance of  the model
                that the form is liked to and saves it to the database.
                If you call it using commit= False, you create the model
                instance but don't saveit to the databse yet.
                This comes in handy when you want to modify the object before finally saving.

            """
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # We gotta remember to save Comment to the database not CommentForm()
            # If we call CommentForm.save() first we instace Comment obj and initialized it with
            # CommentForm values than save it to the database
            new_comment.save()
    else:
        # send an empy form for the user to fill it
        comment_form = CommentForm()
    # List similar posts
    post_tags_ids = Post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
        .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
        .order_by('-same_tags', '-publish')[:4]
    return render(request, 'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_posts': similar_posts
                   })


def post_share(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             # you are querying raw Post make sure to filter status
                             status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted and make a EmailPostForm instace with a filled Form
        form = EmailPostForm(request.POST)  # scans the form

        if form.is_valid():
            # Form is valid, cleaned_data gives only validated data, so here we'll get all fields with their values
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())  # by using reverse() method inside model we can get absolute path to create complete url
            subject = "{cd['name']} recommends you read {post.title}"
            message = "Read {post.title} at {post_url}\n\n"\
                "{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'sbmlai25@gmail.com',
                      [cd['to']])
            sent = True
        else:  # form is not valid
            print('*************************test*****************', form.errors)

    else:
        # request was get
        form = EmailPostForm()  # make it empty to be filled in empty get form
    return render(request, 'blog/post/share.html',
                  {'post': post, 'form': form, 'sent': sent})


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:  # if there is there query parameter inside request.GET dictionary
        # NOTE: request.GET and request.POST are dictionaries
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']  # cleaned_data gives dictionary

            search_vector = SearchVector('title', weight='A') + \
                SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            results = Post.published.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gt=0.1).order_by('-similarity')
    return render(request, 'blog/post/search.html',
                  {'form': form,
                   'query': query,
                   'results': results
                   })
