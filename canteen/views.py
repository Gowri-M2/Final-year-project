from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request,"indira_canteen/chome.html")

def userhome(request):
    if 'q' in request.GET:
        q = request.GET['q']
        
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(caddress=q)  )
        
        data = canteen_details.objects.filter(multiple_q)
    else:
        data = canteen_details.objects.all()
        
    context = {
        'data': data
    }
     #vehl=vehical_location.objects.all()
    return render(request,"indira_canteen/home.html",context)
    
def changepin(request):
    return render(request,"indira_canteen/changepin.html")


def changepin_chk(request):
     uid=request.session['cid']
     
     if request.method=="POST":  #Pasrsing Parameters
        op=request.POST.get("op")
        np=request.POST.get("np")
        cp=request.POST.get("cp")
        if canteen_details.objects.filter(id=uid,ccontact_no=op) and np==cp:
          
          u=canteen_details.objects.get(id=uid)
          u.ccontact_no=np
          u.save()
     else:
         
         return render(request,"indira_canteen/changepin.html")
     return render(request,"indira_canteen/changepin.html")
def chome(request):
    return render(request,"indira_canteen/chome.html")

def canteen_form(request):
    if request.method=="POST":
        #take as foring key trnsaction


        c_name=request.POST.get("Canteen_name")
        c_emailid=request.POST.get("cmail_id")
        c_contactnumber=request.POST.get("ccontact_no")
        c_address=request.POST.get("caddress")
        c_location=request.POST.get("clocation")

        c=canteen_details()

        c.canteen_name=c_name
        c.cmail_id=c_emailid
        c.ccontact_no=c_contactnumber
        c.caddress=c_address
        c.clocation=c_location

        c.save()
        return redirect("/canteen/canteen_view/")

    return render(request,"indira_canteen/canteen_details.html")


def canteen_view(request):
    cview=canteen_details.objects.all()
    return render(request,"indira_canteen/canteen_view.html",{"cview":cview})


def canteen_del(request,cview_id):
    cview=canteen_details.objects.get(id=cview_id)
    cview.delete()
    return redirect("/canteen/canteen_view/")

def canteen_update(request,cview_id):
    civ=canteen_details.objects.get(id=cview_id)
    return render(request,"indira_canteen/canteen_update.html",{"civ":civ})

def canteen_edit(request,cview_id):
    if request.method=="POST":
        #take as foring key trnsaction


        c_name=request.POST.get("Canteen_name")
        c_emailid=request.POST.get("cmail_id")
        c_contactnumber=request.POST.get("ccontact_no")
        c_address=request.POST.get("caddress")
        c_location=request.POST.get("clocation")

        c=canteen_details(id=cview_id)

        c.canteen_name=c_name
        c.cmail_id=c_emailid
        c.ccontact_no=c_contactnumber
        c.caddress=c_address
        c.clocation=c_location

        c.save()
        return redirect("/canteen/canteen_view/")
    





def user_form(request):
    if request.method=="POST":
        u_fullname=request.POST.get("user_fullname")
        u_emailid=request.POST.get("user_emailid")
        u_user_contactnumber=request.POST.get("user_contactnumber")
        pwd=request.POST.get("pwd")

        u=user_details()

        u.user_fullname=u_fullname
        u.user_emailid=u_emailid
        u.user_contactnumber= u_user_contactnumber
        u.pwd= pwd

        u.save()
        messages.success(request,"Registerd successfully ....")
        #return redirect("/canteen/userlogin/")
    return render(request,"canteen/userlogin.html")
    
def user_view(request):
    uview=user_details.objects.all()
    return render(request,"indira_canteen/user_view.html",{"uview":uview})

def user_del(request,uview_id):
    uview=user_details.objects.get(id=uview_id)
    uview.delete()
    return redirect("/canteen/user_view/")

def user_update(request,uview_id):
    uview=user_details.objects.get(id=uview_id)
    return render(request,"indira_canteen/user_update.html",{"uview":uview})

def user_edit(request,uview_id):
    if request.method=="POST":
        u_fullname=request.POST.get("user_fullname")
        u_emailid=request.POST.get("user_emailid")
        u_user_contactnumber=request.POST.get("user_contactnumber")

        u=user_details(id=uview_id)

        u.user_fullname=u_fullname
        u.user_emailid=u_emailid
        u.user_contactnumber=u_user_contactnumber

        u.save()
        return redirect("/canteen/user_view/")


def food_form(request):
    if request.method=="POST":
        
        #take as foring key to transaction
        canteen=request.POST.get('canteen')
        cid=canteen_details.objects.get(id=canteen)
        f_name=request.POST.get("food_name")
        f_rate=request.POST.get("food_rate")
        f_image=request.FILES.get("food_image")

        f=food_details()
        f.canteen_id=cid
        f.food_name=f_name
        f.food_rate=f_rate
        f.food_image=f_image

        f.save()
        return redirect("/canteen/food_view/")

    return render(request,"indira_canteen/food_details.html",{'cvd':canteen_details.objects.all()})
def food_view(request):
    
    fview=food_details.objects.all()
    return render(request,"indira_canteen/food_view.html",{"fview":fview})

def food_del(request,fview_id):
    fview=food_details.objects.get(id=fview_id)
    fview.delete()
    return redirect("/canteen/food_view/")

def food_update(request,fview_id):
    fview=food_details.objects.get(id=fview_id)
    return render(request,"indira_canteen/food_update.html",{"fview":fview})

def food_edit(request,fview_id):
    if request.method=="POST":
        #take as foring key to transaction
        f_name=request.POST.get("food_name")
        f_rate=request.POST.get("food_rate")
        f_image=request.POST.get("food_image")

        f=food_details(id=fview_id)

        f.food_name=f_name
        f.food_rate=f_rate
        f.food_image=f_image

        f.save()
        return redirect("/canteen/food_view/")

def ctransaction_form(request):
    if request.method=="POST":
        t_canteenid=request.POST.get("canteen_id")
        tot=request.POST.get('total')
        canteenid=canteen_details.objects.get(id=t_canteenid)
        t_foodid=request.POST.get("food_id")
        foodid=food_details.objects.get(id=t_foodid)
        t_quantity=request.POST.get("food_quantity")
        t_date=request.POST.get("date")
        
    

        t=ctransaction()

        t.canteen_id=canteenid
        t.food_id=foodid
        t.food_quantity=t_quantity
        t.date=t_date
        t.total=tot

        t.save()
        return redirect("/canteen/ctransaction_view/")
        

    return render(request,"indira_canteen/transaction.html",{
        'cd':canteen_details.objects.all(),
        'fd':food_details.objects.all()
        })
def ctransaction_view(request):
    un=request.session['cid']
    tview=ctransaction.objects.filter(canteen_id=un)
    grand_total = sum(obj.total for obj in tview)
    

    #f=food_details.objects.filter('food_rate').first()
    return render(request,"indira_canteen/ctransaction_view.html",{"tview":tview,'grand_total':grand_total})

def ctransaction_del(request,tview_id):
    tview=ctransaction.objects.get(id=tview_id)
    tview.delete()
    return redirect("/canteen/ctransaction_view/")

def ctransaction_update(request,tview_id):
    tview=ctransaction.objects.get(id=tview_id)
    return render(request,"indira_canteen/ctransaction_update.html",{"tview":tview})

def ctransaction_edit(request,tview_id):
    if request.method=="POST":
        t_canteenid=request.POST.get("canteen_id")
        canteenid=canteen_details.objects.get(id=t_canteenid)
        t_foodid=request.POST.get("food_id")
        foodid=food_details.objects.get(id=t_foodid)
        t_quantity=request.POST.get("food_quantity")
        t_date=request.POST.get("date")
        
    

        t=ctransaction(id=tview_id)

        t.canteen_id=canteenid
        t.food_id=foodid
        t.food_quantity=t_quantity
        t.date=t_date

        t.save()
        return redirect("/canteen/ctransaction_view/")

def food_menu_form(request):
    if request.method=="POST":
        m_canteenid=request.POST.get("canteen_id")
        canteenid=canteen_details.objects.get(id=m_canteenid)
        m_foodid=request.POST.get("food_id")
        foodid=food_details.objects.get(id=m_foodid)
        m_date=request.POST.get("date")

        m=food_menu()
        m.canteen_id=canteenid
        m.food_id=foodid
        m.date=m_date

        m.save()
        return redirect("/canteen/fmenu_view/")


    return render(request,"indira_canteen/food_menu_details.html",{
        'cd':canteen_details.objects.all(),
        'fd':food_details.objects.all()
    })

def fmenu_view(request):
    un=request.session['cid']
    mview=food_menu.objects.filter(canteen_id=un)
    return render(request,"indira_canteen/fmenu_view.html",{"mview":mview})

def fmenu_view_user(request, cid):
    mview=food_menu.objects.filter(canteen_id=cid)
    return render(request,"indira_canteen/fmenu_view_user.html",{"mview":mview})

def fmenu_del(request,mview_id):
    mview=food_menu.objects.get(id=mview_id)
    mview.delete()
    return redirect("/canteen/fmenu_view/")

def fmenu_update(request,mview_id):
    mview=food_menu.objects.get(id=mview_id)
    return render(request,"indira_canteen/fmenu_update.html",{"mview":mview})

def fmenu_edit(request,mview_id):
    if request.method=="POST":
        m_canteenid=request.POST.get("canteen_id")
        canteenid=canteen_details.objects.get(id=m_canteenid)
        m_foodid=request.POST.get("food_id")
        foodid=food_details.objects.get(id=m_foodid)
        m_date=request.POST.get("date")

        m=food_menu(id=mview_id)
        m.canteen_id=canteenid
        m.food_id=foodid
        m.date=m_date

        m.save()
        return redirect("/canteen/fmenu_view/")


    

def ctransaction_view_date(request):
    if request.method=="POST":
            un=request.session['cid']
            dat=request.POST.get("s_date")
            tview=ctransaction.objects.filter(date=dat,canteen_id=un)
            print(dat)
            grand_total = sum(obj.total for obj in tview)
            return render(request,"indira_canteen/ctransaction_view.html",{"tview":tview,'grand_total':grand_total})
