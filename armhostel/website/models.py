from django.db import models

# class Room(models.Model):
#     name = models.CharField(50)
#     armName = models.CharField(50)
#     rusName = models.CharField(50)

#     places = models.IntegerField()

# class RoomPhoto(models.Model):
#     image = models.ImageField()
#     room = models.ForeignKey(Room, on_delete=)

class Tour(models.Model):
    preview = models.ImageField(upload_to="media/")
    name = models.CharField(max_length=50)
    description = models.TextField()

    armName = models.CharField(max_length=50)
    armDescription = models.TextField()

    rusName = models.CharField(max_length=50)
    rusDescription = models.TextField()
