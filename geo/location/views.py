import json

from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.

def index(request):
    res = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=9a504b5fc9da4fa7a18c3b00f4aeba1a")
    data=res.content
    data1=json.loads(data)
    return render(request,'index.html',dict(data=data1))


