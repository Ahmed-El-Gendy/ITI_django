from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]
