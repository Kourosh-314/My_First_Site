from django.contrib import admin
from blog.models import Post , Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    empty_value_display = 'empty'
    list_display = ('title','author','counted_views','status','published_time','created_time')
    list_filter = ('status','author')
    search_fields = ['title','content']
    summernote_fields = ('content',)

admin.site.register(Category)