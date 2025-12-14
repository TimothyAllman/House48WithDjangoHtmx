"""
URL configuration for DjangoWebsiteConfiguration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from DjangoFrontendPages.views import HomePageEndpoint, NoPageEndpoint, OtherAddPageEndpoint, OtherDetailsPageEndpoint, OtherPagesEndpoint
from DjangoFrontendPages.views import OtherListPageEndpoint
from DjangoFrontendPages.views import TallPageEndpoint

urlpatterns = [
    path("", NoPageEndpoint, name="NoPageEndpoint"),
    path('admin/', admin.site.urls),
    path("home/", HomePageEndpoint, name="HomePageEndpoint"),
    path("other/", OtherPagesEndpoint, name="OtherPagesEndpoint"),
    path("otherList/", OtherListPageEndpoint, name="OtherListPageEndpoint"),
    path("otherDetails/", OtherDetailsPageEndpoint, name="OtherDetailsPageEndpoint"),
    path("otherAdd/", OtherAddPageEndpoint, name="OtherAddPageEndpoint"),
    path("tall/", TallPageEndpoint, name="TallPageEndpoint"),
]
