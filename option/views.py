from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from utils.JsonUtils import CreateJson


def index(request):
    data = {
        'patient_name': '张三',
        'age': '25',
        'patient_id': '19000347',
        '诊断': '上呼吸道感染',
    }
    _json = CreateJson()
    return HttpResponse(_json.dict2json(data), content_type="application/json")
