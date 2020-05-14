from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("menu", views.menu, name='menu'),
    path("order", views.order, name='order'),
    path("find-us", views.find_us, name='find-us'),
    path("register", views.register_user, name='register'),
    path("login", views.user_login, name='login'),
    path("logout", views.user_logout, name='logout')
]