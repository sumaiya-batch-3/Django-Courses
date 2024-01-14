
from django.urls import path, include
from . import views
urlpatterns = [
    # path('first/', include('first_app.urls')),
    path('', views.index, name = 'home'),
    path('about/page/<int:id>/', views.about, name = 'about'),
]