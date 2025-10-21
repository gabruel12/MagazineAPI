from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.IntegerField(max_length=25)
    objective = models.CharField(max_length=40)

    def __str__(self):
        return self.name