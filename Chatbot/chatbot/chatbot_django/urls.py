from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns =[
    path('',lambda request: redirect('login'), name='default_url'),
    path('chatbot',views.chatbot , name='chatbot'),
     path('login',views.login , name='login'),
      path('register',views.register , name='register'),
       path('logout',views.logout , name='logout'),
]