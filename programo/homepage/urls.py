from django.urls import path, include
from . import views

urlpatterns = [
    path('home_page/', views.HomeTemplateView.as_view(), name = 'home-page'),
    path('clientview/', views.ClientTemplateView.as_view(), name = 'client-page'),
    
]