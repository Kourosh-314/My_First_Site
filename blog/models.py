from django.db import models

# Create your models here.
class Post(models.Model):
    #author
    #image
    title = models.CharField(max_length=250)
    content = models.TextField()
    #category
    #tag
    counted_views = models.BooleanField(default=0)
    status = models.BooleanField(default=False)
    published_time = models.DateTimeField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return "{}-{}".format(self.title,self.id)