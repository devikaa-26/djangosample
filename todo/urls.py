from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle'),
]
