import email
from django.db import models

from django.contrib.auth.models import User

ROOM_TYPE = (
    ('1BHK','1BHK'),
    ('2BHK','2BHK'),
    ('3BHK','3BHK'),
)

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=264)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    contact_details = models.IntegerField()
    room_type = models.CharField(max_length=6,choices=ROOM_TYPE,default='1BHK',null=True)
    images = models.URLField(max_length=264, null=True, blank=True)
    
    

    def __str__(self):
        return str(self.id) + "--" + self.city


class RentedRooms(models.Model):
    
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE)
    buyer_username = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    odered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_id} -- {self.buyer_username}"

class Cities(models.Model):
    name = models.CharField(max_length=264)
    

    def __str__(self):
        return f"{self.name}"

class Queries(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    problem = models.TextField()