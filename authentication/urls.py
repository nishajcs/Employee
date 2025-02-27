# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.SignupPage, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('home/', views.home, name="home"),
    path('logout/', views.logoutPage, name="logout")
]
