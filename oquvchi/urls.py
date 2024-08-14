from django.urls import path

from oquvchi.views import *

urlpatterns = [
    path('', asosiy, name='asosiy'),
    path('yonalish/<int:id>', yonalish, name='yonalish'),
    path('topshiriq/<int:id>', topshiriq, name='topshiriq'),
    path('oquvchi/', oquvchi_update, name='oquvchi'),
    path('tolov/', tolov, name='tolov'),
    path('help/', help, name='help')
]