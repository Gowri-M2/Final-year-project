from  django.http import HttpResponse
from django.shortcuts import render,redirect
from canteen.models import *

def mainhome(request):
    return render(request,"index.html")

def userreg(request):
    return render(request,"canteen/register.html")


def userlogin(request):
    if request.method=='POST':
        usname=request.POST.get('username')
        passd=request.POST.get('psswd')
        user=user_details.objects.filter(user_fullname=usname,pwd=passd).count()

        if user > 0:
            #login (request,user)
            user=user_details.objects.filter(user_fullname=usname,pwd=passd).first()
            request.session['user_session']=True
            request.session['user_id']=usname
            request.session['uid']=user.id
            return redirect("/canteen/userhome/")
        else:
            return HttpResponse('Invalid Username And Password!!! ')
    return render(request,"canteen/userlogin.html")

def canteenlogin(request):
    if request.method=='POST':
        usname=request.POST.get('username')
        passd=request.POST.get('usercontactno')
        cuser=canteen_details.objects.filter(canteen_name=usname,ccontact_no=passd).count()

        if cuser > 0:
            #login (request,user)
            cuser=canteen_details.objects.filter(canteen_name=usname,ccontact_no=passd).first()
            request.session['canteen_session']=True
            request.session['canteen_name']=usname
            request.session['cid']=cuser.id
            return redirect("/canteen/chome/")
        else:
            return HttpResponse('Invalid Username And Password!!! ')
    return render(request,"canteen/canteenlogin.html")

def clogout(request):
    del request.session['canteen_session']
    return redirect('/')

def userlogout(request):
    del request.session['user_session']
    return redirect('/')