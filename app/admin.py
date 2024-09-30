from django.contrib import admin

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


admin.site.register(HeaderText)
admin.site.register(Slider)
admin.site.register(FooterText)
admin.site.register(AnimatedInfo)
admin.site.register(About)
admin.site.register(Timeline)
admin.site.register(Patients)
admin.site.register(OpeningHours)
admin.site.register(OurClinic)
admin.site.register(Socials)
