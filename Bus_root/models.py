from django.db import models

# Create your models here.




class MovieInfo(models.Model):
    Bus_name=models.CharField(max_length=255)
    Bus_number=models.IntegerField(null=True)
    Bus_root=models.TextField()
    Bus_image=models.ImageField(upload_to='images/',null=True)
    Bus_owner=models.CharField(max_length=255)
def __str__(self):
        return self.Bus_name