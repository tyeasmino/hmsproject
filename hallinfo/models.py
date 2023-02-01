from django.db import models
from userprofile.models import Faculty_Member 

# Create your models here.
class HallInfo(models.Model): 
    hall_pk = models.AutoField(primary_key=True) 
    hall_id = models.CharField(max_length=10, unique=True) 
    name = models.CharField(max_length=200, blank=False)
    gender = (('Male', "MALE"),
              ('Female', "FEMALE"))
    residence_type = models.CharField(max_length=10, choices=gender, default="Male", blank=False)
    provost_name = models.ForeignKey(Faculty_Member, on_delete=models.CASCADE)   
    hall_launch_date = models.DateField()  
    temp_pass = models.CharField(max_length=100, default="hmsprovost")  

    def __str__(self): 
        return self.name 


class RoomInfo(models.Model): 
    room_pk = models.AutoField(primary_key=True)
    hall_name = models.ForeignKey(HallInfo, on_delete=models.CASCADE) 
    room_no = models.CharField(max_length=20, unique=True)
    room_capacity = models.IntegerField()
    room_allotment = models.IntegerField() 
    room_empty = models.IntegerField() 
    comment = models.CharField(max_length=200, blank=True) 

    def __str__(self):
        return self.room_no 

    
class RoomDetail(models.Model): 
    room_details_pk = models.AutoField(primary_key=True) 
    select_room = models.ForeignKey(RoomInfo, on_delete=models.CASCADE) 
    student_id = models.CharField(max_length=15, unique=True) 
    student_name = models.CharField(max_length=100, blank=False)   
    balance = models.FloatField() 
    comment = models.CharField(max_length=200, blank=True) 

    def __str__(self):
        return self.student_id 
    