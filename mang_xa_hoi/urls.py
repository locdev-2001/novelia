from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('settings', views.settings, name='settings'),
    path('upload',views.upload, name='upload'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout')
]