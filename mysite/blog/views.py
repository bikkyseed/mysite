from django.shortcuts import HttpResponse, render
from matplotlib.style import context
from requests import post
from .models import Post


def blogHome(request):
    allPosts = Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    print(post)
    context = {'post':post }
    return render(request, 'blog/blogPost.html', context)

# Create your views here.
