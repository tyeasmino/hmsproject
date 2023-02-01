from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from userprofile.models import Faculty_Member, User
from hallinfo.models import HallInfo, RoomInfo, RoomDetail


# Create your views here. 
def index(request):  
    if request.user.is_anonymous:
        return redirect("signin")  
    
    fmember = Faculty_Member.objects.all() 
    hallinfo = HallInfo.objects.all() 

    data = {
        'fmember' : fmember,  
        'hallinfo' : hallinfo,  
    }
    return render(request, 'userprofile/index.html', data)  

def signin(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 

        # Check if user has etered correct credentials
        user = authenticate(username=username, password=password) 
        if user is not None: 
            login(request, user) 
            return redirect("/") 
        else:
            return render(request, 'userprofile/signin.html') 

    return render(request, 'userprofile/signin.html') 

def signout(request): 
    logout(request) 
    return redirect("signin")  


@login_required
def ManageFacultyMember(request): 
    if request.method == "POST": 
        designation = request.POST.get('designation')
        name = request.POST.get('name')
        department = request.POST.get('department')
        phone = request.POST.get('phone')
        email_address = request.POST.get('email_address')

        fmemeber_new = Faculty_Member(designation=designation, name=name, department=department, phone=phone, email_address=email_address)
        fmemeber_new.save()

        
    fmember = Faculty_Member.objects.all()

    data = {
        'fmember' : fmember,  
    }
    return render(request, 'userprofile/ManageFacultyMember.html', data)  


@login_required
def ManageHallInfo(request):  
    if request.method == "POST": 
        hall_id = request.POST.get('hall_id')
        name = request.POST.get('name')
        residence_type = request.POST.get('residence_type')
        provost_id = request.POST.get('provost_name') 
        print(provost_id) 
        provost = Faculty_Member.objects.get(member_pk=provost_id) 
        hall_launch_date = request.POST.get('hall_launch_date') 
        temp_pass = hall_id + provost.email_address  

        hinfo_new = HallInfo(hall_id=hall_id, name=name, residence_type=residence_type, 
        provost_name=provost, hall_launch_date=hall_launch_date, temp_pass=temp_pass) 
        hinfo_new.save()  

        user = User()
        user.username = provost.email_address
        user.first_name = provost.name 
        user.set_password(temp_pass) 
        user.is_active = True 
        # user.is_instructor = True
        user.roles = 'provost'
        user.save()  


    fmember = Faculty_Member.objects.all()
    hallinfo = HallInfo.objects.all() 

    data = {
        'fmember' : fmember,  
        'hallinfo' : hallinfo,  
    }
    return render(request, 'userprofile/ManageHallInfo.html', data)  


@login_required
def ManageRoomInfo(request): 
    if request.method == "POST": 
        hall_id = request.POST.get('hall_name') 
        hall = HallInfo.objects.get(hall_pk=hall_id)  
        room_no = request.POST.get('room_no')
        room_capacity = request.POST.get('room_capacity')
        room_allotment = request.POST.get('room_allotment') 
        room_empty = int(room_capacity) - int(room_allotment)
        comment = request.POST.get('comment')

        rinfo_new = RoomInfo(hall_name=hall, room_no=room_no, room_capacity=room_capacity, 
        room_allotment=room_allotment, room_empty=room_empty, comment=comment) 
        rinfo_new.save()  


    hallinfo = HallInfo.objects.all()
    roominfo = RoomInfo.objects.all()
    fmember = Faculty_Member.objects.all()
    roomdetails = RoomDetail.objects.all() 

    data = {
        'hallinfo' : hallinfo, 
        'roominfo' : roominfo,
        'fmember' : fmember,  
        'roomdetails' : roomdetails, 
    } 

    return render(request, 'userprofile/ManageRoomInfo.html', data)  


@login_required
def ManageRoomDetail(request):
    if request.method == "POST": 
        selected_room_id = request.POST.get('selected_room_id') 
        select_room = RoomInfo.objects.get(room_pk=selected_room_id)  
        student_id = request.POST.get('student_id') 
        student_name = request.POST.get('student_name') 
        balance = request.POST.get('balance') 
        comment = request.POST.get('comment') 

        rdetails_new = RoomDetail(select_room=select_room, student_id=student_id, student_name=student_name, 
        balance=balance, comment=comment)  
        rdetails_new.save()  

    roominfo = RoomInfo.objects.all()
    roomdetails = RoomDetail.objects.all() 

    data = {
        'roominfo' : roominfo,
        'roomdetails' : roomdetails,  
    } 

    return render(request, 'userprofile/ManageRoomDetail.html', data)


@login_required
def room_with_details(request, room_pk): 
    room_with_details = RoomDetail.objects.filter(select_room = room_pk) 
    room_name = RoomInfo.objects.get(room_pk = room_pk) 
    only_room_name = room_name.room_no
    roominfo = RoomInfo.objects.all()
    
    data = {  
        'room_with_details' : room_with_details,          
        'roominfo' : roominfo, 
        'only_room_name' : only_room_name,
    } 

    return render(request, 'userprofile/ManageRoomInfo.html', data)  