"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include

admin.site.site_title = 'KYTOweb'
admin.site.site_header = 'KYTOweb'
admin.site.index_title = 'tools'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rankcheck/', include('rankcheck.urls')),
    path('suggestnet/', include('suggestnet.urls')),
    path('kyokigo/', include('kyokigo.urls')),
    path('test1/', include('test1.urls')),
    path('test2/', include('test2.urls')),
]
