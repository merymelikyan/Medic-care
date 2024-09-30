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

    return render(request,"base.html", context)

