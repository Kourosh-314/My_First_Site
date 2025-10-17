from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name = 'totalposts')
def function():
    posts = Post.objects.filter(status = 1).count()
    return posts

@register.filter
def snippet(value,arg = 10):
    return value[:arg]

@register.inclusion_tag('Blog/blog-latest-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_time')[:arg]
    return {'posts':posts}