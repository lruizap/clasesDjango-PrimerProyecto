# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name="home"),
    # Enlace de quienes_somos
    path('equipo/', views.quienes_somos, name="quienes_somos"),

]
