from django.urls import path, include
from .views import register
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=AuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]