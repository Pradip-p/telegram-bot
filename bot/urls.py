from django.urls import path
from . import views

urlpatterns = [
    #this is url of dashboard
    path('', views.home, name='home'),
    path('message_list', views.message_list, name="message_list"), # key_matrics
    path('key_matrics', views.key_matrics, name="key_matrics"), # key_matrics
    
]