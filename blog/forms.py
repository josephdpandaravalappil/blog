from django import forms
from django.forms import ModelForm
from models import Blog


class BlogForm(ModelForm):
	# Blog Form
	post = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your post here'}))

	class Meta:
		model = Blog
		fields = ['post']