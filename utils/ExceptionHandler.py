from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.db.models import ObjectDoesNotExist
from django.http import Http404


class CustomExceptionHandler:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, ValidationError):
            return Response({
                'detail': str(exception)
            }, status=status.HTTP_400_BAD_REQUEST)
        elif isinstance(exception, ObjectDoesNotExist):
            return Response({
                'detail': 'Resource not found'
            }, status=status.HTTP_404_NOT_FOUND)
        elif isinstance(exception, Http404):
            return Response({
                'detail': 'Resource not found'
            }, status=status.HTTP_404_NOT_FOUND)
        else:
            response = exception_handler(exception, None)
            if response is not None:
                return Response({
                    'detail': response.data
                }, status=response.status_code)
            return Response({
                'detail': str(exception)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
