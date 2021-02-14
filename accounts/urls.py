from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('useractivation/<str:token>', views.user_activation, name='useractivation'),
    path('users/signup/', views.create_user, name='createuser'),
]