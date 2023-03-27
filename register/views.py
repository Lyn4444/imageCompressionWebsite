import sqlite3
import time
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from utils.ParamUtils import *
from utils.JsonUtils import CreateJson
from utils.RequestDataUtil import CreateRequestData
from utils.Emulate import Emulate
from django.views.decorators.csrf import csrf_exempt
import utils.ParamUtils
from register import models


# Create your views here.
@csrf_exempt
def register(request):
    request.encoding = 'utf-8'
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    print("post register")
    if request.method != "POST":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        print("error: " + emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        post_data = request.POST.dict()
        print("post_data: " + str(post_data))
        if not post_data or not ParamCheck(emulate.login_param, post_data):
            data.setCode(emulate.ERRORPARAMCODE)
            data.setMsg(emulate.ERRORPARAMMSG)
            print("error: " + emulate.ERRORPARAMMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        elif not ContentCheck(post_data):
            data.setCode(emulate.ERRORNOCONTENTCODE)
            data.setMsg(emulate.ERRORNOCONTENTMSG)
            print("error: " + emulate.ERRORNOCONTENTMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        else:
            post_name = post_data['name']
            post_email = post_data['email']
            post_passwd = post_data['passwd']
            try:
                models.UserInfo.objects.get(name=post_name)
                data.setCode(emulate.ERRORDATAEXISTCODE)
                data.setMsg(emulate.ERRORDATAEXISTMSG)
                print("error: " + emulate.ERRORDATAEXISTMSG)
                return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
            except:
                salt = CreateSalt(32)
                passwd = EncryptMD5(post_passwd, salt)
                models.UserInfo.objects.create(
                    name=post_name,
                    email=post_email,
                    salt=salt,
                    passwd=passwd,
                    avatar="",
                    isdelete=False,
                    time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                )
                data.setCode(emulate.OKCODE)
                data.setMsg(emulate.OKMSG)
                print("success: " + emulate.OKMSG)
                return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
