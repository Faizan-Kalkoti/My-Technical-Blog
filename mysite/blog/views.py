from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import PostForm, CommentsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comments
from django.utils import timezone
from django.urls import reverse_lazy
import pytz
from datetime import timedelta

from django.views.generic import (TemplateView, DetailView, DeleteView,
                                   ListView, CreateView, UpdateView)

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostList(ListView):
    model = Post 

    def get_queryset(self):
        tz1 = pytz.timezone('Asia/Kolkata')
        current_time = timezone.now().astimezone(tz1)
        duration = timedelta(hours=5, minutes=30)
        current_date = current_time + duration
        return Post.objects.filter(published_date__lte =current_date).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin ,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    login_url = '/login/'
    form_class = PostForm

class DeletePostView(LoginRequiredMixin, DeleteView):
    model= Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url= '/login/'
    redirect_field_name = 'blog' 
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull= True).order_by('created_date')
    


@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.publish()
    return redirect('post_detail',pk = post.pk )
    

    
# Views for Comments 
#############################

# @login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method  == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk = post.pk)
        else: 
            print("error in validating form")
    else:
        form = CommentsForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comments_Approved(request, pk):
    comment = get_object_or_404(Comments, pk = pk)
    comment.approve()
    return redirect('post_detail', pk = comment.post.pk)

@login_required
def comments_Removed(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk = post_pk)




