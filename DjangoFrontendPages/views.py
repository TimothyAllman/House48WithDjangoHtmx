from django.shortcuts import render

# Create your views here.
def HomePageEndpoint(request):
    return render(request,"HomePage.html")

def OtherPageEndpoint(request):
    return render(request,"OtherPage.html")

def TallPageEndpoint(request):
    return render(request,"TallPage.html")