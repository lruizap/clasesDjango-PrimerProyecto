from django import forms
from .models import Contacto, Mejora


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']


class MejoraForm(forms.ModelForm):
    class Meta:
        model = Mejora
        fields = ['nombre', 'email', 'sugerencia', 'prioridad']
