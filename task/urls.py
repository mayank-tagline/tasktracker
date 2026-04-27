from django.urls import path
from .views import TaskDeleteView, TaskUpdateView, TaskView
from .views import TaskCreateView

urlpatterns = [
    path('workspace/<str:workspace_id>/task/', TaskView.as_view() , name='task'),
    path('workspace/<str:workspace_id>/task/add', TaskCreateView.as_view() , name='add-task'),
    path('workspace/<str:workspace_id>/task/<str:task_id>/delete', TaskDeleteView.as_view() , name = 'delete-task'),
    path('workspace/<str:workspace_id>/task/<str:task_id>/update', TaskUpdateView.as_view() , name = 'update-task'),
]