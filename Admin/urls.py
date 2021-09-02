from django.contrib import admin
from django.urls import path

from Admin import views

urlpatterns = [
    path('manager/d033e22ae348aeb5660fc2140aec35850c4da997/', views.manager, name="manager"),
    path('manager-login', views.manager_login, name="manager-login"),
]