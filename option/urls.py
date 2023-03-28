from django.urls import path
from . import views

urlpatterns = [
    path('do-first/', views.do_first, name='do_first')
]
