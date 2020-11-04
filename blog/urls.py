from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='home'),
    path('contact', views.contact, name='contact')
]
