from django.shortcuts import render , get_list_or_404 , get_object_or_404
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from blog.models import Post
from django.utils import timezone
from django.http import Http404

now = timezone.now()

# Create your views here.

#def for increasing the number of views.  
def increase_views(post):      
    post.counted_views +=1
    post.save(update_fields=['counted_views'])

def blog_home(request,**kwargs):
    posts = Post.objects.filter(published_time__lte = now , status = 1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tag__name__in = [kwargs['tag_name']])
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request,'Blog/blog-home.html',context)

def blog_single(request,pid):
    posts = get_list_or_404(Post,published_time__lte=now, status=1)
    post = None
    next_post = None
    previous_post = None
    try:
        post = next(post for post in posts if post.id == pid)
        current_index = posts.index(post)
        
        if current_index < len(posts) - 1:
            next_post = posts[current_index + 1]
    
        if current_index > 0:
            previous_post = posts[current_index - 1]

    except StopIteration:
        raise Http404()
    increase_views(post)
    context = {'post':post,'next_post':next_post,'previous_post':previous_post}
    return render(request,'Blog/blog-single.html',context)

def blog_search(request):
    posts = Post.objects.filter(published_time__lte = now , status = 1)
    if request.method == "GET":
        if s:= request.GET.get("s"):
            posts = posts.filter(content__contains = s)
    context = {'posts':posts}
    return render(request,'Blog/blog-home.html',context)

def blog_category(request,cat_name):
    posts = Post.objects.filter(published_time__lte = now , status = 1)
    posts = posts.filter(category__name = cat_name)
    context = {"posts":posts}
    return render(request,'Blog/blog-home.html',context)

def test(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'test.html',context)
