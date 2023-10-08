
from django import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Signup,name='signup'),
    path('login/',Login,name='login'),
    path('home/',Home,name='home'),
    path('logout/',Logout,name='logout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
