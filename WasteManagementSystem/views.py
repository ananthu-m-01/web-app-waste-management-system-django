import datetime
import random

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from WasteManagementSystem.models import*


def log(request):
    return render(request,'index.html')

def login_post(request):
    usn = request.POST['textfield']
    psw = request.POST['textfield2']
    res = Login.objects.filter(username=usn, password=psw)
    if res.exists():
        res = res[0]
        request.session['lid'] = res.id
        if res.userType == 'admin':
            return redirect('/admin_home')
        elif res.userType == 'pickupVehicle':
            return redirect('/pickup_vehicle_home')
        elif res.userType == 'krishibhavan':
            return redirect('/KrishibhavanHome')
        else:
            # return HttpResponse("<script>alert('No user Found');Window.location='/log'</script>")
            return HttpResponse("<script>alert('Invalid');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Invalid');window.location='/'</script>")


def  logout(request):
    request.session['lid'] = ''
    return HttpResponse("<script>alert('Logout Successful');window.location='/'</script>")

def admin_home(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'admin/index.html')


# def add_material(request):
#     return  render(request,'admin/Add-Material.html')
#
# def add_material_post(request):
#     m_name = request.POST['textfield']
#     des = request.POST['textarea']
#     price = request.POST['textfield2']
#     img = request.FILES['fileField']
#     dt = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
#     fs = FileSystemStorage()
#     fs.save(r'C:\Users\anant\PycharmProjects\untitled\WasteManagementSystem\static\material\\' + dt + '.jpg', img)
#     path = "/static/material/" + dt + '.jpg'
#     obj = Materials()
#     obj.materialName = m_name
#     obj.description = des
#     obj.price = price
#     obj.image = path
#     obj.save()
#     return HttpResponse("<script>alert('Added');window.location='/view_material'</script>")
#
# def update_material(request,id):
#     res = Materials.objects.get(id=id)
#     return render(request,'admin/Update-Material.html',{'data':res})
#
# def update_material_POST(request,id):
#     try:
#         m_name = request.POST['textfield']
#         des = request.POST['textarea']
#         price = request.POST['textfield2']
#         img = request.FILES['fileField']
#         dt = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
#         fs = FileSystemStorage()
#         fs.save(r'C:\Users\anant\PycharmProjects\untitled\WasteManagementSystem\static\material\\' + dt + '.jpg', img)
#         path = "/static/material/" + dt + '.jpg'
#         Materials.objects.filter(id=id).update(materialName=m_name,description=des,price=price,image=path)
#         return HttpResponse("<script>alert('Updated');window.location='/view_material'</script>")
#
#     except Exception as e:
#         m_name = request.POST['textfield']
#         des = request.POST['textarea']
#         price = request.POST['textfield2']
#         Materials.objects.filter(id=id).update(materialName = m_name,description = des, price = price)
#         return HttpResponse("<script>alert('Updated');window.location='/view_material'</script>")
#
#
# def delete_material(request,id):
#     Materials.objects.get(id=id).delete()
#     return HttpResponse("<script>alert('Deleted');window.location='/view_material'</script>")
#
def view_material(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Materials.objects.all()
        return render(request,'admin/View-Material.html', {'data': met})

def add_krishibhavan(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'admin/Add-Krishibhavan.html')

def add_krishibhavan_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        pin = request.POST['textfield3']
        ltt = request.POST['textfield4']
        lgt = request.POST['textfield5']
        email = request.POST['textfield6']
        ph = request.POST['textfield7']
        p = random.randint(0000,9999)
        if Login.objects.filter(username=email).exists():
            return HttpResponse("<script>alert('Email Already Exists');window.location='/add_krishibhavan#aaa'</script>")
        else:
            log = Login()
            log.username = email
            log.password=p
            log.userType = 'krishibhavan'
            log.save()

            obj = Krishibhavan()
            obj.LOGIN = log
            obj.name = name
            obj.place = place
            obj.pinCode = pin
            obj.latitude = ltt
            obj.logtitude = lgt
            obj.email = email
            obj.phoneNumber = ph
            obj.save()

            return HttpResponse("<script>alert('Added');window.location='/view_krishibhavan#aaa'</script>")

def update_krishibhavan(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        res = Krishibhavan.objects.get(id=id)
        return render(request,'admin/Update-Krishibhavan.html',{'data':res})

def update_krishibhavan_post(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        pin = request.POST['textfield3']
        ltt = request.POST['textfield4']
        lgt = request.POST['textfield5']
        ph = request.POST['textfield7']
        Krishibhavan.objects.filter(id=id).update(name=name, place=place, pinCode=pin, latitude=ltt, logtitude=lgt,phoneNumber=ph)
        return HttpResponse("<script>alert('Updated');window.location='/view_krishibhavan#aaa'</script>")

def delete_krishibhavan(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        Krishibhavan.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/view_krishibhavan#aaa'</script>")

def view_krishibhavan(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Krishibhavan.objects.all()
        return render(request,'admin/View-Krishibhavan.html',{'data': met})

def add_area(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'admin/Add-area.html')

def add_area_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        pnc = request.POST['textfield']
        wrd = request.POST['textfield2']
        obj = Area()
        obj.panchayath = pnc
        obj.wardNumber = wrd
        obj.save()
        return HttpResponse("<script>alert('Added');window.location='/view_area#aaa'</script>")

def update_area(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        res = Area.objects.get(id=id)
        return render(request,'admin/Update-Area.html',{'data':res})

def update_area_post(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        pnc = request.POST['textfield']
        wrdno = request.POST['textfield2']
        Area.objects.filter(id=id).update(panchayath=pnc, wardNumber=wrdno)
        return HttpResponse("<script>alert('Updated');window.location='/view_area#aaa'</script>")

def delete_area(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        Area.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/view_area#aaa'</script>")

def view_area(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Area.objects.all()
        return render(request,'admin/View-Area.html',{'data': met})

def add_pickupVehicle(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'admin/Add-PickipVehicle.html')

def add_pickupVehicle_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        ph = request.POST['textfield']
        email = request.POST['textfield1']
        vno = request.POST['textfield2']
        model = request.POST['textfield3']
        ftype = request.POST['textfield4']
        if Login.objects.filter(username=email).exists():
            return HttpResponse("<script>alert('Email Already Exists');window.location='/add_pickupVehicle#aaa'</script>")
        else:
            p = random.randint(00000, 99999)
            log = Login()
            log.username = email
            log.password = p
            log.userType = 'pickupVehicle'
            log.save()

            obj = PickupVehicle()
            obj.LOGIN = log
            obj.phoneNumber = ph
            obj.vehicleNumber = vno
            obj.model = model
            obj.fuelType = ftype
            obj.email = email
            obj.save()
            return HttpResponse("<script>alert('Added');window.location='/view_pickupVehicle#aaa'</script>")


def update_pickupVehicle(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        res = PickupVehicle.objects.get(id=id)
        return render(request,'admin/Update-PickupVehicle.html',{'data':res})

def update_pickupVehicle_post(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        ph = request.POST['textfield']
        v_no = request.POST['textfield2']
        model = request.POST['textfield3']
        ftype = request.POST['textfield4']
        PickupVehicle.objects.filter(id=id).update(phoneNumber=ph, vehicleNumber=v_no, model=model, fuelType=ftype)
        return HttpResponse("<script>alert('Updated');window.location='/view_pickupVehicle#aaa'</script>")

def delete_pickupVehicle(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        PickupVehicle.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/view_pickupVehicle#aaa'</script>")

def view_pickupVehicle(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = PickupVehicle.objects.all()
        return render(request,'admin/View-PickupVehicle.html',{'data': met})

def view_registeredUser(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = User.objects.all()
        return render(request,'admin/View-RegisteredUser.html',{'data': met})

def view_pickupReports(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = PickupReports.objects.all()
        return render(request,'admin/View-PickupReports.html',{'data': met})

def view_payment(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Payment.objects.all()
        return render(request,'admin/View-Payment.html',{'data':met})

def add_notification(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'admin/Add-Notification.html')

def add_notification_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        noti = request.POST['textfield']
        date = request.POST['textfield2']
        obj = Notification()
        obj.notification = noti
        obj.date = date
        obj.save()
        return HttpResponse("<script>alert('Added');window.location='/view_notification#aaa'</script>")

def update_notification(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        res = Notification.objects.get(id=id)
        return render(request,'admin/Update-Notification.html',{'data':res})

def update_notification_post(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        noti = request.POST['textfield']
        date = request.POST['textfield2']
        Notification.objects.filter(id=id).update(notification=noti,date=date)
        return HttpResponse("<script>alert('Updated');window.location='/view_notification#aaa'</script>")

def delete_notification(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        Notification.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/view_notification#aaa'</script>")


def view_notification(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Notification.objects.all()
        return render(request,'admin/View-Notification.html',{'data': met})

def view_complaint(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Complaint.objects.all()
        return render(request,'admin/View-Complaint.html',{'data': met})

def send_reply(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'admin/Send-Reply.html',{"id":id})

def send_reply_post(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        reply = request.POST['textarea']
        date = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        Complaint.objects.filter(id=id).update(reply=reply,replyDate=date)
        return render(request, 'admin/Send-Reply.html', {"id": id})

def view_feedback(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Feedback.objects.all()
        return render(request,'admin/View-Feedback.html',{'data': met})

def area_allocate(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        if Allocatedarea.objects.filter(PICKUPVEHICLE__id=id).exists():
            return HttpResponse("<script>alert('Already Allocated');window.location='/view_pickupVehicle#aaa'</script>")
        data = Area.objects.all()
        data1 = PickupVehicle.objects.get(id=id)
        return render(request,'admin/Area-Allocate.html',{"data":data,"data1":data1,"id":id})


def area_allocate_post(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        area = request.POST['select2']
        obj = Allocatedarea()
        obj.AREA_id = area
        obj.PICKUPVEHICLE_id = id
        obj.save()
        return HttpResponse("<script>alert('Updated');window.location='/view_allocated_area#aaa'</script>")

def view_allocated_area(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Allocatedarea.objects.all()
        return render(request, 'admin/View- Allocated-area.html', {'data': met})

def delete_allocated_area(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        Allocatedarea.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/view_allocated_area#aaa'</script>")

def change_password(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'admin/Change-password.html')

def change_password_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        crp = request.POST['textfield']
        np = request.POST['textfield2']
        cfp = request.POST['textfield3']
        data = Login.objects.filter(password=crp,id=request.session['lid'])
        # print(data)
        if data.exists():
            if np == cfp:
                if Login.objects.filter(password=np).exists():
                    return HttpResponse("<script>alert('Already exist');window.location='/change_password#aaa'</script>")
                else:
                    Login.objects.filter(id=request.session['lid']).update(password=cfp)
                    return HttpResponse("<script>alert('Password Updated');window.location='/'</script>")
            else:
                return HttpResponse("<script>alert('Mismatch');window.location='/change_password#aaa'</script>")
        else:
            return HttpResponse("<script>alert('Wrong Passowrd');window.location='/change_password#aaa'</script>")


def pickup_vehicle_home(request):
    return render(request,'Pickup-Vehicle/index.html')

def allocated_area_pickup(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Allocatedarea.objects.filter(PICKUPVEHICLE__LOGIN=request.session['lid'])
        return render(request,'Pickup-Vehicle/View-allocatedArea-Pickup.html',{'data':met})

def view_wasteDetails_pickup(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        ar = Allocatedarea.objects.get(PICKUPVEHICLE__LOGIN=request.session['lid'])
        # print(ar.AREA.wardNumber)
        met = WasteDetails.objects.filter(USER__wardnumber=ar.AREA.wardNumber, status='pending')
        return render(request,'Pickup-Vehicle/View-WasteDetalis-Pickup.html',{'data':met})

def set_collection_date(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'Pickup-Vehicle/Add-CollectionDate.html',{'id': id})

def set_collection_date_post(request, id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        date = request.POST['textfield']
        WasteDetails.objects.filter(id=id).update(status='setdate')
        obj = CollectionDate()
        obj.WASTEDETAILS = WasteDetails.objects.get(id=id)
        obj.PICKUPVEHICLE = PickupVehicle.objects.get(LOGIN=request.session['lid'])
        obj.date = date
        obj.collectedWaste = 'pending'
        obj.status = 'pending'
        obj.save()
        return HttpResponse("<script>alert('Collection Date Fixed');window.location='/view_wasteDetails_pickup#aaa'</script>")


def todayCollection(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        c = CollectionDate.objects.filter(date=datetime.datetime.now().strftime('%Y-%m-%d'), status='pending')
        return render(request,'Pickup-Vehicle/Today-Waste-Entry-Pickup.html',{'data':c})

def add_wasteEntry(request,id,uid):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        request.session['uid']=uid
        request.session['cid']=id
        c = CollectionDate.objects.get(id=id)
        return render(request,'Pickup-Vehicle/Add-WasteEntry-Pickup.html',{'data':c})

def wasteP_entry1(request):
    quantity = request.POST['textfield2']
    amount = request.POST['textfield3']
    request.session['quantity'] = quantity
    request.session['amount'] = amount
    return redirect('/wastePayment')
def add_waste_Entry_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        # quantity = request.POST['textfield2']
        # amount = request.POST['textfield3']
        # request.session['quantity'] = quantity
        # request.session['amount'] = amount
        id=request.session['cid']


        date = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        qry=supercoins.objects.filter(LOGIN=request.session['uid'])
        if qry.exists():
            ep=qry[0].coins
            points=int(request.session['quantity'])*0.5
            totalpoints=float(points)+float(ep)
            supercoins.objects.filter(LOGIN=request.session['uid']).update(coins=totalpoints)
            CollectionDate.objects.filter(id=id).update(collectedWaste=request.session['quantity'],status='collected')
            obj =  PickupPayment()
            obj.amount = request.session['amount']
            obj.date = date
            obj.PICKUPVEHICLE = PickupVehicle.objects.get(LOGIN=request.session['lid'])
            obj.COLLECTIONDATE = CollectionDate.objects.get(id=id)
            obj.paymentStatus = 'completed'
            obj.save()

            return HttpResponse("<script>alert('Waste Details Entered');window.location='/todayCollection#aaa'</script>")
        else:
            if int(request.session['quantity']) <= 1:
                obj1=supercoins()
                obj1.coins=0.5
                obj1.LOGIN_id=request.session['uid']
                obj1.save()
                CollectionDate.objects.filter(id=id).update(collectedWaste=request.session['quantity'], status='collected')
                obj = PickupPayment()
                obj.amount = request.session['amount']
                obj.date = date
                obj.PICKUPVEHICLE = PickupVehicle.objects.get(LOGIN=request.session['lid'])
                obj.COLLECTIONDATE = CollectionDate.objects.get(id=id)
                obj.paymentStatus = 'completed'
                obj.save()

                return HttpResponse(
                    "<script>alert('Waste Details Entered');window.location='/todayCollection#aaa'</script>")
            else:
                tcp=int(request.session['quantity']) * 0.5
                obj1 = supercoins()
                obj1.coins = tcp
                obj1.LOGIN_id = request.session['uid']
                obj1.save()
                CollectionDate.objects.filter(id=id).update(collectedWaste=request.session['quantity'], status='collected')
                obj = PickupPayment()
                obj.amount = request.session['amount']
                obj.date = date
                obj.PICKUPVEHICLE = PickupVehicle.objects.get(LOGIN=request.session['lid'])
                obj.COLLECTIONDATE = CollectionDate.objects.get(id=id)
                obj.paymentStatus = 'completed'
                obj.save()

                return HttpResponse(
                    "<script>alert('Waste Details Entered');window.location='/todayCollection#aaa'</script>")
        # return render(request, 'Pickup-Vehicle/Payment.html')


def view_wasteEntry(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        c = CollectionDate.objects.filter(PICKUPVEHICLE__LOGIN=request.session['lid'],status='collected')
        return render(request,'Pickup-Vehicle/View-Waste-Entry-Pickup.html',{'data':c})

def view_cashEntry(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        c = PickupPayment.objects.filter(PICKUPVEHICLE__LOGIN=request.session['lid'],paymentStatus='completed')
        return render(request,'Pickup-Vehicle/View-cash-entry.html',{'data':c})

def view_notification_Pickup(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Notification.objects.all()
        return render(request,'Pickup-Vehicle/View-Notification.html',{'data':met})

def change_password_pickup(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'Pickup-Vehicle/Change-Password-Pickup.html')

def change_password_pickup_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        crp = request.POST['textfield']
        np = request.POST['textfield2']
        cfp = request.POST['textfield3']
        data = Login.objects.filter(password=crp,id=request.session['lid'])
        if data.exists():
            if np == cfp:
                if Login.objects.filter(password=np).exists():
                    return HttpResponse("<script>alert('Already exist');window.location='/change_password_pickup'</script>")
                else:
                    Login.objects.filter(id=request.session['lid']).update(password=cfp)
                    return HttpResponse("<script>alert('Password Updated');window.location='/'</script>")
            else:
                return HttpResponse("<script>alert('Mismatch');window.location='/change_password_pickup'</script>")
        else:
            return HttpResponse("<script>alert('Wrong Passowrd');window.location='/change_password_pickup'</script>")



def KrishibhavanHome(request):
    return render(request,'Krishibhavan/index.html')

def ViewProfile(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        kr = Krishibhavan.objects.get(LOGIN=request.session['lid'])
        return render(request,'Krishibhavan/View-profile.html',{'data':kr})

def AddMaterial(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'Krishibhavan/Add-Material.html')

def add_material_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        m_name = request.POST['textfield']
        des = request.POST['textarea']
        price = request.POST['textfield2']
        quantity = request.POST['textfield3']
        img = request.FILES['fileField']
        dt = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r'C:\Users\anant\PycharmProjects\untitled\WasteManagementSystem\static\material\\' + dt + '.jpg', img)
        path = "/static/material/" + dt + '.jpg'
        obj = Materials()
        obj.materialName = m_name
        obj.description = des
        obj.price = price
        obj.image = path
        obj.quantity = quantity
        obj.save()
        return HttpResponse("<script>alert('Added');window.location='/ViewMaterial'</script>")

def update_material(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        res = Materials.objects.get(id=id)
        return render(request,'Krishibhavan/Update-Material.html',{'data':res})

def update_material_POST(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        try:
            m_name = request.POST['textfield']
            des = request.POST['textarea']
            price = request.POST['textfield2']
            qty = request.POST['textfield4']
            img = request.FILES['fileField']
            dt = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
            fs = FileSystemStorage()
            fs.save(r'C:\Users\anant\PycharmProjects\untitled\WasteManagementSystem\static\material\\' + dt + '.jpg', img)
            path = "/static/material/" + dt + '.jpg'
            Materials.objects.filter(id=id).update(materialName=m_name,description=des,price=price,image=path,quantity=qty)
            return HttpResponse("<script>alert('Updated');window.location='/ViewMaterial'</script>")

        except Exception as e:
            m_name = request.POST['textfield']
            des = request.POST['textarea']
            price = request.POST['textfield2']
            qty = request.POST['textfield4']
            Materials.objects.filter(id=id).update(materialName = m_name,description = des, price = price,quantity=qty)
            return HttpResponse("<script>alert('Updated');window.location='/ViewMaterial'</script>")


def delete_material(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        Materials.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/ViewMaterial'</script>")

def ViewMaterial(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Materials.objects.all()
        return render(request,'Krishibhavan/View-Material.html',{'data':met})

def ViewMaterilOrder(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = MaterialOrder.objects.filter(~Q(status="pending"))
        return render(request,'Krishibhavan/View-Material Order.html',{'data':met})

def ViewMaterilOrderItems(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = MaterialOrderSub.objects.filter(MATERIALORDER = id)
        data = []
        for i in met:
            total = int(i.Quantity)*int(i.MATERIALS.price)
            data.append(
                {
                    "id":i.id,
                    "Materialname":i.MATERIALS.materialName,
                    "price":i.MATERIALS.price,
                    "Quantity":i.Quantity,
                    "total":total
                }
            )
            # print(data)
        return render(request,'Krishibhavan/View-Material-Order-Items.html',{'data':data})

def ViewVegetablesOfUsers(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Vegetable.objects.all()
        return render(request,'Krishibhavan/View-VegetablesOf-Users.html',{'data':met})

def ViewVegetablesOfUsersPOST(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        veg = request.POST['textfield']
        met = Vegetable.objects.filter(vegetableName=veg)
        if met.exists():
            return render(request,'Krishibhavan/View-VegetablesOf-Users.html',{'data':met})
        else:
            return HttpResponse("<script>alert('The Vegetable is not Available');window.location='/ViewVegetablesOfUsers#aaa'</script>")

def sendCollectionRequest(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        request.session['sid']=id
        return render(request,'Krishibhavan/Send-Collection-Request.html')

def sendCollectionRequestPOST(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        Quantity = request.POST['textfield']
        Price = request.POST['textfield2']
        date = request.POST['textfield3']
        obj = VegetableCollectionRequest()
        obj.Quantity = Quantity
        obj.Price = Price
        obj.date = date
        obj.status = 'pending'
        obj.VEGETABLE_id=request.session['sid']
        obj.save()
        return HttpResponse("<script>alert('Request Sent Successfully');window.location='/ViewRequestStatus'</script>")

def deleteRequest(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        VegetableCollectionRequest.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/ViewRequestStatus#aaa'</script>")

def ViewRequestStatus(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = VegetableCollectionRequest.objects.all()
        return render(request,'Krishibhavan/View-Request-Status.html',{'data':met})

def ViewVegetableStock(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = VegetableStock.objects.all()
        return render(request,'Krishibhavan/View-Vegetable-Stock.html',{'data':met})

def ViewVegetableOrders(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = VegetableOrder.objects.filter(~Q(paymentStatus = 'pending'))
        return render(request,'Krishibhavan/View-Vegetable-Order.html',{'data':met})

def ViewVegetableItems(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = VegetableOrderSub.objects.filter(VEGETABLEORDER=id)
        data=[]
        for i in met:
            total=int(i.Quantity)*int(i.VEGETABLESTOCK.Amount)
            data.append(
                {
                    "id":i.id,
                    "vegetablename":i.VEGETABLESTOCK.VegetableName,
                    "Price":i.VEGETABLESTOCK.Amount,
                    "Quantity":i.Quantity,
                    "total":total
                }
            )

        return render(request,'Krishibhavan/View-Vegetable-Order-Items.html',{'data':data})

def ViewNotification(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        met = Notification.objects.all()
        return render(request,'Krishibhavan/View-Notification.html',{'data':met})

def changePassword(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        return render(request,'Krishibhavan/Change-Password-KrishiBhavan.html')

def changePassword_POST_KR(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        crp = request.POST['textfield']
        np = request.POST['textfield2']
        cfp = request.POST['textfield3']
        data = Login.objects.filter(password=crp,id=request.session['lid'])
        if data.exists():
            if np == cfp:
                if Login.objects.filter(password=np).exists():
                    return HttpResponse("<script>alert('Already exist');window.location='/changePassword'</script>")
                else:
                    Login.objects.filter(id=request.session['lid']).update(password=cfp)
                    return HttpResponse("<script>alert('Password Updated');window.location='/'</script>")
            else:
                return HttpResponse("<script>alert('Mismatch');window.location='/changePassword'</script>")
        else:
            return HttpResponse("<script>alert('Wrong Passowrd');window.location='/changePassword'</script>")

def todayApprovedRequest(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        c = VegetableCollectionRequest.objects.filter(date=datetime.datetime.now().strftime('%Y-%m-%d'), status='approved')
        return render(request,'Krishibhavan/View-Today-ApprovedStatus.html',{'data':c})

def updateVegetableStock(request,id,q,p):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        data=[]
        qry=VegetableStock.objects.filter(VegetableName=p)
        if qry.exists():
            amount=qry[0].Amount
            return render(request, 'Krishibhavan/Update-VegetableStock.html',
                          {'id': id, "data": amount, "vegtblename": p, "quantity": q})

        else:
            return render(request, 'Krishibhavan/Update-VegetableStock.html',
                          {'id': id, "data": "0", "vegtblename": p, "quantity": q})


def updatevegetableStockPOST(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    else:
        VegetableName = request.POST['textfield']
        Amount = request.POST['textfield2']
        qty = request.POST['qty']
        # print("quantity  : ",qty)
        qry=VegetableStock.objects.filter(VegetableName=VegetableName)
        if qry.exists():
            total_quantity=int(qry[0].quantity)+int(qty)
            VegetableStock.objects.filter(id=qry[0].id).update(quantity=total_quantity,Amount=Amount)
            VegetableCollectionRequest.objects.filter(id=id).update(status="collected")
            return HttpResponse("<script>alert('Updated');window.location='/todayApprovedRequest'</script>")
        else:
            obj=VegetableStock()
            obj.quantity=qty
            obj.Amount=Amount
            obj.status="Available"
            obj.KRISHIBHAVAN=Krishibhavan.objects.get(LOGIN=request.session['lid'])
            obj.VegetableName=VegetableName
            obj.save()
            VegetableCollectionRequest.objects.filter(id=id).update(status="collected")
            return HttpResponse("<script>alert('Updated');window.location='/todayApprovedRequest'</script>")



def and_login(request):
    user = request.POST['u']
    pss = request.POST['p']

    obj = Login.objects.filter(username=user, password=pss, userType="user")

    if obj.exists():
        q=User.objects.get(LOGIN=obj[0].id)
        # months = 90
        # today = datetime.datetime.now().today()
        # pastmonth = today - datetime.timedelta(months)
        # print(pastmonth.date())
        # fine = "false"
        # qry=CollectionDate.objects.filter(WASTEDETAILS__USER=q.id, date__gte=pastmonth.strftime("%Y-%m-%d"))
        # if qry.exists():
        #     fine="true"
        #     # d=qry[0].date
        #     # dd=d.split('-')
        #     # print("aaa",dd)
        #     # print("aaa1",dd[0],dd[1])
        #     # b=dd[0]+"-"+dd[1]
        #     # print("bbb",b)
        #     # months=90
        #     # today = datetime.datetime.now().today()
        #     # future_month = today + datetime.timedelta(months)
        #     # print("fff",future_month)
        #     # fdate = future_month.strftime("%Y-%m-%d")
        #     # print(fdate, "Here")
        #     # fd=fdate.split("-")
        #     # d=fdate[0]+"-"+fdate[1]
        #     # print("ddd",fd[0])
        #
        #     # Handle cases where the resulting month is greater than 12
        #     # if future_month.month > 12:
        #     #     future_month = future_month.replace(year=future_month.year + 1, month=future_month.month - 12)
        # print(fine)
        return JsonResponse({"status": "ok", "lid": obj[0].id,"n":q.name,"e":q.email})

    return JsonResponse({"status": "no"})


def and_add_vegetable(request):
    vegetableName = request.POST['vg']
    description = request.POST['des']
    Quantity = request.POST['qty']
    Amount = request.POST['amount']
    id = request.POST['lid']
    img = request.FILES['pic']
    dt = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    fs = FileSystemStorage()
    fs.save(r'C:\Users\anant\PycharmProjects\untitled\WasteManagementSystem\static\material\\' + dt + '.jpg', img)
    path = "/static/material/" + dt + '.jpg'
    obj = Vegetable()
    obj.vegetableName = vegetableName
    obj.description = description
    obj.quantity = Quantity
    obj.Amount = Amount
    obj.image = path
    obj.USER = User.objects.get(LOGIN=id)
    obj.save()
    return JsonResponse({"status" : "ok"})

def and_add_waste(request):
    wasteType = request.POST['type']
    quantity = request.POST['qty']
    id = request.POST['lid']
    obj = WasteDetails()
    obj.USER = User.objects.get(LOGIN=id)
    obj.wasteType = wasteType
    obj.quantity = quantity
    obj.status = 'pending'
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.save()
    return JsonResponse({"status" : "ok"})

def and_change_password(request):
    currentPassword = request.POST['crp']
    newPassword = request.POST['np']
    confirmPassword = request.POST['cfp']
    id = request.POST['lid']
    data=Login.objects.filter(password=currentPassword)
    if data.exists():
        if newPassword == confirmPassword:
            Login.objects.filter(id=id).update(password=confirmPassword)
            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "no"})
    else:
        return JsonResponse({"status": "no"})

def and_register(request):
    name = request.POST['name']
    phoneNumber = request.POST['ph']
    email = request.POST['mail']
    place =  request.POST['place']
    pinCode = request.POST['pc']
    wardnumber = request.POST['wrd']
    houseNumber = request.POST['hs']
    obj1 = Login()
    password = request.POST['pw']
    obj1.username = email
    obj1.password = password
    obj1.userType = 'user'
    obj1.save()

    obj = User()
    obj.name = name
    obj.phoneNumber = phoneNumber
    obj.email = email
    obj.place = place
    obj.pinCode = pinCode
    obj.wardnumber = wardnumber
    obj.houseNumber = houseNumber
    obj.LOGIN = obj1
    obj.save()

    return JsonResponse({"status" : "ok"})

def and_send_complaint(request):
    complaints = request.POST['Cmp']
    id = request.POST['lid']
    obj = Complaint()
    obj.complaint = complaints
    obj.complaintDate =datetime.datetime.now().strftime("%Y-%m-%d")
    obj.reply = 'pending'
    obj.replyDate = 'pending'
    obj.USER = User.objects.get(LOGIN_id=id)
    obj.save()
    return JsonResponse({"status" : "ok"})

def and_send_feedback(request):
    feedback = request.POST['feedback']
    id = request.POST['lid']
    obj = Feedback()
    obj.feedback = feedback
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.USER = User.objects.get(LOGIN=id)
    obj.save()
    return JsonResponse({"status" : "ok"})

def and_viewApprovedRequest(request):
    id = request.POST['lid']
    var = VegetableCollectionRequest.objects.filter(VEGETABLE__USER__LOGIN=id, status='approved')
    li = []
    if var.exists():
        for i in var:
            li.append({
                "quantity":i.Quantity,
                "name":i.VEGETABLE.vegetableName,
                "price":i.Price,
                "date":i.date
            })
    return JsonResponse({"status" : "ok","data":li})

def and_viewCollectionRequest(request):
    id = request.POST['lid']
    var = VegetableCollectionRequest.objects.filter(VEGETABLE__USER__LOGIN=id,status='pending')
    li = []
    if var.exists():
        for i in var:
            li.append({
                'id':i.id,
                "name":i.VEGETABLE.vegetableName,
                "quantity":i.Quantity,
                "price":i.Price,
                "date":i.date
            })

    # print(li)
    return JsonResponse({"status":"ok","data":li})

def and_viewMaterial(request):
    id = request.POST['lid']
    var = Materials.objects.all()
    li = []
    if var.exists():
        for i in var:
            li.append({
                "id":i.id,
                "materialName":i.materialName,
                "description":i.description,
                "price":i.price,
                "quantity":i.quantity,
                "image":i.image
            })
    return JsonResponse({"status": "ok","data":li})

def and_viewReply(request):
    id = request.POST['lid']
    var = Complaint.objects.filter(USER__LOGIN=id)
    li =[]
    if var.exists():
        for i in var:
            li.append({
                'complaint':i.complaint,
                "complaintDate":i.complaintDate,
                "reply":i.reply,
                "replyDate":i.replyDate})
    # print(li)
    return JsonResponse({"status" :"ok",'data':li})

def and_viewVegetable(request):
    var = VegetableStock.objects.all()
    li = []
    if var.exists():
        for i in var:
            li.append({
                "id":i.id,
                "vegetableName":i.VegetableName,
                "quantity":i.quantity,
                "Amount":i.Amount,
                "status":i.status
            })
    return JsonResponse({"status" : "ok","data":li})

def and_viewWaste(request):
    id = request.POST['lid']
    var = CollectionDate.objects.filter(WASTEDETAILS__USER__LOGIN=id,status='pending')
    li = []
    if var.exists():
        for i in var:
            li.append({
                "id":i.id,
                "type":i.WASTEDETAILS.wasteType,
                "quantity":i.WASTEDETAILS.quantity,
                "date":i.WASTEDETAILS.date,
                "collectionDate":i.date,
                "CollectedWaste":i.collectedWaste
            })
    return JsonResponse({"status":"ok","data":li})

def and_viewProfile(request):
    id = request.POST['lid']
    # print(id)
    var  = User.objects.get(LOGIN=id)
    return JsonResponse({"status":"ok","name":var.name, "phoneNumber":var.phoneNumber,"email":var.email,"place":var.place,"pinCode":var.pinCode,"wardNumber":var.wardnumber,"houseNumber":var.houseNumber})

def and_editProfile(request):

    lid = request.POST['lid']
    name = request.POST['name']
    phoneNumber = request.POST['ph']
    email = request.POST['email']
    place = request.POST['place']
    pinCode = request.POST['pinCode']
    wardNumber = request.POST['wardNumber']
    houseNumber = request.POST['houseNumber']
    User.objects.filter(LOGIN=lid).update(name=name,phoneNumber=phoneNumber,email=email,place=place,pinCode=pinCode,wardnumber=wardNumber,houseNumber=houseNumber)
    return JsonResponse({"status": "ok"})

def and_vegetableOrder(request):
    lid = request.POST['lid']
    stid=request.POST['id']
    data =VegetableStock.objects.get(id=stid)
    quanity = request.POST['quantity']

    res=VegetableOrder.objects.filter(VEGETABLESTOCK=stid,VEGETABLESTOCK__quantity__lt=quanity)
    if res.exists():
       return JsonResponse({"status":"non", "q": data.quantity})
    am = int(quanity) * int(data.Amount)
    qut=int(data.quantity)-int(quanity)

    VegetableStock.objects.filter(id=stid).update(quantity=qut)
    obj = VegetableOrder()
    obj.amount = am
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.status = 'ordred'
    obj.paymentStatus = 'offline'
    obj.USER=User.objects.get(LOGIN=lid)
    obj.VEGETABLESTOCK_id=stid
    obj.save()
    obj1 = VegetableOrderSub()
    obj1.VEGETABLEORDER=obj
    obj1.VEGETABLESTOCK_id=stid
    obj1.Quantity=quanity
    obj1.save()
    return JsonResponse({"status": "ok"})

def and_materialOrder(request):
    lid = request.POST['lid']
    stdid = request.POST['id']
    data = Materials.objects.get(id=stdid)
    quantity = request.POST['quantity']

    res = Materials.objects.filter(id=stdid, quantity__lt=quantity)

    if res.exists():
        return JsonResponse({"status":"non", "q": data.quantity})
    data = Materials.objects.get(id=stdid)
    am = int(quantity) * int(data.price)
    # print("total", quantity)
    # print("current", data.quantity)
    qut = int(data.quantity) - int(quantity)

    Materials.objects.filter(id=stdid).update(quantity=qut)
    obj = MaterialOrder()
    obj.amount = am
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.status = 'ordred'
    obj.paymentStatus = 'offline'
    obj.USER = User.objects.get(LOGIN=lid)
    obj.MATERIALS_id =stdid
    obj.save()
    obj1 = MaterialOrderSub()
    obj1.MATERIALORDER =obj
    obj1.MATERIALS_id =stdid
    obj1.Quantity =quantity
    obj1.save()
    return JsonResponse({"status": "ok"})

def and_viewVegetableOrder(request):
    id = request.POST['lid']
    var = VegetableOrderSub.objects.filter(VEGETABLEORDER__USER__LOGIN=id)
    li = []
    if var.exists():
        for i in var:
            li.append({
                "id":id,
                "vegetableName":i.VEGETABLESTOCK.VegetableName,
                "quantity":i.Quantity,
                "Amount":i.VEGETABLEORDER.amount,
                "date":i.VEGETABLEORDER.date
            })
    return JsonResponse({"status":"ok","data":li})

def and_viewMaterialOrder(request):
    id = request.POST['lid']
    var = MaterialOrderSub.objects.filter(MATERIALORDER__USER__LOGIN=id)
    li = []
    if var.exists():
        for i in var:
            li.append({
                "id":id,
                "materialName":i.MATERIALS.materialName,
                "quantity":i.Quantity,
                "Amount":i.MATERIALORDER.amount,
                "date":i.MATERIALORDER.date
            })
        return JsonResponse({"status":"ok","data":li})

def and_approveCollectionRequest(request):
    id = request.POST['lid']
    rid = request.POST['rid']
    VegetableCollectionRequest.objects.filter(id=rid).update(status='approved')
    return JsonResponse({"status": "ok"})

def and_rejectCollectionRequest(request):
    id = request.POST['lid']
    rid = request.POST['rid']
    VegetableCollectionRequest.objects.filter(id=rid).update(status='rejected')
    return JsonResponse({"status": "ok"})

def and_cancelWaste(request):
    id = request.POST['lid']
    wid = request.POST['wid']
    CollectionDate.objects.filter(id=wid).delete()
    return JsonResponse({"status": "ok"})

def and_viewCollectedWaste(request):
    id = request.POST['lid']
    var = CollectionDate.objects.filter(WASTEDETAILS__USER__LOGIN=id, status='collected')
    li = []
    if var.exists():
        for i in var:
            li.append({
                "id": i.id,
                "type": i.WASTEDETAILS.wasteType,
                "quantity": i.WASTEDETAILS.quantity,
                "date": i.WASTEDETAILS.date,
                "collectionDate": i.date,
                "CollectedWaste": i.collectedWaste
            })
    return JsonResponse({"status": "ok", "data": li})

# =========waste_payment========

def and_waste_payment(request):
    cid=request.POST['cid']
    lid=request.POST['lid']
    obj=Payment()
    obj.USER=User.objects.get(LOGIN=lid)
    obj.paymentStatus="paid"
    obj.amount=50
    obj.paymentType="online"
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.save()
    CollectionDate.objects.filter(id=cid).update(status="paid")
    return JsonResponse({"status":"ok"})

# ============supercoins===

def view_supercoins(request):
    lid=request.POST['lid']
    qry=supercoins.objects.filter(LOGIN=lid)
    if qry.exists():
        ep=qry[0].coins
        epp=float(ep)
        print(epp)
        am=float(epp)/10


        return JsonResponse({"status":"ok","points":ep,"amount":int(am)})
    else:
        return JsonResponse({"status":"no"})

# ========claim=
def claim_amount(request):
    lid=request.POST['lid']
    supercoins.objects.filter(LOGIN=lid).delete()
    return JsonResponse({"status":"ok"})

def wastePayment(request):
    import razorpay

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    amount = 50*100
    # amount = float(amount)

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    return render(request, 'Pickup-Vehicle/Payment.html',{'razorpay_api_key': razorpay_api_key,
                                            'amount': order_data['amount'],
                                            'currency': order_data['currency'],
                                            # 'order_id': order['id']
    })


def finish_payment(request):

    return HttpResponse("<script>alert('Waste Details Entered');window.location='/todayCollection#aaa'</script>")
