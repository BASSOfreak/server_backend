from django.db import models
from django.db import models
from django.utils import timezone

class Location(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " @ " + self.location.name

class Entry(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    def __str__(self):
        return "tea on " + str(self.created_date) + " @ " + self.location.name