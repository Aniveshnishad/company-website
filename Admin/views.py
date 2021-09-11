import email

from django.core.mail import EmailMessage, send_mail
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
# from portfolio.models import
from django.template.loader import get_template

from Admin.models import Manager
from company_website import settings
from portfolio.models import ContactForm, ApplyDetails, JobPostDetail, Blogs, Event


def manager(request):
    try:
        if request.session['manager_name'] is not None:
            return render(request, "manager/manager.html")
    except:
        return render(request, "manager/manager.html")


def manager_home(request):
    try:
        if request.session['manager_name'] is not None:
            return render(request, "manager/manager-home.html")
    except:
        return render(request, "manager/manager.html")


def contacts(request):
    try:
        if request.session['manager_name'] is not None:
            obj = ContactForm.objects.all().order_by('-id')
            paginator = Paginator(obj, 20)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            obj1 = ContactForm.objects.filter(reply='').order_by('-id')

            obj2 = ContactForm.objects.filter(reply__gte=0).order_by('-id')

            return render(request, "manager/contacts.html", {'data': page_obj, 'data1': obj1, 'data2': obj2})
    except:
        return render(request, "manager/manager.html")


def add_blogs(request):
    try:
        if request.session['manager_name'] is not None:
            obj = Blogs.objects.all().order_by('id')
            paginator = Paginator(obj, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, "manager/add-blogs.html", {"data": page_obj})
    except:
        return render(request, "manager/manager.html")


def add_event(request):
    try:
        if request.session['manager_name'] is not None:
            obj = Event.objects.all().order_by('id')
            paginator = Paginator(obj, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, "manager/add-event.html", {"data": page_obj})
    except:
        return render(request, "manager/manager.html")


def add_job(request):
    try:
        if request.session['manager_name'] is not None:
            obj = JobPostDetail.objects.all().order_by('-id')
            paginator = Paginator(obj, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, "manager/add-job.html", {"data": page_obj})
    except:
        return render(request, "manager/manager.html")


def post_job(request):
    try:
        if request.session['manager_name'] is not None:
            return render(request, "manager/post-job.html")
    except:
        return render(request, "manager/manager.html")


def candidates(request):
    try:
        if request.session['manager_name']:
            if 'search' in request.GET:
                search = request.GET['search']
                obj = ApplyDetails.objects.filter(
                    Q(name__istartswith=search) | Q(number__istartswith=search) | Q(
                        email__istartswith=search)).order_by('-id')
                paginator = Paginator(obj, 20)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request, "manager/candidates.html", {"data": page_obj})
            else:
                obj = ApplyDetails.objects.all().order_by('-id')
                paginator = Paginator(obj, 20)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request, "manager/candidates.html", {"data": page_obj})
    except:
        return render(request, "manager/manager.html")


def search(request):
    if request.method == "POST":
        search = request.POST['search']
        obj = ApplyDetails.objects.filter(
            Q(name__istartswith=search) | Q(number__istartswith=search) | Q(email__istartswith=search))
        paginator = Paginator(obj, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "manager/search.html", {"data": page_obj})


def profile(request):
    try:
        if request.session['manager_name'] is not None:
            manager_name = request.session['manager_name']
            obj = Manager.objects.get(manager_name=manager_name)
            return render(request, "manager/profile.html", {"data": obj})
    except:
        return render(request, "manager/manager.html")


def reply_contact(request, id):
    try:
        if request.session['manager_name'] is not None:
            obj = ContactForm.objects.get(id=id)
            return render(request, "manager/reply.html", {"data": obj})
    except:
        return render(request, "manager/manager.html")


def reply_contact_form(request, id):
    if "manager_name" in request.session:
        if request.method == "POST":
            obj = ContactForm.objects.get(id=id)
            name = obj.name
            email = obj.email

            obj.email_subject = request.POST['email_subject']
            obj.reply = request.POST['reply']
            subject = request.POST['email_subject']

            ctx = {
                'name': name,
                'email': email,
                'reply': request.POST['reply']

            }
            message = get_template('manager/email-tamplate.html').render(ctx)
            msg = EmailMessage(
                subject,
                message,
                "CubexO Software Solution LLP",
                [email],

            )
            msg.content_subtype = "html"
            msg.send()
            obj.save()
            messages.success(request, "Successfully Replied")
            return redirect('manager-contacts')
        else:
            messages.error(request, "Somthing went wrong!")
        return render(request, "manager/manager-home.html")
    else:
        return render(request, "manager/manager.html")


def reply_candidate_form(request, id):
    if request.session['manager_name'] is not None:
        if request.method == "POST":
            obj = ApplyDetails.objects.get(id=id)
            name = obj.name
            email = obj.email
            obj.reply = request.POST['reply']
            obj.email_subject = request.POST['email_subject']
            subject = request.POST['email_subject']
            ctx = {
                'name': name,
                'email': email,
                'reply': request.POST['reply']

            }
            message = get_template('manager/email-tamplate.html').render(ctx)
            msg = EmailMessage(
                subject,
                message,
                "CubexO Software Solution LLP",
                [email],

            )
            msg.content_subtype = "html"
            msg.send()

            obj.save()
            messages.success(request, "Successfully Replied")
            return redirect('manager-candidates')
        else:
            messages.error(request, "Somthing went wrong!")
        return render(request, "manager/manager-home.html")
    else:
        return render(request, "manager/manager.html")


def post_job_form(request):
    try:
        if request.session['manager_name'] is not None:
            if request.method == "POST":
                job_education = request.POST['job_education']
                job_title = request.POST['job_title']
                job_description = request.POST['job_description']
                obj = JobPostDetail(job_education=job_education, job_title=job_title,
                                    job_description=job_description)
                obj.save()
                messages.success(request, "Successfully Posted Job")
                return redirect('manager-add-job')
            else:
                messages.error(request, "Somthing went wrong!")
            return render(request, "manager/manager-home.html")
    except:
        return render(request, "manager/manager.html")


def update_job_form(request, id):
    try:
        if request.session['manager_name'] is not None:
            if request.method == "POST":
                update = JobPostDetail.objects.get(id=id)
                update.job_title = request.POST['job_title']
                update.job_description = request.POST['job_description']
                update.save()
                messages.success(request, "Successfully updated Job")
                return redirect('manager-add-job')
            else:
                messages.error(request, "Somthing went wrong!")
            return render(request, "manager/manager-home.html")
    except:
        return render(request, "manager/manager.html")


def modal(request):
    try:
        if request.session['manager_name'] is not None:
            return render(request, "manager/modal.html")
    except:
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


def manager_logout(request):
    request.session.flush()
    return render(request, "manager/manager.html")


def delete_job(request):
    try:
        if request.session['manager_name'] is not None:
            if request.method == "POST":
                id = request.POST.get('id')
                obj = JobPostDetail.objects.get(id=id)
                obj.delete()
                return JsonResponse({'status': 'delete'})
            else:
                return JsonResponse({"status": 'error'})
    except:
        return render(request, "manager/manager.html")


def delete_blog(request):
    try:
        if request.session['manager_name'] is not None:
            if request.method == "POST":
                id = request.POST.get('id')
                obj = Blogs.objects.get(id=id)
                obj.delete()
                return JsonResponse({'status': 'delete'})
            else:
                return JsonResponse({"status": 'error'})
    except:
        return render(request, "manager/manager.html")


def delete_event(request):
    try:
        if request.session['manager_name'] is not None:
            if request.method == "POST":
                id = request.POST.get('id')
                obj = Event.objects.get(id=id)
                obj.delete()
                return JsonResponse({'status': 'delete'})
            else:
                return JsonResponse({"status": 'error'})
    except:
        return render(request, "manager/manager.html")


def add_blog_form(request):
    try:
        if request.session['manager_name'] is not None:
            return render(request, "manager/add-blog-form.html")
    except:
        return render(request, "manager/manager.html")


def add_event_form(request):
    try:
        if request.session['manager_name'] is not None:
            return render(request, "manager/add-event-form.html")
    except:
        return render(request, "manager/manager.html")


def post_blog_form(request):
    try:
        if request.session['manager_name'] is not None:
            if request.method == "POST":
                blog_title = request.POST['blog_title']
                blog_tag = request.POST['blog_tag']
                blog_body = request.POST['blog_body']
                image = request.FILES['image']

                obj = Blogs(bolg_title=blog_title, blog_title_tag=blog_tag, blog_body=blog_body, image=image)
                obj.save()
                messages.success(request, "Successfully Posted Blog")
                return redirect('manager-add-blogs')
            else:
                messages.error(request, "Somthing went wrong!")
            return render(request, "manager/manager-home.html")
    except:
        return render(request, "manager/manager.html")


def post_event_form(request):
    try:
        if request.session['manager_name'] is not None:
            if request.method == "POST":
                event_name = request.POST['event_name']
                event_date = request.POST['event_date']
                event_body = request.POST['event_body']
                event_cover_image = request.FILES['event_cover_image']

                obj = Event(event_name=event_name, event_date=event_date, event_body=event_body,
                            event_cover_image=event_cover_image)
                obj.save()
                messages.success(request, "Successfully Posted Blog")
                return redirect('manager-add-event')
            else:
                messages.error(request, "Somthing went wrong!")
            return render(request, "manager/manager-home.html")
    except:
        return render(request, "manager/manager.html")


def update_blog_form(request, id):
    try:
        if request.session['manager_name'] is not None:
            if request.method == "POST":
                update = Blogs.objects.get(id=id)
                update.bolg_title = request.POST['blog_title']
                update.blog_title_tag = request.POST['blog_title_tag']
                update.blog_body = request.POST['blog_body']
                update.image = request.FILES['image']
                update.save()
                messages.success(request, "Successfully updated blog")
                return redirect('manager-add-blogs')
            else:
                messages.error(request, "Somthing went wrong!")
            return render(request, "manager/manager-home.html")
    except:
        return render(request, "manager/manager.html")


def update_event_form(request, id):
    if 'manager_name' in request.session:
        if request.method == "POST":
            update = Event.objects.get(id=id)
            update.event_name = request.POST['event_name']
            update.event_date = request.POST['event_date']
            update.event_body = request.POST['event_body']
            update.event_cover_image = request.FILES['event_cover_image']
            update.save()
            messages.success(request, "Successfully updated Event")
            return redirect('manager-add-event')
        else:
            messages.error(request, "Somthing went wrong!")
        return render(request, "manager/manager-home.html")
    else:
        return render(request, "manager/manager.html")


def test(request):
    if request.method == "POST":
        search = request.POST['search']
        obj = ApplyDetails.objects.filter(
            Q(name__istartswith=search) | Q(number__istartswith=search) | Q(email__istartswith=search))

    return render(request, "test_page.html", {"data": obj})
