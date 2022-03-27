

from django.shortcuts import render
from n_apps.models import Contact
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method =='POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse(" Thanks ")

    return render (request, 'contact.html')
def about(request):
    return render(request,'about.html')
