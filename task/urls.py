from django.urls import path
from .views import TaskView
from .views import TaskCreateView

urlpatterns = [
    path('task/', TaskView.as_view() , name='task'),
    path('task/add', TaskCreateView.as_view() , name='add-task'),
]