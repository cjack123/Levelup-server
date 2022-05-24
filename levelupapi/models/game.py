from django.db import models
from levelupapi.models.game_type import GameType
from levelupapi.models.gamer import Gamer



class Game(models.Model):
    game_type = models.ForeignKey(GameType, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=15)
    maker = models.CharField(max_length=15)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    number_of_players = models.PositiveSmallIntegerField()
    skill_level = models.PositiveSmallIntegerField()