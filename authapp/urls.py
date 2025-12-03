from django.urls import path
from . import views
app_name = "authapp"

urlpatterns = [
    path('', views.index, name='home'),
    #path('dashboard/', views.user_dashboard, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]