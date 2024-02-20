from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='home'),
path("register/",views.register,name = 'register'),
path('user_login/', views.user_login, name='user_login'),
path('logout/', views.user_logout,name= 'user_logout'),
path('profile/', views.profile, name='profile'),
]