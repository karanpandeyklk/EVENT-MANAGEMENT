from django.db import models

# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=100,null=True)
    Mobile=models.CharField(max_length=25,null=True)
    Message=models.TextField(null=True)
    def __str__(self):
        return self.Name
class category(models.Model):
    cname=models.CharField(max_length=200,null=True)
    cpic=models.ImageField(upload_to='static/category/',null=True)
    cdate=models.DateField()
    def __str__(self):
        return self.cname


class slider(models.Model):
    spic=models.ImageField(upload_to='static/slider/',null=True)
    sdate=models.DateField()

class city(models.Model):
    city_name=models.CharField(max_length=100)
    city_picture=models.ImageField(upload_to='static/city/',null=True)
    def __str__(self):
        return self.city_name

class placename(models.Model):
    place=models.CharField(max_length=200)
    address=models.TextField()
    ppic=models.ImageField(upload_to='static/Hotel/',null=True)
    pdate=models.DateField()
    def __str__(self):
        return self.place

class event(models.Model):
    event_category=models.ForeignKey(category,on_delete=models.CASCADE)
    speaker_name=models.CharField(max_length=200,null=True)
    hotel=models.ForeignKey(placename,on_delete=models.CASCADE)
    city=models.ForeignKey(city,on_delete=models.CASCADE)
    event_picture=models.ImageField(upload_to='static/event/',null=True)
    speaker_picture=models.ImageField(upload_to='static/speaker',null=True)
    price=models.IntegerField()
    dprice=models.IntegerField()
    event_date=models.DateField()
    event_detail=models.TextField(null=True)

class booknow(models.Model):
    userid=models.CharField(max_length=200,null=True)
    event_name=models.CharField(max_length=400,null=True)
    event_picture=models.CharField(max_length=400,null=True)
    speaker_name=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=50,null=True)
    hotel=models.CharField(max_length=200,null=True)
    speaker_picture=models.CharField(max_length=400,null=True)
    event_date=models.CharField(max_length=100,null=True)
    event_price=models.CharField(max_length=500,null=True)
    booking_date=models.DateField()


class imagegallery(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='static/gallery',null=True)
    event_des=models.TextField(null=True)
    eventdate=models.DateField()

class videogallery(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    vlink=models.TextField(null=True)
    vdate=models.DateField()
    event_des=models.TextField(null=True)
class register(models.Model):
    email=models.CharField(max_length=200,primary_key=True)
    uname=models.CharField(max_length=200,null=True)
    passwd=models.CharField(max_length=100,null=True)
    upic=models.ImageField(upload_to='static/profile',null=True)
    address=models.TextField(null=True)
