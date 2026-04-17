from django.urls import path
from .views import WorkSpaceView
from .views import WorkSpaceCreateView

urlpatterns = [
    path('workspace/', WorkSpaceView.as_view() , name='workspace'),
    path('workspace/add', WorkSpaceCreateView.as_view() , name='add-workspace'),
]