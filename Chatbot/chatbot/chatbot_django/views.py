from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import auth

# Create your views here.

from hugchat import hugchat
from hugchat.login import Login





   


def chatbot(request):
    sign = Login('jicsocialmedia1234@gmail.com', 'QezS8>=^rfR~,"3')
    cookies = sign.login()

    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chatbot.query(message, web_search=True)
        
        return  JsonResponse({'message' : message , 'response' : str(response)})
    return render(request,'chatbot.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def logout(request):
    auth.logout(request)