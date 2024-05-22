"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views


from website.views import index, about, profile, meetings, change_profile, register, contact



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('profile', profile, name='profile'),
    path('change_information', change_profile , name='change_profile'),
    path('about', about ),
    path('contact', contact, name='contact' ),
    path('meetings', meetings, name='meetings'),
    path('meetings/', include('meetings.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register, name='register'),
]

