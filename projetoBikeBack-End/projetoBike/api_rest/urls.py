from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_all_users'),
    path('users/<int:id>', views.get_by_id, name='get_user_by_id'),
    path('users/create', views.user_create, name='create_user'),
    path('users/delete/<int:id>', views.delete_user, name='delete_user'),
]
