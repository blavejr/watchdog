from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import PostForm
from .models import Post


@login_required
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
    

@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post})



def logout_view(request):
    logout(request)
    return render(request, 'logout.html', {})
