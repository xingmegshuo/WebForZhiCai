from django.shortcuts import render
from .models import *
from django.http.response import JsonResponse


# Create your views here.

# 首页
def home_view(request):
    desc = Desc.objects.all()
    video = Video.objects.all()
    return render(request, 'video/home.html', {"desc": desc, "video": video})


# 登录
def login(request):
    account = request.POST.get('account')
    password = request.POST.get('passwd')
    user = User.objects.get(phone=account,)
    return JsonResponse({"ok"})