# pages/urls.py
from django.urls import path

from .views import HomePageView, AboutPageView
#test git
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]