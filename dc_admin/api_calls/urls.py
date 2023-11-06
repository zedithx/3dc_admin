from django.urls import path
from . import views

urlpatterns = [
    #Define api paths ehre
    path('hello-world/', views.hello_world, name='hello_world'),
]