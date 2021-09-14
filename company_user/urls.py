from django.urls import path

from company_user import views

urlpatterns = [
    # urls for web templates
    path('user', views.user_login),
    path('user-login', views.login, name="user-login"),
    path('user-home', views.user_home, name="user-home"),
    path('user-blog', views.user_blog, name="user-blog"),
    path('user-events', views.user_event, name="user-events"),
    # path('blog-full/<id>', views.full_blog, name="full-blog"),
    # path('blog-event/<id>', views.full_event, name="full-event"),
    path('post-blog-user', views.post_blog_user, name="post-blog-user"),
    path('user-about-us', views.user_about_us, name="user-about"),
    path('user-service', views.user_service, name="user-service"),
    path('user-our-team', views.user_our_team, name="user-our-team"),
    path('user-contact', views.user_contact, name="user-contact"),
    path('user-careers', views.user_career, name="user-careers"),
    path('user-profile', views.user_profile, name="user-profile"),
    path('update-profile/<id>', views.update_profile, name="update-profile"),
    path('user-my-blog', views.user_my_blog, name="user-my-blog"),
    path('user-my-event', views.user_my_event, name="user-my-event"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('delete-user-blog', views.delete_user_blog, name="delete-user-blog"),
    path('update-user-blog/<id>', views.update_user_blog, name="update-user-blog"),
    path('delete-user-event', views.delete_user_event, name="delete-user-event"),
    path('update-user-event/<id>', views.update_user_event, name="update-user-event"),
    path('email-otp/<id>', views.email_otp, name="email-otp"),
    path('user-add-blog', views.user_add_blog, name="user-add-blog"),
    path('user-add-event', views.user_add_event, name="user-add-event"),
    path('post-event-user', views.post_event_user, name="post-event-user"),

    # path('careers/graduate', views.graduate_page, name="graduate"),
    # path('careers/experience', views.experience_page, name="experience"),
    # path('careers/intern', views.intern_page, name="intern"),
    # path('careers/apply-form/<id>', views.apply_form, name="apply-form"),
    # path('submit-form', views.submit_form, name="submit-form"),

    # urls for admin actions

]
