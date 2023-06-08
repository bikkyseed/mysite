from email import message
from django.shortcuts import render, HttpResponse, redirect
from sympy import content
from home.models import Contact, Admit
from django.contrib import messages
from blog.models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



def home(request):
    allPosts = Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'home/home.html',context)

def about(request):
    return render(request, 'home/about.html')

def tool(request):
    return render(request, 'home/tool.html')

def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<10:
            messages.error(request,' Please fill from Correctly')
        else:
             contact = Contact(name=name,email=email,phone=phone,content=content)
             contact.save()
             messages.success(request, 'Your form has been successfully sent')

    return render(request, 'home/contact.html')

#for pass creation    

def admit(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<10:
            messages.error(request,' Please fill from Correctly')
        else:
            admit = Admit(name=name,email=email,phone=phone,content=content)
            admit.save()
            messages.success(request, 'Your form has been successfully sent')

    return render(request, 'home/admit.html')


def search(request):
    query = request.GET['query']

    if len(query)>78:
        allPosts = Post.objects.none()
    else:    
     allPostsTitle = Post.objects.filter(title__icontains=query)
     allPostsContent = Post.objects.filter(content__icontains=query)
     allPosts = allPostsTitle.union(allPostsContent)     

    if allPosts.count()==0:
        messages.error(request, 'No Search Quey,Please refine Your Query') 
    params = {'allPosts': allPosts, 'query':query}
    return render(request,'home/search.html',params)
    #return HttpResponse("this is search")
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

         #for checking username alredy exists 
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "password did not match the")
            return redirect('home')
        if not username.isalnum():
            messages.warning(request,"Usernaem Should only contains numbers and characters")  
            return redirect('home')      
        
        #check inputs
        #creating user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been successfully created")
        return redirect('home')

       

    else:
        return HttpResponse('404 Not Found') 

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user =  authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('home')
        else:
            messages.warning(request,"Invalid credentials")  
            return redirect('home')  
        
    return HttpResponse("404 : Error")

def handleLogout(request):
    logout(request)
    messages.success(request,"Succesfully Logout")
    return redirect('home')

# Create your views here.
