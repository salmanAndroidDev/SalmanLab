from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    """ Customized model manager to get only published posts """

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICE = (
                    ('draft', 'Draft'),
                    ('published', 'Published')
    )

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Our customed manager

    title = models.CharField(max_length=250)

    # simple slug field for SEO-Friendly url, we gonna add it to url
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    # Relationship is many-to-one
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,  # after deleting user, it's posts also would be deleted
                               related_name='blog_post')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)  # acts like const
    # get updated everytime we type Post.save()
    update = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='draft')

    class Meta:
        ordering = ('-publish',)  # ordering by ascending

    def __str__(self):  # user-friendly representation of post
        return self.title

    def get_absolute_url(self):
        """ conanical url pass to domain/post/post_detail/args** """
        return reverse('blog:post_detail',  # path
                       args=[self.publish.day,  # args
                             self.publish.month,
                             self.publish.year,
                             self.slug])
