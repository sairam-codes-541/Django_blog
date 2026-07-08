from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Blog


def post_by_category(request,category_id):
    posts = Blog.objects.filter(status="Published", category = category_id)
    category= get_object_or_404(Category,pk=category_id)
   
    #later we will addd 404 error page
    context={
        "posts":posts,
        "category":category,
    }
    return render(request,'post_by_category.html',context)