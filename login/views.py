from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from utils.JsonUtils import CreateJson


# Create your views here.
def login(request):
    return HttpResponse("ok")
