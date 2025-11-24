from django.shortcuts import render, redirect
from .forms import ContactoForm, MejoraForm
from .models import Contacto

# Create your views here.


def inicio(request):
    return render(request, 'inicio/inicio.html')


# Formulario


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio:inicio')
    else:
        form = ContactoForm()

    return render(request, 'inicio/contacto.html', {'form': form})


def listado_contactos(request):
    buscar = request.GET.get('buscar', '')

    contactos = Contacto.objects.all().order_by('-creado')

    if buscar:
        contactos = (
            contactos.filter(nombre__icontains=buscar) |
            contactos.filter(email__icontains=buscar) |
            contactos.filter(mensaje__icontains=buscar)
        )

    return render(request, "inicio/listado_contactos.html", {
        "contactos": contactos,
        "buscar": buscar,
    })


def detalle_contacto(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    return render(request, "inicio/detalle_contacto.html", {
        "contacto": contacto,
    })

# Formulario de mejoras


def formulario_mejora(request):
    if request.method == 'POST':
        form = MejoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio:inicio')
    else:
        form = MejoraForm()

    return render(request, 'inicio/mejoras.html', {'form': form})
