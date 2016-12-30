from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from models import Blog
from forms import BlogForm

class BlogView(View):
	# Blog view
    form_class = BlogForm
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'username':kwargs['username']})

    def post(self, request, *args, **kwargs):
    	pass