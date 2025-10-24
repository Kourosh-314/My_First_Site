from django.contrib import admin
from blog.models import Post , Category , Comment
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

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    empty_value_display = 'empty'
    list_display = ('name','post','approved','created_time')
    list_filter = ('approved','post')
    search_fields = ['name','post']