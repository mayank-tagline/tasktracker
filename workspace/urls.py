from django.urls import path
from .views import WorkSpaceView
from .views import WorkSpaceCreateView
from .views import WorkSpaceDetailView

urlpatterns = [
    path('workspace/', WorkSpaceView.as_view() , name='workspace'),
    path('workspace/add', WorkSpaceCreateView.as_view() , name='add-workspace'),
    path('workspace/<str:workspace_id>', WorkSpaceDetailView.as_view() , name='workspace-detail'),
]