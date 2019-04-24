from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('help/', views.help, name='help'),
    path('payment/', views.payment, name='payment'),
    path('privacy/', views.privacy, name='privacy'),
    path('product/', views.product, name='product'),
    path('product2/', views.product2, name='product2'),
    path('single/', views.single, name='single'),
    path('single2/', views.single2, name='single2'),
    path('terms/', views.terms, name='terms'),
    path('message/',views.message, name='message'), 
    
]
