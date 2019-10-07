from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
class commentManager(models.Manager):
    def filter_by_instance(self, instance):
            content_type = ContentType.objects.get_for_model(instance.__class__)
            object_id = instance.id
            comments = Comment.objects.filter(content_type=content_type, object_id=object_id) 
            qs =super(commentManager,self).filter(content_type=content_type, object_id=object_id)
            return qs
class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField(blank=False)
    comment_date = models.DateTimeField(default = datetime.now, blank=True)
    #from django doc: Generic Relations
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    objects = commentManager()
    
    def __str__(self):
        return self.author
   