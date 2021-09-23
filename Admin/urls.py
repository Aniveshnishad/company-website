from django.contrib import admin
from django.urls import path

from Admin import views

urlpatterns = [
    path('manager/d033e22ae348aeb5660fc2140aec35850c4da997/', views.manager, name="manager"),
    path('manager-login', views.manager_login, name="manager-login"),
    path('manager-home', views.manager_home, name="manager-home"),
    path('manager-service', views.manager_service, name="manager-service"),
    path('manager-about-us', views.manager_about_us, name="manager-about-us"),
    path('manager-add-blogs', views.add_blogs, name="manager-add-blogs"),
    path('manager-add-event', views.add_event, name="manager-add-event"),
    path('manager-add-job', views.add_job, name="manager-add-job"),
    path('manager-candidates', views.candidates, name="manager-candidates"),
    path('manager-contacts', views.contacts, name="manager-contacts"),
    path('manager-profile', views.profile, name="manager-profile"),
    path('reply-contact/<id>', views.reply_contact, name="reply-contact"),
    path('reply-contact-form/<id>', views.reply_contact_form, name="reply-contact-form"),
    path('reply-candidate-form/<id>', views.reply_candidate_form, name="reply-candidate-form"),
    path('post-job-form', views.post_job_form, name="post-job-form"),
    path('delete-blog', views.delete_blog, name="delete-blog"),
    path('delete-added-user', views.delete_added_user, name="delete-added-user"),
    path('delete-event', views.delete_event, name="delete-event"),
    path('update-job-form/<id>', views.update_job_form, name="update-job-form"),
    path('update-blog-form/<id>', views.update_blog_form, name="update-blog-form"),
    path('update-event-form/<id>', views.update_event_form, name="update-event-form"),
    path('post-job', views.post_job, name="post-job"),
    path('add-user', views.add_user, name="add-user"),
    path('delete-add-job', views.delete_job, name='delete-add-job'),
    path('add-blog-form', views.add_blog_form, name="add-blog-form"),
    path('add-event-form', views.add_event_form, name="add-event-form"),
    path('manager-logout', views.manager_logout, name="manager-logout"),
    path('post-blog-form', views.post_blog_form, name="post-blog-form"),
    path('add-user-data', views.add_user_data, name="add-user-data"),
    path('post-event-form', views.post_event_form, name="post-event-form"),

    path('test-page', views.test, name="test-page"),
]
