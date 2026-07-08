from django.shortcuts import render
from blogs.models import Category,Blog
from assignments.models import About,SocialLinks

def home(request):
   
    posts = Blog.objects.filter(is_featured = False,status = 'Published').order_by('-updated_at')
    sociallinks = SocialLinks.objects.all()
    featured_posts=Blog.objects.filter(is_featured = True,status = 'Published').order_by('-updated_at')
    

    # fetch abou us
    try:
         about = About.objects.get()
    except:
         about = None
    
    context={
        "posts":posts,
        "about":about,
        "featured_posts": featured_posts,
        "sociallinks":sociallinks

    }
    return render(request,'home.html',context)