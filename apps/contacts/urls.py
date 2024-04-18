from django.urls import path
from apps.base.views import index 
from apps.contacts import views
from apps.base import views
from apps.secondary import views
urlpatterns = [
    path('', index, name='index'),
    path('contact/', views.contact, name='contact'),  
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
]



