from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

admin.site.site_header = "Hall Management System Admin"
admin.site.site_title = "Hall Management System"
admin.site.index_title = "Well To Hall Management System"

urlpatterns = [  
    path('admin/', admin.site.urls),
    # path('', include('hmsapp.urls')),  
    # path('', include('accounts.urls')),
    path('', include('userprofile.urls')), 
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)