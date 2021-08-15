from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("안녕하세요 pybo app 에 오신걸 환영합니다")