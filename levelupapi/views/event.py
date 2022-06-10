"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import  serializers, status
from levelupapi.models import Event
from levelupapi.models import Game
from levelupapi.models import Gamer

class EventView(ViewSet):
    """Level up event view"""
    def retrieve(self, request, pk):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serialized event
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all event

        Returns:
            Response -- JSON serialized list of event
        """
        events = Event.objects.all()

        # Add in the next 3 lines
        game = request.query_params.get('type', None)
        if game is not None:
            events = events.filter(game_id=game)

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        
        Returns -- JSON serializer game instance
        """

        organizer = Gamer.objects.get(pk=request.data["organizer"])
        serializer = CreateEventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organizer=organizer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date_time', 'organizer')
        depth = 2

class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'game', 'description', 'date_time', 'organizer']