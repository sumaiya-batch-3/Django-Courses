# from django.urls import path,include
# from .views import add_Musician
# from django.contrib import admin
# from . import views
# urlpatterns = [
#     path('add/',views.add_Musician, name = 'add_Musician'),
#     path('register/',views.register,name='register'),
#     path('login/',views.user_login,name='user_login'),
#     path('logout/',views.user_logout,name ='user_logout'),
#     path('edit/<int:id>',views.edit_Musician,name='edit_Musician'),
#     path('delete/<int:id>',views.delete_musician,name='delete_musician'),

# ]
from django.urls import path, include
from .views import add_Musician
from django.contrib import admin
from . import views

urlpatterns = [
    path('add/', views.add_Musician, name='add_Musician'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('edit/<int:id>/', views.edit_Musician, name='edit_Musician'),
    path('delete/<int:id>/', views.delete_musician, name='delete_musician'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]




