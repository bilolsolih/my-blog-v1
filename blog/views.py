from django.shortcuts import render
from .models import Post
from django.http import Http404

# git@github.com:bilolsolih/my-blog-v1.git
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found!")
    return render(request, 'blog/post/detail.html', {'post': post})
# >>> Post.objects.order_by('?')
