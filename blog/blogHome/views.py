from django.shortcuts import render,HttpResponse,redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def home(request):
    data=Blog.objects.all()
    print(data)
    context = {
        "blog":data
    }
    return render(request,"home.html",context) 

def contentreading(request,id):
    data = Blog.objects.get(id=id)
    com = Comments.objects.all()
    reply = Reply.objects.all()
    context={
        "blog":data,
        "comments":com,
        "reply":reply,
    }
    return render(request,'contentreading.html',context)

def signup(request):
    if request.method=="POST":
        name = request.POST.get("suname")
        email = request.POST.get("suemail")
        password = request.POST.get("supassword")
        print(name,email,password)
        user = User.objects.create_user(first_name=name,username=email, email=email,password=password)
        user.save()
        return redirect("Home")   
    return render(request,"signup.html")

def Login(request):
    if request.method=="POST":
        email = request.POST.get("suemail")
        password = request.POST.get("supassword")
        print(email,password)
        user = authenticate(request,username=email,password=password)
        print(user)
        if user is not None:
            messages.success(request, "Login successfully.")
            login(request,user)
            return redirect("Home")
        else:
            messages.warning(request, "Invalid credentials Try again.")
            return redirect("Login") 
    return render(request,"login.html")

def Logout(request):
    logout(request)
    messages.success(request, "Logout successfully.")
    return redirect("Home")

def comment(request):
    if request.method=="POST":
        name =  request.user  
        blog_id = request.POST.get("blogid")
        comment = request.POST.get("comment")
        blog = Blog.objects.get(id=blog_id)
         
        com = Comments(name=name,blogparent=blog ,comment=comment)
        com.save()
        messages.success(request,"comment successfully added")
    return redirect(f"contentreading/{blog_id}")

def reply(request):
    if request.method == "POST":
        name = request.user
        reply = request.POST.get("reply")
        comment_id = request.POST.get("commentid")
        blog_id = request.POST.get("blogid")
        comment_parent = Comments.objects.get(id=comment_id)
        rep = Reply(name=name,commentparent=comment_parent,reply=reply)
        rep.save()
    return redirect(f"contentreading/{blog_id}")

 