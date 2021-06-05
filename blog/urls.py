from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('view/<int:pk>/', views.retrieve, name='retrieve'),
    path('view2/<int:pk>/', views.RetrieveView.as_view(), name='retrieve'),
    path('rate/<int:pk>', views.rate, name='rate'),
    path('register', views.reqister, name='register'),
    path('login', views.loginView, name='login'),
    path('register', views.reqister, name='register'),
    # path('landing', views.landing, name='landing'), # Daniyar
    path('add_post', views.add_post, name='add_post'), # Arli
    path('user/<int:pk>/', views.user, name='user'), # Bakdoolot
    path('search', views.search, name='search'),  # Ainura
    #path('contact', views.contact, name='contact'), # Askat
    #path('404', views.not_found, name='not_found') # Akim
]