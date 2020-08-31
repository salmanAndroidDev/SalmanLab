from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post
from .forms import ShareByEmailForm
from django.core.mail import send_mail


class PostListView(ListView):
    """ class-based view """
    queryset = Post.published.all()
    context_object_name = 'posts'  # variable name of posts to use in template
    paginate_by = 3
    template_name = 'blog/post/list.html'


""" function-based view. uncomment it if you like and comment class-based view"""
# def post_list(request):
#     """ rendering post list """
#     object_list = Post.published.all()
#     # instaciate paginator with object_list and get 3 posts per each query
#     paginator = Paginator(object_list, 3)
#     page = request.GET.get('page')

#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)

#     template = 'blog/post/list.html'
#     return render(request, template, {'posts': posts})


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
    return render(request, template, {'post': post})


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
