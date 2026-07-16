from django.db import models
from django.db import models

class Location(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.TextField()
    location = ForeignKey(Location)
    def __str__(self):
        return self.name + " @ " + location.namew