from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def ranked_list(request):
    return render(request, 'ranked_list.html')

def ranked_detail(request):
    return render(request, 'ranked_detail.html')

def spots_list(request):
    return render(request, 'spots_list.html')

def spot_detail(request):
    return render(request, 'spot_detail.html')

def about(request):
    return render(request, 'about.html')

def contribute(request):
    return render(request, 'contribute.html')