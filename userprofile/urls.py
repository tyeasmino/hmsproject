from django.contrib import admin
from django.urls import path, include  
from userprofile import views

urlpatterns = [
    path('', views.index, name="home"),
    path('signin', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),    
]  

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)