from django.urls import path

from .views import (
    get_tasks,
    add_task,
    delete_task,
)

urlpatterns = [

    path('tasks/', get_tasks),

    path('tasks/add/', add_task),

    path('tasks/delete/<int:pk>/', delete_task),
]