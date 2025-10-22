from django.contrib import admin
from myapp.models import Contact, NewsLetter
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    empty_value_display = 'empty'
    list_display = ('name','email','created_time')
    list_filter = ('subject',)
    search_fields = ['subject']
admin.site.register(NewsLetter)