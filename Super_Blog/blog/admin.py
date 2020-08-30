from django.contrib import admin
from .models import Post

# Easy way to registering the app. uncomment next line.
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ customizing the way models are displayed in admin site"""

    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)} # prepopulates slug when title get filled
    raw_id_fields = ('author',) # we can choose author by id
    date_hierarchy = 'publish' # will be displayed in date hierarchy
    ordering = ('status', 'publish') 