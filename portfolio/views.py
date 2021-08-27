from django.contrib import messages
from django.shortcuts import render


# Create your views here.
from portfolio.models import ContactForm


def index_page(request):
    return render(request, "index.html")


def index_page(request):
    return render(request, "index.html")


def blog_page(request):

    return render(request, "blog.html")


def test_page(request):
    return render(request, "test.html")


def about_page(request):
    return render(request, "about_us.html")


def service_page(request):
    return render(request, "services.html")


def our_team(request):
    return render(request, "our_team.html")


def contact_page(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number= request.POST['number']
        subject=request.POST['subject']
        message=request.POST['message']
        obj=ContactForm(name=name,email=email,number=number,subject=subject,message=message)
        messages.success(request, 'Hey! you submitted Successfully')
        obj.save()
    else:
        pass

    return render(request, "contact.html")
