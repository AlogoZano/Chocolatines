from django.contrib import admin
from .models import Spot, Chocolatin, ChocolatinScore

# Register your models here.
admin.site.register(Spot)
admin.site.register(Chocolatin)
admin.site.register(ChocolatinScore)