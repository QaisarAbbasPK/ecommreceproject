
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings




admin.site.site_header = 'Grocery Shop'       # default: "Django Administration"
admin.site.index_title = 'Grocery Shop'       # default: "Site administration"
admin.site.site_title = 'Grocery Shop'        # default: "Django site admin"






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
