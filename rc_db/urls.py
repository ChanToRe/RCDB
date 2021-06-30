from django.urls import path
from . import views

app_name = 'rc_db'

urlpatterns = [
    path('', views.index, name='index'),
]