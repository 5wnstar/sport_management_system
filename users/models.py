from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('administrator', 'Administrator'),
        ('coach', 'Coach'),
        ('player', 'Player'),
    )
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES, default='player')

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey('teams.Team', related_name='team_players', on_delete=models.SET_NULL, null=True, blank=True)
