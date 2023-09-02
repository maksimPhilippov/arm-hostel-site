from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50)
    armName = models.CharField(max_length=50)
    rusName = models.CharField(max_length=50)

    places = models.IntegerField()

class RoomPhoto(models.Model):
    image = models.ImageField(upload_to="media/")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

class Tour(models.Model):
    preview = models.ImageField(upload_to="media/")
    name = models.CharField(max_length=50)
    description = models.TextField()

    armName = models.CharField(max_length=50)
    armDescription = models.TextField()

    rusName = models.CharField(max_length=50)
    rusDescription = models.TextField()
