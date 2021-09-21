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
from django.views.decorators.cache import cache_page

from portfolio import views

urlpatterns = [
    # urls for web templates
    path('', views.index_page, name="index"),
    path('home', views.index_page, name="home"),
    path('blog', views.blog_page, name="blog"),
    path('events', views.events_page, name="events"),
    path('blog-full/<id>', views.full_blog, name="full-blog"),
    path('blog-event/<id>', views.full_event, name="full-event"),
    path('about-us', views.about_page, name="about"),
    path('service', views.service_page, name="service"),
    path('our-team', views.our_team, name="our-team"),
    path('contact', views.contact_page, name="contact"),
    path('careers', views.careers_page, name="careers"),
    path('careers/graduate', views.graduate_page, name="graduate"),
    path('careers/experience', views.experience_page, name="experience"),
    path('careers/intern', views.intern_page, name="intern"),
    path('careers/apply-form/<id>', views.apply_form, name="apply-form"),
    path('submit-form', views.submit_form, name="submit-form"),
    path('test_page', views.test_page, name="test_page"),
    # path(r'^$', cache_page(60 * 60)(views.index_page), name="index"),

    # urls for admin actions

]
