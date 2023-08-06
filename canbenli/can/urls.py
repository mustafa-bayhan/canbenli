from django.urls import path
from . import views
urlpatterns=[
   
    path('',views.home, name='home'),
    path('blog',views.blog, name='blog'),
    path('contact',views.contact, name='contact'),
    path('blog-single',views.blog_single, name='blog-single'),
    path('blog/<slug:slug>/',views.blog_single,name='blog_single'),
]