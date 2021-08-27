from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from portfolio.models import ContactForm, Blogs


def index_page(request):
    return render(request, "index.html")


def index_page(request):
    return render(request, "index.html")


def blog_page(request):
    obj = Blogs.objects.all()
    return render(request, "blog.html", {"obj": obj})


def full_blog(request, id):
    obj = Blogs.objects.get(id=id)
    return render(request, "full_blog.html", {"obj": obj})


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
        number = request.POST['number']
        subject = request.POST['subject']
        message = request.POST['message']
        obj = ContactForm(name=name, email=email, number=number, subject=subject, message=message)
        messages.success(request, 'Hey! you submitted Successfully')
        obj.save()
    else:
        pass

    return render(request, "contact.html")

# for admin views

def manager(request):

    return render(request, "manager/manager.html")