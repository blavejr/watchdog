from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-created')[:10]
    form = PostForm()
    context = {'latest_post_list': latest_post_list, 'form' : form}
    return render(request, 'index.html', context)
    


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post})
