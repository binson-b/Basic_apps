from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('approve/<int:user_id>', views.approve, name='approve'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:task_id>', views.edit_task, name='edit_task'),
    path('edit_task/', views.edit_task, name='edit_task'),
    path('view_tasks/', views.view_tasks, name='view_tasks'),
    path('task_completed/', views.task_completed, name='task_completed'),
    path('thanks/', views.thanks, name='thanks')
]