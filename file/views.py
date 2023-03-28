import os.path

from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from utils.ParamUtils import ParamCheck
from utils.Emulate import Emulate
from utils.JsonUtils import CreateJson
from utils.RequestDataUtil import CreateRequestData


# Create your views here.
@csrf_exempt
def upload(request):
    request.encoding = 'utf-8'
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    print("post upload")
    if request.method != "POST":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        print("error: " + emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        file = request.FILES["file"]
        post_data = request.POST.dict()
        print("post_data: " + str(post_data))
        if file and "filename" in post_data:
            file_name = post_data['filename']
            if file_name:
                print("origin filename: " + file.name + "\tnew filename: " + file_name)
                try:
                    with open("module/input/" + str(file_name), "wb") as f:
                        for chunk in file.chunks():
                            f.write(chunk)
                    data.setCode(emulate.OKCODE)
                    data.setMsg(emulate.OKMSG)
                    print("success: " + emulate.OKMSG)
                    return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
                except:
                    data.setCode(emulate.ERRORINTERIORCODE)
                    data.setMsg(emulate.ERRORINTERIORMSG)
                    print("error: " + emulate.ERRORINTERIORMSG)
                    return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
            else:
                data.setCode(emulate.ERRORNOCONTENTCODE)
                data.setMsg(emulate.ERRORNOCONTENTMSG)
                print("error: " + emulate.ERRORNOCONTENTMSG)
                return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        else:
            data.setCode(emulate.ERRORNOCONTENTCODE)
            data.setMsg(emulate.ERRORNOCONTENTMSG)
            print("error: " + emulate.ERRORNOCONTENTMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")


@csrf_exempt
def download(request):
    request.encoding = 'utf-8'
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    print("post download")
    if request.method != "GET":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        print("error: " + emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        file_path = "module/input/"
        get_data = request.GET.dict()
        print("get_data: " + str(get_data))
        if get_data and 'filename' in get_data:
            file_path = file_path + str(get_data['filename'])
            if os.path.exists(file_path):
                try:
                    with open(file_path, "rb") as f:
                        content = f.read()
                    response = FileResponse(content)
                    response["Content-Type"] = "application/octet-stream"
                    response["Content-Disposition"] = 'attachment; filename=' + str(get_data['filename'])
                    return response
                except:
                    data.setCode(emulate.ERRORINTERIORCODE)
                    data.setMsg(emulate.ERRORINTERIORMSG)
                    print("error: " + emulate.ERRORINTERIORMSG)
                    return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
            else:
                data.setCode(emulate.ERRORNODATACODE)
                data.setMsg(emulate.ERRORNODATAMSG)
                print("error: " + emulate.ERRORNODATAMSG)
                return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        else:
            data.setCode(emulate.ERRORNOCONTENTCODE)
            data.setMsg(emulate.ERRORNOCONTENTMSG)
            print("error: " + emulate.ERRORNOCONTENTMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
