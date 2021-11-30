from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/<str:pk>/',views.services,name='services'),
    path('downloadfile',views.downloadfile,name='downloadfile'),
    path('blog/',views.blog,name='blog'),
    path('blog/<str:slug>/',views.blogpost,name='blogpost'),
]