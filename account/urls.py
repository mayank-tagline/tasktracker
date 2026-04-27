from django.urls import path
from .views import LoginView, RegisterView, LogoutView, UserDetailView, UserView


urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True) , name='login'),
    path('register/', RegisterView.as_view() , name='register'),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('workspace/<str:workspace_id>/user/', UserView.as_view() , name='user'),
    path('workspace/<str:workspace_id>/user/<int:user_id>/', UserDetailView.as_view() , name='user-detail'),
]