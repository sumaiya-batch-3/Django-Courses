from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('New_app', views.about, name = 'about'),

]