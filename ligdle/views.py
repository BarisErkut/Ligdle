import random
from django.shortcuts import render
from django.http import JsonResponse
from .models import Player

def index(request):
    players = Player.objects.all()
    return render(request, 'ligdle/index.html', {"players": players})

def player_data(request, player_name):
    try:
        player = Player.objects.get(name=player_name)
        player_data = {
            "name": player.name,
            "team": player.team,
            "position": player.position,
            "age": player.age,
            "jersey_number": player.jersey_number,
        }
        return JsonResponse(player_data)
    except Player.DoesNotExist:
        return JsonResponse({"error": "Player not found"}, status=404)

# Global variables to store the target player and game status
target_player = None
game_started = False

def random_player(request):
    global target_player, game_started

    players = Player.objects.all()
    if players:
        selected_player = random.choice(players)
        player_data = {
            "name": selected_player.name,
            "team": selected_player.team,
            "position": selected_player.position,
            "age": selected_player.age,
            "jersey_number": selected_player.jersey_number,
        }

        # Set the target player when the game starts
        target_player = selected_player.name
        game_started = True

        return JsonResponse(player_data)
    else:
        return JsonResponse({"error": "No players found"}, status=404)
def search_players(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter

    # Filter players based on the search query
    players = Player.objects.filter(name__icontains=query)
    
    # Create a list of player names for suggestions
    suggestions = [player.name for player in players]

    return JsonResponse({"suggestions": suggestions})