from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/hackathon', views.HackathonView.as_view()),
    path('api/contact', views.ContactView.as_view()),
]