from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('perfil/', views.perfil, name="perfil"),
]