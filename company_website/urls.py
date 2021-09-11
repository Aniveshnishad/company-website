from django.contrib import admin
from django.urls import path, include
from js_asset import static
from django.conf.urls.static import static

import portfolio
from company_website import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('portfolio.urls')),
                  path('', include('Admin.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
              ]
