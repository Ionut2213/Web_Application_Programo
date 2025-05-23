from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'



class ClientTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home/clientview.html'