from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_task/', views.add_task, name='add_task'),
    path('', views.task_list, name='task_list'),
]
