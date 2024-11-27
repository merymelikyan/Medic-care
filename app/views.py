from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from .models import (
    HeaderText, 
    Slider,
    FooterText,
    AnimatedInfo,
    About,
    Timeline,
    Patients,
    OpeningHours,
    OurClinic,
    Socials
  )  


def index(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "slider": Slider.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "animated_info": AnimatedInfo.objects.all().first(),
        "about": About.objects.all().first(),
        "timeline": Timeline.objects.all(),
        "patients": Patients.objects.all(),
        "opening_hours": OpeningHours.objects.all().first(),
        "our_clinic": OurClinic.objects.all().first(),
        "socials": Socials.objects.all()
    }

    return render(request,"home.html", context)



def about(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "about": About.objects.all().first(),
        "opening_hours": OpeningHours.objects.all().first(),
        "our_clinic": OurClinic.objects.all().first(),
        "socials": Socials.objects.all()
        
    }
    return render(request, "about.html", context)



def contact(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "opening_hours": OpeningHours.objects.all().first(),
        "our_clinic": OurClinic.objects.all().first(),
        "socials": Socials.objects.all()
        
    }
    return render(request, "contact.html", context)



def booking(request):
    context = {
        "header_text": HeaderText.objects.all(),       
        "footer_text": FooterText.objects.all().first(),
        "opening_hours": OpeningHours.objects.all().first(),
        "our_clinic": OurClinic.objects.all().first(),
        "socials": Socials.objects.all()
        
    }
    return render(request, "booking.html", context)



def testimonials(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "patients": Patients.objects.all(),
        "opening_hours": OpeningHours.objects.all().first(),
        "our_clinic": OurClinic.objects.all().first(),
        "socials": Socials.objects.all()
        
    }
    return render(request, "testimonials.html", context)



def timeline(request):
    context = {
        "header_text": HeaderText.objects.all(),
        
        "footer_text": FooterText.objects.all().first(),
        
        "timeline": Timeline.objects.all(),
        "opening_hours": OpeningHours.objects.all().first(),
        "our_clinic": OurClinic.objects.all().first(),
        "socials": Socials.objects.all()
        
    }
    return render(request, "timeline.html", context)


