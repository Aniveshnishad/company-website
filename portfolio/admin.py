from django.contrib import admin

# Register your models here.
from portfolio.models import ContactForm, Blogs, JobPostDetail, ApplyDetails, Event

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','number', 'subject','message')
    search_fields = ('name', 'email','number')
    list_per_page = 10
    list_filter = ('name',)
    ordering = ('-id',)



class BlogsAdmin(admin.ModelAdmin):
    list_display = ('bolg_title','blog_title_tag','image','date')
    list_per_page = 10
    list_filter = ('bolg_title',)
    ordering = ('date',)

class JobPostDetailAdmin(admin.ModelAdmin):
    list_display = ('job_education','job_title', )
    list_per_page = 10
    list_filter = ('job_title',)


class ApplyDetailsAdmin(admin.ModelAdmin):
    list_display = ('name','number','subject','email','cover_leter','file_cv')
    list_per_page = 10
    list_filter = ('name',)
    ordering = ('-id',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name','event_cover_image','event_date')
    list_per_page = 10
    list_filter = ('event_name',)





admin.site.register(ContactForm,ContactFormAdmin)
admin.site.register(Blogs,BlogsAdmin)
admin.site.register(JobPostDetail,JobPostDetailAdmin)
admin.site.register(ApplyDetails,ApplyDetailsAdmin)
admin.site.register(Event,EventAdmin)