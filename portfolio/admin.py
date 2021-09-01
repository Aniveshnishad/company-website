from django.contrib import admin

# Register your models here.
from portfolio.models import ContactForm, Blogs, Manager, JobPostDetail, ApplyDetails

admin.site.register(ContactForm)
admin.site.register(Manager)
admin.site.register(Blogs)
admin.site.register(JobPostDetail)
admin.site.register(ApplyDetails)
