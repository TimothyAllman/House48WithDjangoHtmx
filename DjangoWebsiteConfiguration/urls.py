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
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from DjangoFrontendPages.views import HomePageEndpoint, OtherAddPageEndpoint, OtherDetailsPageEndpoint
from DjangoFrontendPages.views import OtherListPageEndpoint
from DjangoFrontendPages.views import TallPageEndpoint

urlpatterns = [
    path('admin/', admin.site.urls),

    # pages
    path("", RedirectView.as_view(pattern_name="HomePageEndpoint", permanent=False), name="NoPageEndpoint"),
    path("home/", HomePageEndpoint, name="HomePageEndpoint"),
    path("other/",  RedirectView.as_view(pattern_name="OtherListPageEndpoint", permanent=False), name="OtherPagesEndpoint"),
    path("other/List/", OtherListPageEndpoint, name="OtherListPageEndpoint"),
    path("other/Details/", OtherDetailsPageEndpoint, name="OtherDetailsPageEndpoint"),
    path("other/Add/", OtherAddPageEndpoint, name="OtherAddPageEndpoint"),
    path("tall/", TallPageEndpoint, name="TallPageEndpoint"),

    # api
    path("NewOutput/", NewOutputEndpoint),
]
