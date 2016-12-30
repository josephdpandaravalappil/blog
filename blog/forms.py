from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from models import Blog


class BlogForm(ModelForm):
	# Blog Form
	post = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Blog
		fields = ['post']