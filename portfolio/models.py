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
