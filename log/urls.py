from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_log, name='add_log'),
]


