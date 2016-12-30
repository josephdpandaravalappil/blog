from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

from models import Blog
from forms import BlogForm

class BlogView(View):
	# Blog view
	form_class = BlogForm
	template_name = 'home.html'
	msg = {}

	def get(self, request, *args, **kwargs):
		form = self.form_class
		posts = Blog.objects.filter(created_by__username=kwargs['username'].lower()).order_by('-created_on')
		return render(request, self.template_name, {
			'form': form, 
			'username':kwargs['username'], 
			'msg': self.msg,
			'posts': posts
		})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			blog = form.save(commit=False)
			try:
				blog.created_by = User.objects.get(username=kwargs['username'].lower())
				blog.save()
				self.msg = {'message': 'Post created successfully.'}
			except User.DoesNotExist:
				self.msg = {'message': 'Oops! Wrong username provided'}
		posts = Blog.objects.filter(created_by__username=kwargs['username']).order_by('-created_on')
		return render(request, self.template_name, {
			'form': form, 
			'username':kwargs['username'], 
			'msg': self.msg,
			'posts': posts
		})