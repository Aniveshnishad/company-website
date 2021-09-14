from django.contrib import admin

# Register your models here.
from company_user.models import User

admin.site.register(User)