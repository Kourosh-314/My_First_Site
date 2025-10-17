from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
now = timezone.now()
# Create your views here.
#def for increasing the number of views.  
def increase_views(post):      
    post.counted_views +=1
    post.save(update_fields=['counted_views'])

def blog_home(request):
    posts = Post.objects.filter(published_time__lte = now , status = 1)
    context = {'posts':posts}
    return render(request,'Blog/blog-home.html',context)

def blog_single(request,pid):
    post = get_object_or_404(Post,pk = pid,status = 1)
    posts = list(Post.objects.filter(published_time__lte=now, status=1))
    next_post = None
    previous_post = None
    try:
        current_post = next(post for post in posts if post.id == pid)
        current_index = posts.index(current_post)
        
        if current_index < len(posts) - 1:
            next_post = posts[current_index + 1]
    
        if current_index > 0:
            previous_post = posts[current_index - 1]

    except StopIteration:
        
        pass
    increase_views(post)
    context = {'post':post,'posts':posts,'next_post':next_post,'previous_post':previous_post}
    return render(request,'Blog/blog-single.html',context)

def test(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'test.html',context)
