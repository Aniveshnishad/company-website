from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from portfolio.models import ContactForm, Blogs, Manager, JobPostDetail, ApplyDetails


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


def careers_page(request):
    return render(request, "careers.html")


def graduate_page(request):
    obj = JobPostDetail.objects.filter(job_education__icontains="Graduate").order_by('-id')
    paginator = Paginator(obj, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "graduate.html", {"data": page_obj})


def experience_page(request):
    obj = JobPostDetail.objects.filter(job_education__icontains="Experience").order_by('-id')
    paginator = Paginator(obj, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "experience.html", {"data": page_obj})


def intern_page(request):
    obj = JobPostDetail.objects.filter(job_education__icontains="Intern").order_by('-id')
    paginator = Paginator(obj, 3)
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
        obj = ContactForm(name=name, email=email, number=number, subject=subject, message=message)
        messages.success(request, 'Hey! you submitted Successfully')
        obj.save()
    else:
        pass

    return render(request, "contact.html")


# for admin views

def manager(request):
    return render(request, "manager/manager.html")


def manager_login(request):
    if request.method == "POST":
        manager_name = request.POST['manager_name']
        manager_password = request.POST['manager_password']
        try:
            if Manager.objects.get(manager_name=manager_name, manager_password=manager_password) is not None:
                request.session['manager_name'] = manager_name
                messages.success(request, "Login Successful")
                return render(request, "manager/manager-home.html")
        except:
            messages.error(request, "Invalid login details")
        return render(request, "manager/manager.html")

    return render(request, "manager/manager.html")


def apply_form(request, id):
    obj = JobPostDetail.objects.get(id=id)
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
        obj = ApplyDetails(name=name, email=email, number=number, subject=subject, city=city, cover_leter=cover_leter,
                           file_cv=file_cv)
        obj.save()
        messages.success(request, "Submitted Successfully")
        return render(request, "index.html")
    else:
        messages.error(request, "Somthing went Wrong!")
        return render(request, "index.html")
