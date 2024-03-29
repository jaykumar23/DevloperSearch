
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),
    
]

# used static to grab media-url and plug to media root
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
