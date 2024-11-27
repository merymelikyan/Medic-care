from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('timeline/', views.timeline, name="timeline"),
    path('booking/', views.booking, name="booking"),

]