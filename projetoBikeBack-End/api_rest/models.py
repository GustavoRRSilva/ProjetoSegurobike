from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_fullname = models.CharField(max_length=200,default='')
    user_email = models.EmailField(default = '')
    user_age = models.IntegerField(default=0)

class Bike(models.Models):
    bike_id = models.AutoField(primary_key=True)
    bike_model = models.CharField(max_length="100",min_length ="1")
    bike_year = models.IntegerField();
    bike_user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    