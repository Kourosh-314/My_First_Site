from django.shortcuts import render,get_list_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
#def for increasing the number of views  
def increase_views(posts):      
    posts.counted_views +=1
    posts.save(update_fields=['counted_views'])

def blog_home(request):
    now = timezone.now()
    posts = Post.objects.filter(published_time__lte = now , status = 1)
    context = {'posts':posts}
    return render(request,'Blog/blog-home.html',context)

def blog_single(request,pid):
    posts = Post.objects.get(pk=pid)
    increase_views(posts)
    context = {'posts':posts}
    return render(request,'Blog/blog-single.html',context)

def test(request,pid):
    posts = get_list_or_404(Post,pk=pid)
    context = {'posts':posts}
    return render(request,'test.html',context)