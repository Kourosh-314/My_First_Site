from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
#def for increasing the number of views.  
def increase_views(post):      
    post.counted_views +=1
    post.save(update_fields=['counted_views'])

def blog_home(request):
    now = timezone.now()
    posts = Post.objects.filter(published_time__lte = now , status = 1)
    context = {'posts':posts}
    return render(request,'Blog/blog-home.html',context)

def blog_single(request,pid):
    post = get_object_or_404(Post,pk = pid,status = 1)
    increase_views(post)
    context = {'post':post}
    return render(request,'Blog/blog-single.html',context)

def test(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'test.html',context)
