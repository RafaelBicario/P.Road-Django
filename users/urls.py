
from django.urls import path
from django.contrib.auth import views

from users.views import UserCreate

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('register', UserCreate.as_view(), name='register-user'),

]