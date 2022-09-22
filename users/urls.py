from django.urls import path
from django.contrib.auth import views

from django.contrib.auth import  views as auth_views


urlpatterns = [
    path('users/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        extra_context={'titulo': 'Autenticação'}
    ), name='login'),

    path('sair/', views.LogoutView.as_view(), name='logout')
]