from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from utils.JsonUtils import CreateJson
from utils.RequestDataUtil import CreateRequestData
from utils.Emulate import Emulate


# Create your views here.
def login(request):
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    if request.method == "GET":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        # print(request.body)
        data.setCode(emulate.OKCODE)
        data.setMsg(emulate.OKMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
