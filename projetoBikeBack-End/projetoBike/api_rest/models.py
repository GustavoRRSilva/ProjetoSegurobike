from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_fullname = models.CharField(max_length=200, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)
<<<<<<< HEAD
    user_password = models.CharField(default="12345678",max_length = 8)
    user_plan = models.CharField(default=0,max_length=30)
    def __str__(self):
        return f'Id:{self.user_id} | fullname: {self.user_fullname}'
=======
>>>>>>> 231d2694fe2ea5d208e3f1bb90acd6ec1ef22368

class Bike(models.Model):  # Corrigido de models.Models para models.Model
    bike_id = models.AutoField(primary_key=True)
    bike_model = models.CharField(max_length=100, default='', blank=False)  # Corrigido o max_length
    bike_year = models.IntegerField()
<<<<<<< HEAD
    bike_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

=======
    bike_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> 231d2694fe2ea5d208e3f1bb90acd6ec1ef22368
