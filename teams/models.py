from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.OneToOneField('users.Coach', on_delete=models.SET_NULL, null=True, blank=True)
    players = models.ManyToManyField('users.Player', related_name='player_teams', blank=True)

    def __str__(self):
        return self.name
