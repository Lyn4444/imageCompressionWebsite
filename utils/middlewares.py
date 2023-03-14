from django.middleware.common import MiddlewareMixin


class ExceptionMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        print(exception)
        return None
