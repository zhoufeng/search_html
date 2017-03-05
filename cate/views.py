# encoding=utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core  import serializers
import json
from seleniumutil import mobile1688CateParse;

# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")

def index(request):
    return render(request, 'home.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(unicode(c))

def search_ali_cate(request):
    url =request.POST["url"]
    mobile1688CateParse.parse(url);
    return
'''
返回json字符串
'''
def test(request):
    response_data = {}
    response_data['result'] = '哈哈'
    response_data['message'] = 'You messed up'
    return HttpResponse(json.dumps(response_data, ensure_ascii=False), content_type="application/json; charset=utf-8")