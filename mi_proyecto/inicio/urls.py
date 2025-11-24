from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name="contacto"),
    path('mejoras/', views.formulario_mejora, name="mejoras"),
    path('listado_contactos/', views.listado_contactos, name="listado_contactos"),
    path('listado_contactos/<int:contacto_id>/',
         views.detalle_contacto, name="detalle_contacto"),
]
