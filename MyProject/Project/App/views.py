from django.shortcuts import render
from django.http import HttpResponse
from App.models import QuemSomos
# Create your views here.
def index (request):
    quemsomos = QuemSomos.objects.all()
    context = {
        'quemsomos':quemsomos
    }
    return render(request, "index.html", context)
def a2(request):
    return HttpResponse("2.html")