from django.urls import path, include
from . import views
from n_apps.views import index,Contact
from django.contrib import admin

urlpatterns = [
      
     path('admin/',admin.site.urls),
     path('home/', views.index, name='home'),
     path('contact/', views.contact, name='contact'),
     path('', views.about, name='about'),
]