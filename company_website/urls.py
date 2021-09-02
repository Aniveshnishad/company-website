from django.contrib import admin
from django.urls import path, include
import portfolio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('', include('Admin.urls')),
]
