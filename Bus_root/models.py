from django.db import models
from datetime import time
from django.contrib.auth.models import User

class MovieInfo(models.Model):
    Bus_name = models.CharField(max_length=255)
    Bus_number = models.IntegerField(null=True)
    Bus_root = models.TextField()
    Bus_time = models.TimeField(default=time(0, 0))  # Set a default time
    Bus_image = models.ImageField(upload_to='images/', null=True)
    Bus_owner = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Bus_name
