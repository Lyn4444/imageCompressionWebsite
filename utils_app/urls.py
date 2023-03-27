from django.urls import path
from . import views

urlpatterns = [
    path('get-email/', views.get_email, name='get-email'),
    path('set-email/', views.set_email, name='set-email')
]