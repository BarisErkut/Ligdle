from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player_data/<str:player_name>/', views.player_data, name='player_data'),
    path('random_player/', views.random_player, name='random_player'),
    path('search_players/', views.search_players, name='search_players'),
]
