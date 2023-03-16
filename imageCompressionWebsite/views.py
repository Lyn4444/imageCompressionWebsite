from django.shortcuts import redirect


def redirect_view_home(request):
    response = redirect('/home/')
    return response
