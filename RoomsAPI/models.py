from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()
    objective = models.CharField(max_length=40)

    def __str__(self):
        return self.name