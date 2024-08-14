# your_app_name/urls.py

from django.urls import path
from chat.views import *

urlpatterns = [
    path('chat/', chat_home, name='chat_home'),
    path('chat/<str:username>/', chat_home, name='chat_home')
]
