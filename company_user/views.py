from django.contrib import messages
from django.core.mail import message
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from company_user.models import User
from portfolio.models import Blogs, Event


def user_home(request):
    if 'user_name' in request.session:
        obj = Blogs.objects.all()
        return render(request, "user/index.html",{"data":obj})
    else:
        return render(request, "user/user-login.html")


def login(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        try:
            if User.objects.get(user_name=user_name, user_password=user_password) is not None:
                request.session['user_name'] = user_name
                obj = Blogs.objects.all().order_by('id')
                messages.success(request, "Login Successfully")
                return render(request, "user/index.html",{'data':obj})
        except:
            messages.error(request, "Invalid login details")
            return render(request, "user/user-login.html")

    return render(request, "user/index.html")


def user_login(request):
    return render(request, "user/user-login.html")


def user_about_us(request):
    if 'user_name' in request.session:
        return render(request, "user/user-about-us.html")
    else:
        return render(request, "user/user-login.html")


def user_our_team(request):
    if 'user_name' in request.session:
        return render(request, "user/user-our-team.html")
    else:
        return render(request, "user/user-login.html")


def user_career(request):
    if 'user_name' in request.session:
        return render(request, "user/user-career.html")
    else:
        return render(request, "user/user-login.html")


def user_service(request):
    if 'user_name' in request.session:
        return render(request, "user/user-service.html")
    else:
        return render(request, "user/user-login.html")


def user_blog(request):
    if 'user_name' in request.session:
        obj = Blogs.objects.all().order_by('-id')
        return render(request, "user/user-blog.html", {"obj": obj})
    else:
        return render(request, "user/user-login.html")


def user_contact(request):
    if 'user_name' in request.session:
        return render(request, "user/user-contact.html")
    else:
        return render(request, "user/user-login.html")


def user_event(request):
    if 'user_name' in request.session:
        obj = Event.objects.all().order_by('-id')
        return render(request, "user/user-event.html", {"obj": obj})
    else:
        return render(request, "user/user-login.html")


def user_profile(request):
    if 'user_name' in request.session:
        obj = User.objects.get(user_name=request.session['user_name'])
        return render(request, "user/user-profile.html", {"data": obj})
    else:
        return render(request, "user/user-login.html")


def user_my_event(request):
    if "user_name" in request.session:
        user_name = request.session['user_name']
        obj = Event.objects.filter(user_name=user_name).order_by('-id')
        return render(request, "user/user-my-event.html", {"obj": obj})
    else:
        return render(request, "user/user-login.html")


def user_my_blog(request):
    if "user_name" in request.session:
        user_name = request.session['user_name']
        obj = Blogs.objects.filter(user_name=user_name).order_by('-id')
        return render(request, "user/user-my-blog.html", {"obj": obj})
    else:
        return render(request, "user/user-login.html")


def user_logout(request):
    request.session.flush()
    messages.success(request,"Successfully Logout")
    return render(request, "user/user-login.html")


def update_profile(request, id):
    if 'user_name' in request.session:
        if request.method == "POST":
            obj = User.objects.get(id=id)
            obj.user_password = request.POST['user_password']
            obj.save()
            messages.success(request, " Profile Updated Successfully ")
            return redirect(user_profile)
        else:
            messages.error(request, "Somthing went wrong!")
    else:
        return render(request, "user/user-login.html")


def update_user_blog(request, id):
    if 'user_name' in request.session:
        if request.method == "POST":
            update = Blogs.objects.get(id=id)
            update.bolg_title = request.POST['blog_title']
            update.blog_title_tag = request.POST['blog_title_tag']
            update.blog_body = request.POST['blog_body']
            update.image=request.FILES['image']
            update.save()
            messages.success(request, "Successfully updated Blog")
            return redirect('user-profile')
        else:
            messages.error(request, "Somthing went wrong!")
        return render(request, "manager/user-home.html")
    else:
        return render(request, "manager/manager.html")


def delete_user_blog(request):
    try:
        if request.session['user_name'] is not None:
            if request.method == "POST":
                id = request.POST.get('id')
                obj = Blogs.objects.get(id=id)
                obj.delete()
                return JsonResponse({'status': 'delete'})
            else:
                return JsonResponse({"status": 'error'})
    except:
        return render(request, "user/index.html")


def delete_user_event(request):
    try:
        if request.session['user_name'] is not None:
            if request.method == "POST":
                id = request.POST.get('id')
                obj = Event.objects.get(id=id)
                obj.delete()
                return JsonResponse({'status': 'delete'})
            else:
                return JsonResponse({"status": 'error'})
    except:
        return render(request, "user/index.html")


def update_user_event(request, id):
    if 'user_name' in request.session:
        if request.method == "POST":
            update = Event.objects.get(id=id)
            update.event_name = request.POST['event_name']
            update.event_body = request.POST['event_body']
            update.event_cover_image = request.FILES['event_cover_image']
            update.save()
            messages.success(request, "Successfully updated Blog")
            return redirect('user-profile')
        else:
            messages.error(request, "Somthing went wrong!")
        return render(request, "manager/user-home.html")
    else:
        return render(request, "user/index.html")


def email_otp(request, id):
    obj = User.objects.get(id=id)
    return render(request, "user/email-otp.html", {"data": obj})


def user_add_blog(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        return render(request, "user/user-add-blog.html", {"data": user_name})
    else:
        return render(request, "user/user-login.html")


def post_blog_user(request):
    if 'user_name' in request.session:
        if request.method == "POST":
            blog_title = request.POST['blog_title']
            blog_tag = request.POST['blog_tag']
            blog_body = request.POST['blog_body']
            image = request.FILES['image']
            user_name = request.POST['user_name']

            obj = Blogs(bolg_title=blog_title, blog_title_tag=blog_tag, blog_body=blog_body, image=image,
                        user_name=user_name)
            obj.save()
            messages.success(request, "Successfully Posted Blog")
            return redirect('user-profile')
        else:
            messages.error(request, "Somthing went wrong!")
        return render(request, "user/user-login.html")
    else:
        return render(request, "user/user-login.html")


def user_add_event(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        return render(request, "user/user-add-event.html", {"data": user_name})
    else:
        return render(request, "user/user-login.html")


def post_event_user(request):
    if 'user_name' in request.session:
        if request.session['user_name'] is not None:
            if request.method == "POST":
                event_name = request.POST['event_name']
                event_date = request.POST['event_date']
                event_body = request.POST['event_body']
                event_cover_image = request.FILES['event_cover_image']
                user_name=request.POST['user_name']

                obj = Event(event_name=event_name, event_date=event_date, event_body=event_body,
                            event_cover_image=event_cover_image,user_name=user_name)
                obj.save()
                messages.success(request, "Successfully Posted Event")
                return redirect('user-profile')
            else:
                messages.error(request, "Somthing went wrong!")
            return render(request, "user/index.html")
        else:
            return render(request, "user/index.html")
    else:
        return render(request, "user/user-login.html")

