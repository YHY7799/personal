from django.shortcuts import render, redirect
from .models import post, about
from .forms import postForm, aboutForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    about_list = about.objects.all
    posts_list = post.objects.all

    return render(request, 'per/home.html', {'about_list': about_list, 'posts_list': posts_list})


def blogs(request):
    posts_list = post.objects.all
    return render(request, 'per/posts.html', {'posts_list': posts_list}) 


def add_post(request):
    submitted = False
    if request.method == 'POST':
        if request.user.is_superuser:
            form = postForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_post?submitted=True')
    else:
        form = postForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'per/add_post.html', {'submitted': submitted, 'form': form})


def update_post(request, post_id):
    Post = post.objects.get(pk=post_id)
    if request.user.is_superuser:
        form = postForm(request.POST or None, instance=Post)
    if form.is_valid():
                form.save()
                return redirect('blogs')
    return render(request, 'per/update_post.html', {'Post':Post, 'form': form})



def edit_about(request):
    About = about.objects.get()
    if request.user.is_superuser:
        form = aboutForm(request.POST or None, instance=About)
    if form.is_valid():
                form.save()
                return redirect('home')
    return render(request, 'per/edit.html', {'About':About, 'form': form})


def delete_post(request, post_id):
    Post = post.objects.get(pk=post_id)
    Post.delete()
    messages.success(request, ("تم الحذف"))
    return redirect('blogs')


def show_post(request, post_id):
    Post = post.objects.get(pk=post_id)
    return render(request, 'per/show_post.html', {'Post': Post})

