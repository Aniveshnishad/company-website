import ckeditor.fields
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name=models.CharField(max_length=200,blank=True)
    email=models.EmailField(max_length=200,blank=True)
    number=models.CharField(max_length=11,blank=True)
    subject=models.CharField(max_length=200,blank=True)
    message=models.CharField(max_length=900,blank=True)
    reply=models.TextField(max_length=2000,blank=True)
    def __str__(self):
        return self.email

class Blogs(models.Model):
    bolg_title=models.CharField(max_length=1000,blank=True)
    blog_title_tag=models.CharField(max_length=900,blank=True)
    blog_body= RichTextField(blank=True,null=True)
    image=models.ImageField(upload_to='static/blog-images',blank=True)
    date=models.DateField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.bolg_title


class JobPostDetail(models.Model):
    choose=(('Graduate','Graduate'),('Internship','Internship'),('Experience/Professional','Experience/Professional'))
    job_education=models.CharField(max_length=300,choices=choose,blank=True)
    job_title=models.CharField(max_length=200,blank=True)
    start_date=models.DateField(default='dd/mm/yy',blank=True)
    last_date = models.DateField(default='dd/mm/yy',blank=True)
    country=models.CharField(max_length=200,blank=True)
    state=models.CharField(max_length=200,blank=True)
    work_location=models.CharField(max_length=900,blank=True)
    company_name=models.CharField(max_length=900,blank=True)
    job_description=models.TextField(max_length=2000,blank=True)
    roles_responsibility=models.TextField(max_length=2000,blank=True)
    essential_skill=models.TextField(max_length=2000,blank=True)
    preffered_skill=models.TextField(max_length=2000,blank=True)
    additional_skill=models.TextField(max_length=2000,blank=True)
    image=models.ImageField(blank=True)
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