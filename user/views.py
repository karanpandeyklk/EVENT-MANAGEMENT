from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from datetime import datetime
# Create your views here.
def index(request):
    data=category.objects.all().order_by('-id')[0:12]
    sliderdata=slider.objects.all().order_by('-id')[0:3]
    edata=event.objects.all().order_by('-id')[0:8]
    edata1=event.objects.all().order_by('-id')[0:6]
    #print(data)
    md={"cdata":data,"sdata":sliderdata,"edata":edata,"edata1":edata1}
    return render(request,'user/index.html',md)
def about(request):
    return render(request,'user/aboutus.html')
def contact(request):
    if request.method=="POST":
        a1=request.POST.get('name')
        a2=request.POST.get('email')
        a3=request.POST.get('mobile')
        a4=request.POST.get('message')
        #print(a1,a2,a3,a4)
        x=contactus(Name=a1,Email=a2,Mobile=a3,Message=a4).save()
        return HttpResponse("<script>alert('Thank you for contacting with us');location.href='/user/contact/' </script>")


    return render(request,'user/contactus.html')
def signin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        x=register.objects.filter(email=email,passwd=passwd).count()
        if x==1:
            a=register.objects.filter(email=email,passwd=passwd)
            request.session['username']=str(a[0].uname)
            request.session['userpic']=str(a[0].upic)
            request.session['user']=email
            return HttpResponse("<script>alert('you are Signed in');location.href='/user/signin/'</script>")
        else:
            return HttpResponse("<script>alert('your user id passwrd is incorrect');location.href='/user/signin/'</script>")
    return render(request,'user/signin.html')
def signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        address=request.POST.get('address')
        picture=request.FILES['fu']
        a=register.objects.filter(email=email).count()
        if a==0:
            register(email=email,uname=name,passwd=passwd,address=address,upic=picture).save()
            return HttpResponse("<script>alert('you are registerd successfully..');location.href='/user/signup/'</script>")
        else:
            return HttpResponse("<script>alert('Yuo are already registered...');location.href='/user/signup/'</script>")
    return render(request,'user/signup.html')
def myevent(request):
    cid=request.GET.get('msg')
    sdata=request.GET.get('search')
    if cid is not None:
        edata=event.objects.filter(event_category=cid)
    elif sdata is not None:
        edata=event.objects.filter(Q(speaker_name__icontains=sdata))
    else:
        edata=event.objects.all().order_by('-id')
    md={"edata":edata}
    return render(request,'user/event.html',md)

def igallery(request):
    cid=request.GET.get('cid')
    if cid is not None:
        idata=imagegallery.objects.filter(category=cid)
    else:
        idata=imagegallery.objects.all().order_by('-id')
    cdata=category.objects.all().order_by('-id')
    mydict={"idata":idata,"cdata":cdata}
    return render(request,'user/igallery.html',mydict)

def vgallery(request):
    cid=request.GET.get('x')
    cdata=category.objects.all().order_by('-id')
    if cid is not None:
        vdata=videogallery.objects.filter(category=cid)
    else:
        vdata=videogallery.objects.all().order_by('-id')
    mydict={
        "cdata":cdata,
        "vdata":vdata,
    }
    return render(request,'user/vgallery.html',mydict)

def viewdetails(request):
    eid=request.GET.get('msg')
    edata=event.objects.filter(id=eid)
    md={"edata":edata}
    return render(request,'user/viewdetails.html',md)

def logout(request):
    user=request.session.get('user')
    if user:
        del request.session['user']
        del request.session['username']
        del request.session['userpic']
        return HttpResponse("<script>alert('you are logout...');location.href='/user/index/'</script>")

    return render(request,'user/logout.html')
def booking(request):
    user = request.session.get('user')
    if user:
        title = request.GET.get('title')
        spic = request.GET.get('spic')
        sname = request.GET.get('sname')
        city = request.GET.get('city')
        hotel = request.GET.get('hotel')
        price = request.GET.get('price')
        edate = request.GET.get('edate')
        epic = request.GET.get('epic')
        booknow(userid=user,event_name=title,event_picture=epic, speaker_name=sname,city=city,hotel=hotel,event_date=edate,event_price=price,speaker_picture=spic,booking_date=datetime.now().date()).save()
        return HttpResponse("<script>alert('Your event booked successfully...');location.href='/user/event/'</script>")

        return render(request,'user/booking.html')
def myticket(request):
    bid=request.GET.get('bid')
    user=request.session.get('user')
    ticket="";
    if user:
        ticket=booknow.objects.filter(userid=user)
    if bid is not None:
        booknow.objects.filter(id=bid).delete()
        return HttpResponse("<script>alert('Your ticket have been deleted..');location.href'/user/myticket/'</script>")
    md={"myticket":ticket}
    return render(request,'user/myticket.html',md)
def myprofile(request):
    user=request.session.get('user')
    rdata="";
    if user:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            passwd = request.POST.get('passwd')
            address = request.POST.get('address')
            picture = request.FILES['fu']
            register(email=user,passwd=passwd,address=address,upic=picture).save()
            return HttpResponse("<script>alert('Your event booked successfully...');location.href='/user/event/'</script>")
        rdata=register.objects.filter(email=user)
    md={"mdata":rdata}
    return render(request,'user/myprofile.html',md)