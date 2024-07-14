from django.db import models
from teams.models import Team

class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='home_team', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='away_team', on_delete=models.CASCADE)
    date = models.DateTimeField()
    result = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date}"

