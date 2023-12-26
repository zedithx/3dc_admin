from django.urls import path
from . import views

urlpatterns = [
    #Define api paths here
    path('hello-world/', views.hello_world, name='hello_world'),
]