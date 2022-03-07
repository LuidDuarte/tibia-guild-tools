from django.urls import path

from guild_tracker import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('online/', views.list_online_players, name='online'),
]