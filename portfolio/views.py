import json
import urllib
from urllib import response

import requests
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render




# Create your views here.
from company_website import settings
from portfolio.models import ContactForm, Blogs, JobPostDetail, ApplyDetails, Event


def test_page(request):
    return render(request,"test_page.html")
def index_page(request):
    obj = Blogs.objects.all().order_by('-id')
    return render(request, "index.html", {"data": obj, "index": "data"})


def blog_page(request):
    obj = Blogs.objects.all()
    return render(request, "blog.html", {"obj": obj, "blog": "data"})


def full_blog(request, id):
    obj = Blogs.objects.get(id=id)
    return render(request, "full_blog.html", {"obj": obj})


def about_page(request):
    return render(request, "about_us.html", {"isPage": "data"})


def service_page(request):
    return render(request, "services.html", {"service": "data"})


def our_team(request):
    return render(request, "our_team.html", {"out_team": "data"})


def careers_page(request):
    return render(request, "careers.html", {"career": "data"})


def graduate_page(request):
    obj = JobPostDetail.objects.filter(job_education__icontains="Graduate").order_by('-id')
    paginator = Paginator(obj, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "graduate.html", {"data": page_obj})


def experience_page(request):
    obj = JobPostDetail.objects.filter(job_education__icontains="Experience").order_by('-id')
    paginator = Paginator(obj, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "experience.html", {"data": page_obj})


def intern_page(request):
    obj = JobPostDetail.objects.filter(job_education__icontains="Intern").order_by('-id')
    paginator = Paginator(obj, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "intern.html", {"data": page_obj})


def contact_page(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        subject = request.POST['subject']
        message = request.POST['message']
        captcha_rs = request.POST.get('g-recaptcha-response')
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': captcha_rs,

        }
        data = urllib.parse.urlencode(params).encode("utf-8")
        response = urllib.request.urlopen(url, data)

        result = json.load(response)
        ''' End reCAPTCHA validation '''

        if result['success']:
            obj = ContactForm(name=name, email=email, number=number, subject=subject, message=message)
            messages.success(request, 'Hey! you submitted Successfully')
            obj.save()
            return render(request, "contact.html")
        else:
            messages.error(request,"Invalid Recaptcha")
            return render(request, "contact.html")
    else:
        pass

    return render(request, "contact.html", {"contact": "data"})


# for admin views

def apply_form(request, slug):
    obj = JobPostDetail.objects.get(slug=slug)
    return render(request, "apply-form.html", {"data": obj})


def submit_form(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        subject = request.POST['subject']
        city = request.POST['city']
        cover_leter = request.POST['cover_leter']
        file_cv = request.FILES['file_cv']
        captcha_rs = request.POST.get('g-recaptcha-response')
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': captcha_rs,

        }
        data = urllib.parse.urlencode(params).encode("utf-8")
        response = urllib.request.urlopen(url, data)

        result = json.load(response)
        ''' End reCAPTCHA validation '''
        if result['success']:
            obj = ApplyDetails.objects.create(name=name, email=email, number=number, subject=subject, city=city,
                               cover_leter=cover_leter,
                               file_cv=file_cv)

            obj.save()

            messages.success(request, "Submitted Successfully")
            return render(request, "careers.html")
        else:
            messages.error(request,"Invalid Recaptcha")
            return render(request, "careers.html")
    else:
        messages.error(request, "Somthing went Wrong!")
    return render(request, "careers.html")


def events_page(request):
    obj = Event.objects.all()
    return render(request, "events.html", {"obj": obj, "event": "data"})


def full_event(request, id):
    obj = Event.objects.get(id=id)
    return render(request, "full-event.html", {"obj": obj})
