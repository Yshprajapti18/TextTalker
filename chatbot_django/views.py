from django.shortcuts import render,redirect
from django.http import JsonResponse , HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.

from hugchat import hugchat
from hugchat.login import Login
from .models import Chat
from django.utils import timezone
from django.shortcuts import redirect


   

def chatbot(request):
    credentials ={
        'EMAIL' : settings.EMAIL,
        'PASSWORD' : settings.PASSWORD
    }
    email = credentials['EMAIL']
    password = credentials['PASSWORD']
    sign = Login("jicsocialmedia1234@gmail.com", 'QezS8>=^rfR~,"3')
    cookies = sign.login()

    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    chats = Chat.objects.filter(user = request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chatbot.query(message, web_search=True)
        chat = Chat(user = request.user , message = message , response = response,created_at = timezone.now())
        chat.save()
        return  JsonResponse({'message' : message , 'response' : str(response)})
    return render(request,'chatbot.html', {'chats': chats})

def login(request):

    
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('chatbot')
        else:
            error_message ="WRONG USERNAME OR PASSWORD"
            return render(request,'login.html',{'error_message':error_message})
    else:        
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            try:
                user = User.objects.create_user(username,email,password1)
                user.save()
                
                return redirect('login')
            except:
                error_message ="ERROR CREATING A USER"
                return render(request,'register.html',{'error_message':error_message})
        else:
            error_message ="THE PASSWORD DOES NOT MATCH"
            return render(request,'register.html',{'error_message':error_message})    
        
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')