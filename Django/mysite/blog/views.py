from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
# Create your views here.
from django.core.mail import send_mail


class PostListView(ListView):
    queryset = Post.published.all()
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


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
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n"\
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'sbmlai25@gmail.com',
                      [cd['to']])
            sent = True
        else:  # form is not valid
            print('****************************************************************test*****************', form.errors)

    else:
        # request was get
        form = EmailPostForm()  # make it empty to be filled in empty get form
    return render(request, 'blog/post/share.html',
                  {'post': post, 'form': form, 'sent': sent})
