from django.urls import path
from . import views

app_name = 'rcdb'

urlpatterns = [
    #path('', views.index, name='index'),
    path('get_RCDB/', views.get_RCDB, name='get_RCDB'),
    path('apiRCDB/', views.apiRCDB, name='index')
]