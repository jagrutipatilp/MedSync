from django.urls import path
from med import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about_page/", views.about_view, name="about_page.html"),
    path("login_page/", views.login_view, name="login.html"),
    path("signin_page/", views.signin_view, name="signin.html"),
    path("fillhistory_page/", views.fillhistory_view, name="fillhistory.html"),
    path("contactus_page/", views.contactus_view, name="contactus.html"),
    path("newsevents_page/", views.newsevents_view, name="newsevents.html"),
    path("remedies_page/", views.remedies_view, name="remedies.html"),
    path("terms_view_page/", views.terms_view, name="termsofuse.html"),
    path("privacy_view_page/", views.privacy_view, name="privacy_policy.html"), 
    path('success/', views.success_view, name='success.html'),


]
