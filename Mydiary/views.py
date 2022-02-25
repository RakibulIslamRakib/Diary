from django.shortcuts import render,redirect
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def show(request):
    posts = Posts.objects.filter(user=request.user)     
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        posts = Posts(title=title,content=content,user = request.user)
        posts.save()
        return redirect(show)
    return render(request,'showdiary.html',{'posts':posts,'user':request.user })


def deletepost(request,post_id):
    post = Posts.objects.get( pk = int(post_id)) 
    post.delete()
    return redirect(show)

def editpost(request, post_id):
    if request.method=='POST':
        content = request.POST['content']
        title = request.POST['title']
        post = Posts.objects.get( pk = int(post_id)) 
        post.title = title
        post.content = content
        post.save()
        return redirect(show)

    else:
        post = Posts.objects.get( pk = int(post_id))
        return render(request,'editpost.html',{'post':post}) 


@login_required(login_url='/accounts/login')
def post_details(request,post_id):
    post = Posts.objects.get( pk = int(post_id)) 
    return render(request,'post_details.html',{'post':post})
