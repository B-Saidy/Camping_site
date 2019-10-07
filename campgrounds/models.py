from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment


# class Author(models.Model):
#     user = models.ForeignKey(User, on_delete = models.DO_NOTHING, blank=True,null=True)
#     name = models.CharField(max_length=100)
#     text = models.TextField(max_length=400)
    
#     def __str__(self):
#         return self.name

class Campground(models.Model):
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    def __str__(self):
        return self.name
    
    @property
    def comments(self):
        camp=self
        qs = Comment.objects.filter_by_instance(camp)
        return qs
    @property
    def get_content_type(self):
        camp=self
        content_type = ContentType.objects.get_for_model(camp.__class__)
        return content_type