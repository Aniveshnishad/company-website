from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
# from portfolio.models import
from Admin.models import Manager
from portfolio.models import ContactForm, ApplyDetails, JobPostDetail, Blogs


def manager(request):
    return render(request, "manager/manager.html")


def manager_home(request):
    return render(request, "manager/manager-home.html")


def contacts(request):
    obj = ContactForm.objects.all()

    return render(request, "manager/contacts.html", {'data': obj})


def add_blogs(request):
    obj = Blogs.objects.all().order_by('id')
    return render(request, "manager/add-blogs.html", {"data": obj})


def add_job(request):
    obj = JobPostDetail.objects.all().order_by('-id')
    return render(request, "manager/add-job.html", {"data": obj})


def post_job(request):
    return render(request, "manager/post-job.html")


def candidates(request):
    obj = ApplyDetails.objects.all().order_by('-id')
    return render(request, "manager/candidates.html", {"data": obj})


def profile(request):
    manager_name = request.session['manager_name']
    obj = Manager.objects.get(manager_name=manager_name)
    return render(request, "manager/profile.html", {"data": obj})


def reply_contact(request, id):
    obj = ContactForm.objects.get(id=id)

    return render(request, "manager/reply.html", {"data": obj})


def reply_contact_form(request, id):
    if request.method == "POST":
        obj = ContactForm.objects.get(id=id)
        obj.reply = request.POST['reply']
        obj.save()
        messages.success(request, "Successfully Replied")
        return redirect('manager-contacts')
    else:
        messages.error(request, "Somthing went wrong!")
    return render(request, "manager/manager-home.html")


def reply_candidate_form(request, id):
    if request.method == "POST":
        obj = ApplyDetails.objects.get(id=id)
        obj.reply = request.POST['reply']
        obj.save()
        messages.success(request, "Successfully Replied")
        return redirect('manager-candidates')
    else:
        messages.error(request, "Somthing went wrong!")
    return render(request, "manager/manager-home.html")


def post_job_form(request):
    if request.method == "POST":
        job_education = request.POST['job_education']
        job_title = request.POST['job_title']
        state = request.POST['state']
        country = request.POST['country']
        work_location = request.POST['work_location']
        job_description = request.POST['job_description']
        start_date = request.POST['start_date']
        last_date = request.POST['last_date']
        obj = JobPostDetail(job_education=job_education, job_title=job_title, state=state, country=country,
                            work_location=work_location, job_description=job_description, start_date=start_date,
                            last_date=last_date, )
        obj.save()
        messages.success(request, "Successfully Posted Job")
        return redirect('manager-add-job')
    else:
        messages.error(request, "Somthing went wrong!")
    return render(request, "manager/manager-home.html")


def update_job_form(request, id):
    if request.method == "POST":
        update = JobPostDetail.objects.get(id=id)
        update.job_title = request.POST['job_title']
        update.state = request.POST['state']
        update.work_location = request.POST['work_location']
        update.job_description = request.POST['job_description']
        update.start_date = request.POST['start_date']
        update.last_date = request.POST['last_date']
        update.save()
        messages.success(request, "Successfully updated Job")
        return redirect('manager-add-job')
    else:
        messages.error(request, "Somthing went wrong!")
    return render(request, "manager/manager-home.html")


def modal(request):
    return render(request, "manager/modal.html")


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


def delete_add_job(request, id):
    obj = JobPostDetail.objects.get(id=id)
    obj.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('manager-add-job')


def delete_blog(request, id):
    obj = Blogs.objects.get(id=id)
    obj.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('manager-add-blogs')


def add_blog_form(request):
   return render(request,"manager/add-blog-form.html")



def post_blog_form(request):
    if request.method == "POST":
        blog_title = request.POST['blog_title']
        blog_tag = request.POST['blog_tag']
        blog_body = request.POST['blog_body']
        image = request.FILES['image']

        obj = Blogs(bolg_title=blog_title,blog_title_tag=blog_tag,blog_body=blog_body,image=image)
        obj.save()
        messages.success(request, "Successfully Posted Blog")
        return redirect('manager-add-blogs')
    else:
        messages.error(request, "Somthing went wrong!")
    return render(request, "manager/manager-home.html")



