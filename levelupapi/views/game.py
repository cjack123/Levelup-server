"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game

class GameView(ViewSet):
    """Level up game view """

    def retrieve(self, request, pk):
        """Handle GET requests for single games

        Returns:
            Response -- JSON serialized games
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """

        games = Game.objects.all()

        # Add in the next 3 lines
        game_type = request.query_params.get('type', None)
        if game_type is not None:
            games = games.filter(game_type_id=game_type)

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game
    """
    class Meta:
        model = Game
        fields = ('game_type','title','maker', 'gamer', 'number_of_players', 'skill_level')
        depth = 1