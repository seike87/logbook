from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_log, name='add_log'),
    path('list', views.list_log, name='list_log'),
]


