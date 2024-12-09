from django.shortcuts import render

from . import models

# Create your views here.

def home(request):
    return render(request, 'index.html')

def detail(request, pk):
    product = models.Product.objects.get(pk=pk)
    return render(request, 'detail.html', {'product': product})