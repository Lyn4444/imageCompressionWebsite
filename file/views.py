from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload(request):
    return None


@csrf_exempt
def download(request):
    return None
