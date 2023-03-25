from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from utils.ParamUtils import *
from utils.JsonUtils import CreateJson
from utils.RequestDataUtil import CreateRequestData
from utils.Emulate import Emulate
from django.views.decorators.csrf import csrf_exempt
import utils.ParamUtils

# Create your views here.
@csrf_exempt
def register(request):
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    print("post register")
    if request.method != "POST":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        post_data = request.POST.dict()
        print("post_data: " + str(post_data))
        if not post_data or not ParamCheck(emulate.login_param, post_data):
            data.setCode(emulate.ERRORPARAMCODE)
            data.setMsg(emulate.ERRORPARAMMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        else:
            name = post_data['name']
            email = post_data['email']
            post_passwd = post_data['passwd']
            salt = CreateSalt(32)
            passwd = EncryptMD5(post_passwd, salt)
            data.setCode(emulate.OKCODE)
            data.setMsg(emulate.OKMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")