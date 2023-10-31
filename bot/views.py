from django.shortcuts import render
from .models import *
from .pagination import set_pagination
from django.contrib.auth.decorators import login_required

def key_matrics(request):
    members = BotUser.objects.all().order_by('-id')
    context = {
        'members': members
    }
    return render(request, 'key_matrics.html', context)

def message_list(request):
    messages = MessageContent.objects.all().order_by('-time')
    messages = set_pagination(request, messages)
    context = {'messages':messages,}
    return render(request, 'message_list.html', context)

# @login_required(login_url='/')
def home(request):
    members = BotUser.objects.all().order_by('-id')
    context = {
               'members':members,
               }
    return render(request, 'index.html', context)