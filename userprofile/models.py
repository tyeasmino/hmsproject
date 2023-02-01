from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# This class is important 
class User(AbstractUser): 
    role = (('user', "USER"),
            ('admin', "ADMIN"),
            ('batchCoordinate',"BATCH COORDINATE"),
            ('provost',"PROVOST"),
            ('asst. provost',"ASST. PROVOST"), 
            ('house tutor',"HOUSE TUTOR"), 
            ('student', "STUDENT"))
    roles = models.CharField(max_length=20, choices=role, default="user") 


class Faculty_Member(models.Model): 
    member_pk = models.AutoField(primary_key=True)  
    designation = models.CharField(max_length=100)
    name = models.CharField(max_length=100)    
    department = models.CharField(max_length=100) 
    phone = models.IntegerField()  
    email_address = models.EmailField(max_length=100,blank=False,unique=True) 
   
    # default_pass = models.CharField(max_length=100, default="hmsfmember")  
     
    def __str__(self):
        return self.designation + " " + self.name 

        