"""online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from portfolio import views

urlpatterns = [
    # urls for web templates
    path('',views.index_page,name="index"),
    path('home',views.index_page,name="home"),
    path('blog',views.blog_page,name="blog"),
    path('blog-full/<id>',views.full_blog,name="full-blog"),
    path('test',views.test_page,name="test"),
    path('about-us',views.about_page,name="about"),
    path('service',views.service_page,name="service"),
    path('our-team', views.our_team, name="our-team"),
    path('contact',views.contact_page,name="contact"),
    path('careers',views.careers_page,name="careers"),
    path('careers/graduate',views.graduate_page,name="graduate"),
    path('careers/experience',views.experience_page,name="experience"),
    path('carrers/intern',views.intern_page,name="intern"),

    # urls for admin actions
    path('manager',views.manager,name="manager"),
    path('manager-login',views.manager_login,name="manager-login"),
]
