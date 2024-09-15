from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register'),
    path('forgot_password/', views.forgot_password_view, name='forgot_password'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    
    # path('login/', views.custom_login, name='login'),
    # path('', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]