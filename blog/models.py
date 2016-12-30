from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
	# Blog Model
    post = models.CharField(max_length=100)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)