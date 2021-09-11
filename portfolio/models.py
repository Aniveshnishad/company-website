import ckeditor.fields
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name=models.CharField(max_length=200,blank=True)
    email=models.EmailField(max_length=200,blank=True)
    number=models.CharField(max_length=11,blank=True)
    subject=models.CharField(max_length=200,blank=True)
    message=models.CharField(max_length=900,blank=True)
    email_subject=models.CharField(max_length=200,blank=True)
    reply=models.TextField(max_length=2000,blank=True)
    def __str__(self):
        return self.email

class Blogs(models.Model):
    bolg_title=models.CharField(max_length=1000,blank=True)
    blog_title_tag=models.CharField(max_length=900,blank=True)
    blog_body= RichTextUploadingField(blank=True,null=True)
    image=models.ImageField(upload_to='static/blog-images/',blank=True)
    date=models.DateField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.bolg_title


class JobPostDetail(models.Model):
    choose=(('Graduate','Graduate'),('Internship','Internship'),('Experience/Professional','Experience/Professional'))
    job_education=models.CharField(max_length=300,choices=choose,blank=True)
    job_title=models.CharField(max_length=200,blank=True)
    job_description=RichTextUploadingField(max_length=2000,blank=True)
    def __str__(self):
        return self.job_title

class ApplyDetails(models.Model):

    name = models.CharField(max_length=200, blank=True)
    number = models.CharField(max_length=200, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    cover_leter = models.TextField(max_length=200, blank=True)
    file_cv=models.FileField(upload_to='static/cover-leters',blank=True)
    reply=models.TextField(max_length=2000,blank=True)
    def __str__(self):
        return self.email

class Event(models.Model):
    event_name=models.CharField(max_length=2000,blank=True)
    event_date=models.DateField(auto_now_add=True,blank=True)
    event_cover_image=models.ImageField(upload_to='static/event-cover-image/',blank=True)
    event_body=RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.event_name