from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-created')[:10]
    form = PostForm()
    user = request.user
    context = {'latest_post_list': latest_post_list, 'form' : form, 'user': user}

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()
    
    return render(request, 'index.html', context)
    

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()
    return render(request, 'edit.html', {'form': form})
