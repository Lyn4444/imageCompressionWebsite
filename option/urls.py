from django.urls import path
from . import views

urlpatterns = [
    path('do-first/', views.do_first, name='do_first'),
    path('do-second/', views.do_second, name='do_second')
]
