from datetime import time
from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    room_name = models.CharField(max_length=50)
    room_floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.room_name}: Room {self.room_number} on floor {self.room_floor}"


class Comment(models.Model):
    comment = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.comment}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"