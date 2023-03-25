from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from utils.JsonUtils import CreateJson
from utils.DataUtils import CreateData
from utils.RequestDataUtil import CreateRequestData
from utils.Emulate import Emulate
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
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
        data.setCode(emulate.OKCODE)
        data.setMsg(emulate.OKMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
