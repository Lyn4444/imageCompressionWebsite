from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from utils.ParamUtils import ParamCheck
from utils.JsonUtils import CreateJson
from utils.DataUtils import CreateData
from utils.RequestDataUtil import CreateRequestData
from utils.Emulate import Emulate
from django.views.decorators.csrf import csrf_exempt
from register import models
from utils.ParamUtils import *


# Create your views here.
@csrf_exempt
def login(request):
    request.encoding = 'utf-8'
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    print("get login")
    if request.method != "GET":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        print("error: " + emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        get_data = request.GET.dict()
        print("get_data: " + str(get_data))
        if not get_data or not ParamCheck(emulate.login_param, get_data):
            data.setCode(emulate.ERRORPARAMCODE)
            data.setMsg(emulate.ERRORPARAMMSG)
            print("error: " + emulate.ERRORPARAMMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        elif not ContentCheck(get_data):
            data.setCode(emulate.ERRORNOCONTENTCODE)
            data.setMsg(emulate.ERRORNOCONTENTMSG)
            print("error: " + emulate.ERRORNOCONTENTMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        else:
            get_name = get_data['name']
            get_email = get_data['email']
            get_passwd = get_data['passwd']
            try:
                tmp = models.UserInfo.objects.get(name=get_name)
                dict_data = tmp.toJSON()
                tmp.toString(dict_data.get("id"))
                if EncryptMD5(get_passwd, dict_data.get('salt')) != dict_data.get('passwd'):
                    data.setCode(emulate.ERRORPARAMCODE)
                    data.setMsg(emulate.ERRORPARAMMSG)
                    print("error: " + emulate.ERRORPARAMMSG)
                    return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
                elif dict_data.get('isdelete'):
                    data.setCode(emulate.ERRORNODATACODE)
                    data.setMsg(emulate.ERRORNODATAMSG)
                    print("error: " + emulate.ERRORNODATAMSG)
                    return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
                else:
                    dict_data.pop('salt')
                    dict_data.pop('passwd')
                    dict_data.pop('isdelete')
                    data.setCode(emulate.OKCODE)
                    data.setMsg(emulate.OKMSG)
                    data.setData(dict_data)
                    print("success: " + emulate.OKMSG)
                    return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
            except:
                data.setCode(emulate.ERRORNODATACODE)
                data.setMsg(emulate.ERRORNODATAMSG)
                print("error: " + emulate.ERRORNODATAMSG)
                return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")

