from django.shortcuts import render

# Create your views here.


def blog_home(request):
    return render(request, 'blog/home.html')


def quienes_somos(request):
    return render(request, "blog/quienes_somos.html")
