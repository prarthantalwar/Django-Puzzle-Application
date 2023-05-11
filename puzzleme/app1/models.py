from django.db import models

# Create your models here.
class Player(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    score = models.IntegerField()

    def __str__(self):
        return self.username