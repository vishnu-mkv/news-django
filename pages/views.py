from django.shortcuts import render, get_object_or_404
from news.models import News
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.


def home_view(request):
	return render(request, "home.html")


class PostList(ListView):
	model = News
	template_name = 'list.html'
	context_object_name = 'object'
	paginate_by = 3
	ordering = ['-datetime']


class UserPostList(ListView):
	model = News
	template_name = 'userpostlist.html'
	context_object_name = 'object'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return News.objects.filter(author=user, ).order_by('-datetime')


class PostDetail(DetailView):
	model = News
	template_name = 'detail.html'


class PostCreate(LoginRequiredMixin, CreateView):
	model = News
	fields = ['headlines', 'content']
	template_name = 'create.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = News
	fields = ['headlines', 'content']
	template_name = 'create.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if post.author == self.request.user:
			return True
		else:
			return False


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = News
	template_name = 'delete.html'
	success_url = '../../../news'

	def test_func(self):
		post = self.get_object()
		if post.author == self.request.user:
			return True
		else:
			return False



