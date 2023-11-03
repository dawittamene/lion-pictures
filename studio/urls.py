
from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('booking/', views.booking, name="booking"),
    
    path('contact/', views.contact, name="contact"),
    path('Gallery/', views.Gallery, name="Gallery"),
    path('loginpage/', views.loginpage, name="loginpage"),
    
    path('signuppage/', views.signuppage, name="signuppage"),
    path('logoutPage/', views.logoutPage, name="logoutPage"),
    path('findpage/', views.findpage, name="findpage"),
    
   
    path('post_user_photo/', views.post_user_photo, name="post_user_photo"),
    path('messagess/', views.messagess, name="messagess"),
    path('contact_booking/', views.contact_booking, name="contact_booking"),
    
    path('gallary_post/', views.gallary_post, name="gallary_post"),
    path('UpdatePage/<str:pk>/', views.UpdatePage, name="UpdatePage"),
]  



