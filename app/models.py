from django.db import models

class HeaderText(models.Model):
    tag = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Text"


class Slider(models.Model):
    img = models.ImageField(upload_to="slider", blank=True, null=True)
    
    def __str__(self):
        return f"{self.img}"

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"


class FooterText(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    text3 = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return f"{self.text1} {self.text2} {self.text3}"

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"       


class AnimatedInfo(models.Model):
    tag = models.CharField(max_length=50)
    title1 = models.CharField(max_length=255, blank=True, null=True)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    title3 = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=250)
    phone = models.CharField(max_length=25, blank=True, null=True)
    

    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name = "Animated Info"
        verbose_name_plural = "Animated Info"       


class About(models.Model):
    title = models.CharField(max_length=25)
    description1 = models.TextField(max_length=250, blank=True, null=True)
    description2 = models.TextField(max_length=250, blank=True, null=True)
    years = models.CharField(max_length=55)
    text = models.TextField(max_length=55)
    gallery_image1 = models.ImageField(upload_to="image1", blank=True, null=True)
    gallery_image2 = models.ImageField(upload_to="image2", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"


class Timeline(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, null=True, blank=True)
    icon_class= models.CharField(max_length=50, null=True, blank=True, help_text="FontAwesome icon")
    data = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Timeline"
        verbose_name_plural = "Timeline"    


class Timeline1(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.TextField(max_length=250, blank=True, null=True)
    description2 = models.TextField(max_length=250, blank=True, null=True)
    description3 = models.TextField(max_length=250, null=True, blank=True)
    icon_class= models.CharField(max_length=50, null=True, blank=True, help_text="FontAwesome icon")
    link_url = models.URLField(max_length=200, blank=True, null=True) 
    data = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Timeline1"
        verbose_name_plural = "Timeline1"    


class Timeline2(models.Model):
    title = models.CharField(max_length=50)
    description1 = models.TextField(max_length=250, blank=True, null=True)
    description2 = models.TextField(max_length=250, blank=True, null=True)
    icon_class= models.CharField(max_length=50, null=True, blank=True, help_text="FontAwesome icon")
    data = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Timeline2"
        verbose_name_plural = "Timeline2"    

 
class Patients(models.Model):
    reviews_class1  = models.CharField(max_length=400, blank=True, null=True)
    reviews_class2  = models.CharField(max_length=400, blank=True, null=True)
    reviews_class3 = models.CharField(max_length=400, blank=True, null=True)
    reviews_class4  = models.CharField(max_length=400, blank=True, null=True)
    reviews_class5  = models.CharField(max_length=400, blank=True, null=True)
    name = models.CharField(max_length=45)
    position = models.CharField(max_length=60)
    description1 = models.TextField(max_length=250, blank=True, null=True)
    description2 = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to="patients", blank=True, null=True)
      
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Patients"
        verbose_name_plural = "Patients"


class OpeningHours(models.Model):
    title = models.CharField(max_length=60)
    days1 = models.CharField(max_length=60)
    days2 = models.CharField(max_length=60)
    open_time1 = models.CharField(max_length=60)
    open_time2 = models.CharField(max_length=60)
    close_time = models.CharField(max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Opening Hours"
        verbose_name_plural = "Opening Hours"       


class OurClinic(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=255, blank=True)
    name_url = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Our Clinic"
        verbose_name_plural = "Our Clinic"       


class Socials(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=255, blank=True)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"       