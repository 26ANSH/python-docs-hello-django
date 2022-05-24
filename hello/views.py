from django.http import HttpResponse
from django.shortcuts import render
import os

def hello(request):
    if "USER_NAME" in os.environ:
        return HttpResponse(f"<h1>Hello, World!</h1><br>This is Ansh from Azure CLI")
    else:
        return HttpResponse(f"<h1>Hello, {os.environ['USER_NAME']}!</h1><br>This is Ansh from Azure CLI")
        
        
        
        
