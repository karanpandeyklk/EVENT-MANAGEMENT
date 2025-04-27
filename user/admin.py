from django.contrib import admin
from .models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display =('Name','Email','Mobile','Message')
admin.site.register(contactus,contactusAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cpic','cdate')

admin.site.register(category,categoryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display =('id','spic','sdate')

admin.site.register(slider,sliderAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('id','city_name','city_picture')

admin.site.register(city,cityAdmin)

class placenameAdmin(admin.ModelAdmin):
    list_display = ('id','place','address','ppic','pdate')

admin.site.register(placename,placenameAdmin)

class eventAdmin(admin.ModelAdmin):
    list_display = ('id','event_category','speaker_name','hotel','city','event_picture','speaker_picture','price','dprice','event_date')

admin.site.register(event,eventAdmin)

class imagegalleryAdmin(admin.ModelAdmin):
    list_display = ('id','category','picture','eventdate','event_des')

admin.site.register(imagegallery,imagegalleryAdmin)

class videogalleryAdmin(admin.ModelAdmin):
    list_display = ('id','category','vlink','vdate','event_des')

admin.site.register(videogallery,videogalleryAdmin)
class registerAdmin(admin.ModelAdmin):
    list_display = ('email','uname','passwd','upic','address')
admin.site.register(register,registerAdmin)

class booknowAdmin(admin.ModelAdmin):
    list_display = ('id','userid','event_name','event_picture','speaker_name','city','hotel','speaker_picture','event_date','event_price','booking_date')
admin.site.register(booknow,booknowAdmin)