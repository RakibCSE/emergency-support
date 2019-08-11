from django.contrib import admin
from django.urls import path, include

import service

urlpatterns = [
    path('', include('service.urls')),
    path('admin/', admin.site.urls),
]
