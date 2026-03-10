from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Chocolatin, Spot

# Create your views here.

def ranked_list(request):
    chocolatines = Chocolatin.objects.filter(is_published=True).order_by('-score')
    return render(request, 'ranked_list.html', {'chocolatines': chocolatines})

def ranked_detail(request):
    return render(request, 'ranked_detail.html')

def spots_list(request):
    spots = Spot.objects.all()
    return render(request, 'spots_list.html', {'spots': spots})

def spot_detail(request):
    return render(request, 'spot_detail.html')

def about(request):
    return render(request, 'about.html')

def contribute(request):
    return render(request, 'contribute.html')