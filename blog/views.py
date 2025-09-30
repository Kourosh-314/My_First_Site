from django.shortcuts import render
from blog.models import Post
# Create your views here.
def blog_home(request):
    return render(request,'Blog/blog-home.html')

def blog_single(request):
    return render(request,'Blog/blog-single.html')

def test(request):
    posts = Post.objects.all()
    # A way to filter items
    #posts = Post.objects.filter()
    context = {'posts':posts}
    return render(request,'test.html',context)
    