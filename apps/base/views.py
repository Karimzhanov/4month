from django.shortcuts import render
from apps.base.models import Home, Hom
from apps.contacts.models import Contacts
from apps.base.models import About, Secondary
from apps.secondary.models import Course

def index(request):
    user = Home.objects.latest('id')
    users= Hom.objects.latest('id')
    courses = Course.objects.all()  
    info_users = Secondary.objects.latest('id')
    return render(request, 'index2.html', locals())

def about(request):
    info_user = About.objects.latest('id')
    info_users = Secondary.objects.latest('id')
    return render(request, 'about.html', locals())  

def course(request):
    courses = Course.objects.all()
    return render(request, 'course.html', locals())

def contact(request):
    info_contact = Contacts.objects.latest('id')
    return render(request, 'contact.html', locals())
