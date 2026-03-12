from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='ranked', permanent=True)),

    path('ranked/', views.ranked_list, name='ranked'),
    path('ranked/<int:pk>/', views.ranked_detail, name='ranked_detail'),

    path('spots/', views.spots_list, name='spots'),
    path('spots/<int:pk>/', views.spot_detail, name='spot_detail'),

    path('about/', views.about, name='about'),
    path('contribute/', views.contribute, name='contribute'),
]