from django.contrib import admin
from django.urls import path

from Admin import views

urlpatterns = [
    path('manager/d033e22ae348aeb5660fc2140aec35850c4da997/', views.manager, name="manager"),
    path('manager-login', views.manager_login, name="manager-login"),
    path('manager-home', views.manager_home, name="manager-home"),
    path('manager-add-blogs', views.add_blogs, name="manager-add-blogs"),
    path('manager-add-job', views.add_job, name="manager-add-job"),
    path('manager-candidates', views.candidates, name="manager-candidates"),
    path('manager-contacts', views.contacts, name="manager-contacts"),
    path('manager-profile', views.profile, name="manager-profile"),
    path('reply-contact/<id>', views.reply_contact, name="reply-contact"),
    path('reply-contact-form/<id>', views.reply_contact_form, name="reply-contact-form"),
    path('reply-candidate-form/<id>', views.reply_candidate_form, name="reply-candidate-form"),
    path('post-job-form', views.post_job_form, name="post-job-form"),
    path('delete-blog/<id>', views.delete_blog, name="delete-blog"),
    path('update-job-form/<id>', views.update_job_form, name="update-job-form"),
    path('post-job', views.post_job, name="post-job"),
    path('delete-add-job/<id>',views.delete_add_job,name='delete-add-job'),
    path('add-blog-form', views.add_blog_form, name="add-blog-form"),
    path('post-blog-form', views.post_blog_form, name="post-blog-form"),
]