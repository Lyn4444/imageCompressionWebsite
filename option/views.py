import os.path

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from utils.ParamUtils import ParamCheck, ContentCheck
from utils.Emulate import Emulate
from utils.RequestDataUtil import CreateRequestData
from utils.JsonUtils import CreateJson


@csrf_exempt
def do_first(request):
    request.encoding = 'utf-8'
    _json = CreateJson()
    data = CreateRequestData()
    emulate = Emulate()
    print("get do_first")
    if request.method != "GET":
        data.setCode(emulate.ERRORREQUESTCODE)
        data.setMsg(emulate.ERRORPARAMMSG)
        print("error: " + emulate.ERRORPARAMMSG)
        return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
    else:
        get_data = request.GET.dict()
        print("get_data: " + str(get_data))
        if not get_data or "filename" not in get_data:
            data.setCode(emulate.ERRORNOCONTENTCODE)
            data.setMsg(emulate.ERRORNOCONTENTMSG)
            print("error: " + emulate.ERRORNOCONTENTMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        elif not ContentCheck(get_data):
            data.setCode(emulate.ERRORNOCONTENTCODE)
            data.setMsg(emulate.ERRORNOCONTENTMSG)
            print("error: " + emulate.ERRORNOCONTENTMSG)
            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
        else:
            get_name = get_data['filename']
            filepath = 'module/input/' + str(get_name)
            if os.path.exists(filepath):
                try:
                    print("first command: " + "python module/generate_map.py " + filepath)
                    res = os.system("python module/generate_map.py " + filepath)
                    if res == 0:
                        print("second command: " + "python module/combine_images.py -image " + filepath
                              + " -map  module/output/msroi_map_" + str(get_name))
                        res1 = os.system("python module/combine_images.py -image " + filepath
                                         + " -map  module/output/msroi_map_" + str(get_name))
                        if res1 == 0:
                            data.setCode(emulate.OKCODE)
                            data.setMsg(emulate.OKMSG)
                            res_file_name = "_original_" + str(get_name) + "_50.jpg"
                            file_data = {"filename": res_file_name}
                            data.setData(file_data)
                            print("success: " + emulate.OKMSG)
                            return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
                except Exception as e:
                    print(e)
                    data.setCode(emulate.ERRORINTERIORCODE)
                    data.setMsg(emulate.ERRORINTERIORMSG)
                    print("error: " + emulate.ERRORINTERIORMSG)
                    return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
            else:
                data.setCode(emulate.ERRORNODATACODE)
                data.setMsg(emulate.ERRORNODATAMSG)
                print("error: " + emulate.ERRORNODATAMSG)
                return HttpResponse(_json.dict2json(data.getRequestData()), content_type="application/json")
