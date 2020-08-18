from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Titre, Personnel
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 15)
def index(request):
    requete = Service.objects.all()
    return render(request, 'service/service.html', {'services':requete})

@cache_page(60 * 15)
def personnel(request):
    requete = Personnel.objects.select_related('service')
    return render(request, 'service/personnel.html', {'personnels':requete})
