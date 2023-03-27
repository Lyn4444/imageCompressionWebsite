from __future__ import unicode_literals

from django.core.cache import cache
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
def get_email(request):
    request.encoding = 'utf-8'
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    print("get get-email")
    get_data = request.GET.dict()
    if request.method != "GET":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        print("error: " + emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    elif not ContentCheck(get_data):
        data.setCode(emulate.ERRORNOCONTENTCODE)
        data.setMsg(emulate.ERRORNOCONTENTMSG)
        print("error: " + emulate.ERRORNOCONTENTMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        print("get_data: " + str(get_data))
        if not get_data or "email" not in get_data:
            data.setCode(emulate.ERRORPARAMCODE)
            data.setMsg(emulate.ERRORPARAMMSG)
            print("error: " + emulate.ERRORPARAMMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        else:
            try:
                get_email = get_data['email']
                try:
                    if cache.get(str(get_email)):
                        data.setCode(emulate.ERRORREPEATCODE)
                        data.setMsg(emulate.ERRORREPEATMSG)
                        print("error: " + emulate.ERRORREPEATMSG)
                        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
                    else:
                        code = CreateCode()
                        cache.set(str(get_email), code, timeout=60)
                        from_email = settings.DEFAULT_FROM_EMAIL
                        subject = '你的一次性代码'
                        text_content = str(
                            get_email) + ',你好！\n我们已收到你要求获得PicSmart账号所用的一次性代码的申请。\n你的一次性代码为：' + code \
                                       + "\n如果你没有申请此代码，可放心忽略这封电子邮件。别人可能错误地键入了你的电子邮件地址。\n谢谢！\nPicSmart账号团队"
                        html_content = '<p><strong>' + str(get_email) + '</strong>，你好！</p><br/><p>我们已收到你要求获得PicSmart' \
                                                                        '账号所用的一次性代码的申请。</p><br/><p>你的一次性代码为：' + code + \
                                       '</p><br/><p>如果你没有申请此代码，可放心忽略这封电子邮件。别人可能错误地键入了你的电子邮件地址。</p><br/><p>谢谢！</p><br' \
                                       '/><p' \
                                       '>PicSmart账号团队</p>'
                        msg = EmailMultiAlternatives(subject, text_content, from_email, [get_email])
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                        data.setCode(emulate.OKCODE)
                        data.setMsg(emulate.OKMSG)
                        print("email: " + str(get_email) + "\tcode: " + code)
                        print("success: " + emulate.OKMSG)
                        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
                except:
                    data.setCode(emulate.ERRORINTERIORCODE)
                    data.setMsg(emulate.ERRORINTERIORMSG)
                    print("error: " + emulate.ERRORINTERIORMSG)
                    return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
            except:
                data.setCode(emulate.ERRORINTERIORCODE)
                data.setMsg(emulate.ERRORINTERIORMSG)
                print("error: " + emulate.ERRORINTERIORMSG)
                return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")


@csrf_exempt
def set_email(request):
    request.encoding = 'utf-8'
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    print("post set-email")
    if request.method != "POST":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        print("error: " + emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        post_data = request.POST.dict()
        print("post_data: " + str(post_data))
        _list = ['code', 'email']
        if not post_data or not ParamCheck(_list, post_data):
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
            post_email = post_data['email']
            post_code = post_data['code']
            try:
                if not cache.get(str(post_email)):
                    data.setCode(emulate.ERRORNODATACODE)
                    data.setMsg(emulate.ERRORNODATAMSG)
                    print("error: " + emulate.ERRORNODATAMSG)
                    return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
                else:
                    origin_code = cache.get(str(post_email))
                    print("email: " + str(post_email) + "\tcode: " + post_code + "\torigin code: " + str(origin_code))
                    if str(origin_code) == post_code:
                        cache.delete(str(get_email))
                        data.setCode(emulate.OKCODE)
                        data.setMsg(emulate.OKMSG)
                        print("success: " + emulate.OKMSG)
                        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
                    else:
                        data.setCode(emulate.ERRORDATAEXISTCODE)
                        data.setMsg(emulate.ERRORDATAEXISTMSG)
                        print("error: " + emulate.ERRORDATAEXISTMSG)
                        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
            except:
                data.setCode(emulate.ERRORINTERIORCODE)
                data.setMsg(emulate.ERRORINTERIORMSG)
                print("error: " + emulate.ERRORINTERIORMSG)
                return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")

