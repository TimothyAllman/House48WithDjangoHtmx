from django.shortcuts import render
from django.views.generic import RedirectView

# Create your views here.
def NoPageEndpoint(request):
    return HomePageEndpoint(request)


def HomePageEndpoint(request):
    return render(request,"HomePage.html")

def OtherPagesEndpoint(request):
    return OtherListPageEndpoint(request)

def OtherListPageEndpoint(request):
    return render(request,"OtherListPage.html")

def OtherDetailsPageEndpoint(request):
    return render(request,"OtherDetailsPage.html")

def OtherAddPageEndpoint(request):
    return render(request,"OtherAddPage.html")

def TallPageEndpoint(request):
    return render(request,"TallPage.html")