from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def blog_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/blog_page.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('../')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
