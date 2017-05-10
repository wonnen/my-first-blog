from django.shortcuts import render
from django.utils import timezone
from .models import Post


def blog_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/blog_page.html', {'posts': posts})
