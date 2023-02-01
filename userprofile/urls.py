from django.contrib import admin
from django.urls import path, include  
from userprofile import views

urlpatterns = [
    path('', views.index, name="home"),
    path('signin', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),   
    path('ManageFacultyMember', views.ManageFacultyMember, name="ManageFacultyMember"), 
    path('ManageHallInfo', views.ManageHallInfo, name="ManageHallInfo"),   
    path('ManageRoomInfo', views.ManageRoomInfo, name="ManageRoomInfo"),   
    path('ManageRoomDetail', views.ManageRoomDetail, name="ManageRoomDetail"),   
    path('room_with_details/<int:room_pk>/', views.room_with_details, name="room_with_details"),   
]  

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)