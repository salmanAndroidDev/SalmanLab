from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES= (('draft','Draft'),('publish', 'Publish'))

    title = models.CharField(max_length= 250)
    slug = models.SlugField(max_length= 250, unique_for_date='publish')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length= 10, choices= STATUS_CHOICES, default= 'draft')

    class Meta:
        ordering= ('-publish',)
    def __str__(self):
        return self.title










