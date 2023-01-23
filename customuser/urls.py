from .views import CustomUserListCreateView, CustomUserUpdateDeleteView
from django.urls import path

urlpatterns = [
    path('', CustomUserListCreateView.as_view(), name='create'),
    path("<int:pk>/", CustomUserUpdateDeleteView.as_view(), name="user_detail"),
]