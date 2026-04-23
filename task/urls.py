from django.urls import path
from .views import TaskView
from .views import TaskCreateView

urlpatterns = [
    path('workspace/<str:workspace_id>/task/', TaskView.as_view() , name='task'),
    path('workspace/<str:workspace_id>/task/add', TaskCreateView.as_view() , name='add-task'),
]