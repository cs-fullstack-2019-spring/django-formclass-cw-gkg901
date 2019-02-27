from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appForm', views.appForm, name='appForm'),
    path('formInfo', views.formInfo, name='formInfo'),
]
