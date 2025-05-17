
from django.contrib import admin
from django.urls import path, include
from django.conf import settings, static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),


