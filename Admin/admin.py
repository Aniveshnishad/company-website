from django.contrib import admin

# Register your models here.
from Admin.models import Manager


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_name','manager_password')


admin.site.register(Manager,ManagerAdmin)