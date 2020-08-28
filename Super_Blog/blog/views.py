from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post


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
