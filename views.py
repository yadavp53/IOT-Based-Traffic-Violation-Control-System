from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from datetime import date,datetime
from django.contrib.auth import authenticate,logout,login
from Tracker.tasks import *

def Login(request):
    MyTask.delay()
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['user']
        p = d['pwd']
        user = authenticate(username = u,password = p)
        if user is not None:
            if not user.is_staff:
               login(request,user)
               return redirect('home')
            elif user.is_staff:
                login(request, user)
                return redirect('admin_panel')
        else:
            error = True
    return render(request,'login.html',{"error":error})

def Logout(request):
    logout(request)
    return redirect('login')
################# Admin Panal Functions #################

def Admin_Panel(request):
    if not request.user.is_authenticated() or not request.user.is_staff:
        return redirect('login')

    all_vehicle = Vehicle_info.objects.all().order_by('-id')
    return render(request,'admin_panel.html',{"all_vehicle":all_vehicle})


def Vehicle_fine(request):
    if not request.user.is_authenticated() or not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        type = request.POST['type']
        fine = request.POST['fine']
        data = Fine_of_vehicle.objects.filter(v_type = type).first()
        if data:
            data.fine = fine
            data.save()
        else:
            Fine_of_vehicle.objects.create(v_type = type,fine = fine)
    fine_list = Fine_of_vehicle.objects.all()
    return render(request,'vehicle_fine.html',{"fine_list":fine_list})


def Add_vehicle(request):
    if not request.user.is_authenticated() or not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        d = request.POST
        name = d['name']
        mob = d['mob']
        add = d['add']
        rfid = d['rfid']
        v_num = d['v_num']
        type = d['type']
        Vehicle_info.objects.create(ownwr_name = name,ownwr_mob=mob,ownwr_add = add,
                                    rfid_no = rfid,vehicle_no = v_num,vehicle_type = type)
        return redirect('admin_panel')
    return render(request,'add_vehicle.html')

def Delete(request,num):
    if not request.user.is_authenticated() or not request.user.is_staff:
        return redirect('login')
    data = Vehicle_info.objects.filter(id = num).first()
    data.delete()
    return redirect('admin_panel')

######################User Functions
def Home(request):
    if not request.user.is_authenticated() or request.user.is_staff:
        return redirect('login')
    error = False
    today_date = date.today()
    upload_date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d-%m-%Y')
    if request.method == "POST":
        from datetime import datetime as dt
        now = dt.now().strftime('%H:%M:%S')
        d = request.POST
        vn = d['vehicle']
        time = now
        status = d['status']
        data = Vehicle_info.objects.filter(vehicle_no = vn).first()
        if data:
            if status == "Wrong":
                data2 = Fine_of_vehicle.objects.filter(v_type = data.vehicle_type).first()
                fine = data2.fine
            else:
                fine = 0
            Vehicle_status.objects.create(vehicle = data,status = status,entry_time = time
                                          ,entry_date = upload_date,fine = fine)
        else:
            error = True

    return render(request,'index.html',{"error":error})


def Todays_vehicle(request):
    if not request.user.is_authenticated() or request.user.is_staff:
        return redirect('login')
    today_date = date.today()
    today_date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d-%m-%Y')
    vehicles = Vehicle_status.objects.filter(entry_date = today_date)
    return render(request,'entry.html',{"vehicles":vehicles,"date":today_date})

def Entries_by_date(request):
        if not request.user.is_authenticated() or request.user.is_staff:
         return redirect('login')
        d = request.GET['entry_date']
        print(d)
        da = datetime.strptime(str(d), "%Y-%m-%d").strftime('%d-%m-%Y')
        data =Vehicle_status.objects.filter(entry_date = da)
        return render(request, 'entry.html', {"vehicles": data, "date": da})