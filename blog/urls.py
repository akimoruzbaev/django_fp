from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:pk>/', views.retrieve, name='retrieve'),
    path('register', views.reqister, name='register'),
    path('login', views.loginView, name='login'),
    path('register', views.reqister, name='register')
]