from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from utils.Emulate import Emulate
from utils.RequestDataUtil import CreateRequestData
from utils.JsonUtils import CreateJson


def login(request):
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    print("get login")
    if request.method != "GET":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        print(request)
        get_data = request.GET.dict()
        print("get_data: " + str(get_data))
        data.setCode(emulate.OKCODE)
        data.setMsg(emulate.OKMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")

