from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to = 'blog/',default = 'blog/default.jpg')
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    #tag
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_time = models.DateTimeField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return "{}-{}".format(self.id,self.title)