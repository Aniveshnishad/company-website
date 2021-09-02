from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
# from portfolio.models import
from Admin.models import Manager


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

