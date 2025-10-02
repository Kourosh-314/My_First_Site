from django.contrib import admin
from blog.models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    empty_value_display = 'empty'
    list_display = ('title' ,'counted_views','status','published_time','created_time')
    list_filter = ('status',)
    search_fields = ['title','content']
    