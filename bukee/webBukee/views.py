from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "webBukee/base.html")

def index(request):
    return render(request, "webBukee/pages/index.html")

def contacto(request):
    return render(request, "webBukee/pages/Contacto.html")