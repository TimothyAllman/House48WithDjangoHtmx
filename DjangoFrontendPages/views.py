from django.shortcuts import render

# Create your views here.
def HomePageEndpoint(request):
    return render(request,"HomePage.html")

def OtherListPageEndpoint(request):
    return render(request,"OtherListPage.html")

def OtherDetailsPageEndpoint(request):
    return render(request,"OtherDetailsPage.html")

def OtherAddPageEndpoint(request):
    return render(request,"OtherAddPage.html")

def TallPageEndpoint(request):
    return render(request,"TallPage.html")