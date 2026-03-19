from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Chocolatin, Spot, ChocolatinScore
import json
from django.conf import settings

# Create your views here.

def ranked_list(request):
    chocolatines = Chocolatin.objects.filter(is_published=True).order_by('-score')
    return render(request, 'ranked_list.html', {'chocolatines': chocolatines})

def ranked_detail(request, pk):
    chocolatin = Chocolatin.objects.get(pk=pk)
    rank = ChocolatinScore.objects.get(chocolatin=chocolatin)
    return render(request, 'ranked_detail.html', {'chocolatin': chocolatin, 'rank': rank})

def spots_list(request):
    spots = Spot.objects.all()
    return render(request, 'spots/spots_list.html', {'spots': spots})

def spot_detail(request, pk):
    spot = Spot.objects.get(pk=pk)
    return render(request, 'spots/spot_detail.html', {'spot': spot})

def about(request):
    return render(request, 'about.html')

def contribute(request):
    return render(request, 'contribute.html')

def spots_map(request):
    spots = Spot.objects.all()

    spots_data = [
        {
            "name": spot.name,
            "lat": spot.latitude,
            "lng": spot.longitude,
            "id": spot.id,
        }
        for spot in spots
    ]

    return render(request, "spots/map.html", {
        "spots_json": json.dumps(spots_data),
        "GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY,
    })