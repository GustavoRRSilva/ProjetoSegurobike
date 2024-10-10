from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_all_users'),
    path('users/<int:id>', views.get_by_id, name='get_user_by_id'),
    path('users/create', views.user_create, name='create_user'),
    path('users/delete/<int:id>', views.delete_user, name='delete_user'),
    path('users/att/<int:id>',views.att_user,name = "att_user"),
  path('login/', views.login_view, name='login'),
      path('users/<int:user_id>/bikes/', views.get_bike_by_id, name='get_bikes_by_user'),

    path('bikes/', views.get_bikes, name='get_bikes'),
    path('bikes/<int:id>/', views.get_bike_by_id, name='get_bike_by_id'),
    path('bikes/create/', views.bike_create, name='bike_create'),
     path('bikes/update/<int:id>/', views.bike_update, name='update_bike'),
    path('bikes/delete/<int:id>/', views.bike_delete, name='delete_bike'),
]
