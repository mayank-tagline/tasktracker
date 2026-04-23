from django.urls import path
from .views import WorkSpaceView
from .views import WorkSpaceCreateView
from .views import WorkSpaceDetailView
from .views import AddMemberView

urlpatterns = [
    path('workspace/', WorkSpaceView.as_view() , name='workspace'),
    path('workspace/add', WorkSpaceCreateView.as_view() , name='add-workspace'),
    # path('workspace/<str:workspace_id>', WorkSpaceDetailView.as_view() , name='workspace-detail'),
    path('workspace/<str:workspace_id>/add-member', AddMemberView.as_view() , name='add-member'),
]