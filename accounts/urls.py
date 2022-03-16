from django.urls import path
from . import views
from accounts.models import *


urlpatterns=[

    path('register', views.userregister, name='userregister'),
    path('login', views.userlogin, name='userlogin'),
    path('logout',views.logout,name='logout'),

]