from django.contrib import admin

# Register your models here.
from portfolio.models import ContactForm, Blogs

admin.site.register(ContactForm)

admin.site.register(Blogs)