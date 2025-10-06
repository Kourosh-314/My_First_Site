from django.shortcuts import render,get_list_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
#def for increasing the number of views        
def blog_home(request):
    posts = get_list_or_404(Post)
    #posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'Blog/blog-home.html',context)

def blog_single(request,pid):
    posts = get_list_or_404(Post,pk=pid)
    posts = Post.objects.get(pk=pid)
    context = {'posts':posts}
    return render(request,'Blog/blog-single.html',context)

def test(request,pid):
    posts = get_list_or_404(Post,pk=pid)
    context = {'posts':posts}
    return render(request,'test.html',context)
