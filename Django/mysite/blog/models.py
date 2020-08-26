from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# keep in mind that model.Manager == objects
class PublishedManager(models.Manager):
    """Custom model manager for Post class """
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    
    objects = models.Manager() #The Default Manager
    published = PublishedManager() # Our Custom Manager

    title = models.CharField(max_length=250)    
    slug = models.SlugField(max_length=250,        
                unique_for_date='publish')
                
    author = models.ForeignKey(User,
                on_delete=models.CASCADE,
                related_name='blog_posts')
    body = models.TextField()
        
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    status = models.CharField(max_length=10,
                choices=STATUS_CHOICES,
                default='draft')
                
    class Meta:
        """spacify decending order by adding "-" prefix to publish
        to query recent posts first"""
        ordering = ('-publish',)
        
        """This guy is human readable representation of the object """
    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('blog:post_detail',
            args=[self.publish.year,
            self.publish.month,
            self.publish.day, self.slug])