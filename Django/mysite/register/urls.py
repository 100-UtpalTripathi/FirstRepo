from django.urls import path, include
from . import views

app_name = "register"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register/signup', views.signup, name="signup"),
    path('register/login', views.login, name="login"),
    path('register/signupValues', views.signupValues, name="signupValues"),
    path('register/loginValues', views.loginValues, name="loginValues"),
    path('register/logout', views.logout, name="logout"),
]
