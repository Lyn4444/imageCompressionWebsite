from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from utils.ParamUtils import *
from utils.Emulate import Emulate
from utils.JsonUtils import CreateJson
from utils.RequestDataUtil import CreateRequestData


# Create your views here.
@csrf_exempt
def email(request):
    request.encoding = 'utf-8'
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    print("get email")
    if request.method != "GET":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        print("error: " + emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        get_data = request.GET.dict()
        print("get_data: " + str(get_data))
        if not get_data or "email" not in get_data:
            data.setCode(emulate.ERRORPARAMCODE)
            data.setMsg(emulate.ERRORPARAMMSG)
            print("error: " + emulate.ERRORPARAMMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        else:
            try:
                get_email = get_data['email']
                from_email = settings.DEFAULT_FROM_EMAIL
                subject = '你的一次性代码'
                text_content = str(get_email) + ',你好！\n我们已收到你要求获得PicSmart账号所用的一次性代码的申请。'
                html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [get_email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                data.setCode(emulate.OKCODE)
                data.setMsg(emulate.OKMSG)
                print("success: " + emulate.OKMSG)
                return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
            except:
                data.setCode(emulate.ERRORINTERIORCODE)
                data.setMsg(emulate.ERRORINTERIORMSG)
                print("error: " + emulate.ERRORINTERIORMSG)
                return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
