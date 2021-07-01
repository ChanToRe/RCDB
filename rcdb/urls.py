from django.urls import path
from . import views

app_name = 'rcdb'

urlpatterns = [
    path('', views.index, name='index'),
]