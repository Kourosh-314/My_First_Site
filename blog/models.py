from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from taggit.managers import TaggableManager
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
    tag = TaggableManager()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    published_time = models.DateTimeField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return "{}-{}".format(self.id,self.title)
    # There is also a template tag for following function which i wrote in blog-home.html 
    def truncatewords(self):
        context = truncatewords(self.content, 5)
        return context
    
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField(upload_to = 'comment/',default = 'comment/default.jpg')
    approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_time'] 

    def __str__(self):
        return self.name
