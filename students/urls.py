from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add_students),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]
