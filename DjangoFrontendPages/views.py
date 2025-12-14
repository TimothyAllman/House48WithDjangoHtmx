from django.shortcuts import render
from django.views.generic import RedirectView

# Create your views here.
def NoPageEndpoint(request):
    return RedirectView.as_view(url="home/", permanent=False)

def HomePageEndpoint(request):
    return render(request,"HomePage.html")

def OtherPagesEndpoint(request):
    return RedirectView.as_view(url="otherList/", permanent=False)

def OtherListPageEndpoint(request):
    return render(request,"OtherListPage.html")

def TallPageEndpoint(request):
    return render(request,"TallPage.html")