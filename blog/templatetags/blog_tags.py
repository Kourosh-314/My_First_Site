from django import template
from blog.models import Post
from blog.models import Category
from django.utils import timezone

now = timezone.now()
register = template.Library()

@register.simple_tag(name = 'totalposts')
def function():
    posts = Post.objects.filter(status = 1).count()
    return posts

@register.filter
def snippet(value,arg = 10):
    return value[:arg]

@register.inclusion_tag('Blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_time')[:arg]
    return {'posts':posts}

@register.inclusion_tag('Blog/blog-single-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status = 1,published_time__lte = now)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category__name = name).count()
    return {'categories':cat_dict}

@register.inclusion_tag("website/latest_post.html")
def latest_posts(arg=6):
    posts = Post.objects.filter(status = 1,published_time__lte = now).order_by('published_time')[:arg]
    return {"posts":posts}