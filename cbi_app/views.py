from django.shortcuts import render

# Create your views here.
def home(req):
    active = 'active'
    return render(req,'home.html',{'home_active':active})

def about(req):
    active = 'active'
    return render(req,'about.html',{'about_active':active})

def services(req):
    active = 'active'
    return render(req,'services.html',{'service_active':active})


def contact(req):
    active = 'active'
    return render(req,'contact.html',{'contact_active':active})