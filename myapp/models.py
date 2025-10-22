from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_time']
    
    def __str__(self):
        return self.name
    
class NewsLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email