from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
# Create your views here.


def create(request):
    if request.method == 'POST':
        new_blog = Blog()
        new_blog.title = request.POST['title']
        new_blog.content = request.POST['content']

        new_blog.save()

        return redirect('home')
    return render(request, 'new.html')


def home(request):
    blog_data = Blog.objects.all()
    blogs = {'blog_data':blog_data}
    return render(request, 'home.html', blogs)