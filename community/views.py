from django.shortcuts import render
from community.forms import PostForm, CommentForm
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from community.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
	model=Post

	def get_queryset(self):
		return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
class PostDetailView(DetailView):
	model=Post

class CreatePostView(LoginRequiredMixin,CreateView):
	login_url='/sign_in/'
	redirect_field_name='community/post_detail.html'
	model=Post
class PostUpdateView(LoginRequiredMixin,UpdateView):
	login_url='/sign_in/'
	redirect_field_name='community/post_detail.html'
	model=Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
	model=Post
	success_url=reverse_lazy('post_list')
class DraftListView(LoginRequiredMixin,ListView):
	login_url='/sign_in/'
	redirect_field_name='community/post_list.html'
	model=Post

	def get_queryset(self):
		return Post.objects.filter(published_date__isnull=True).order_by('created_date')