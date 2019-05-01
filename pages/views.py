from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Person


class HomePageView(ListView):
    model = Person
    template_name = 'home.html'
    context_object_name = 'people'  # new


class AboutPageView(TemplateView):
    template_name = 'about.html'

