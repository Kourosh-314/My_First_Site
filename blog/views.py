from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

# Create your views here.
#def for increasing the number of views
def increase_views(posts):
    for post in posts:
        post.counted_views +=1
        post.save(update_fields=['counted_views'])
        
def blog_home(request):
    now = timezone.now().date()
    posts = Post.objects.filter(published_time__lte=now)
    increase_views(posts)
    #posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'Blog/blog-home.html',context)

def blog_single(request):
    return render(request,'Blog/blog-single.html')

def test(request):
    posts = Post.objects.all()
    # A way to filter items
    #posts = Post.objects.filter()
    context = {'posts':posts}
    return render(request,'test.html',context)

    