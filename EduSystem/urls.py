  
"""EduSystem URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexView,name="home"),
    path('accounts/',indexView,name="home"),
    path('accounts/dashboard/',dashboardView,name="dashboard"),
    path('accounts/login/',LoginView.as_view(),name="login_url"),
    path('accounts/register/',registerView,name="register_url"),
    path('accounts/logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
    path('accounts/dashboard/student/',student),
    path('accounts/dashboard/teacher/',teacher),
    path('accounts/dashboard/student/sendanswer/',sendanswer),
    path('accounts/dashboard/student/answers/',answers),
    path('', TemplateView.as_view(template_name='home.html'),name='home' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)