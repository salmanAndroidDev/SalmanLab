from django.contrib import admin
from .models import Post, Comment

# Easy way to registering the app. uncomment next line.
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ customizing the way models are displayed in admin site"""

    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # prepopulates slug when title get filled
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)  # we can choose author by id
    date_hierarchy = 'publish'  # will be displayed in date hierarchy
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'update')
    search_fields = ('name', 'email', 'body')
