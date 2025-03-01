from django.db import models

class User(models.Model):
      
    MASCULINO = 'M'
    FEMININO = 'F'
    GENERO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino'),
    ]   



    user_id = models.AutoField(primary_key=True)
    user_fullname = models.CharField(max_length=200, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

    user_password = models.CharField(default="12345678",max_length = 8)
    user_plan = models.CharField(default=0,max_length=30)
    user_number = models.CharField(default=12345678912,max_length=11)
    user_birthday= models.DateField(default="0001-01-01",null=True)
    user_gender = models.CharField(max_length=1, choices=GENERO_CHOICES,default="m")
    user_nome_rua = models.CharField(max_length=255,default="lalal")
    user_cidade = models.CharField(max_length=100,default="city")
    user_estado = models.CharField(max_length=100,default="state")
    user_pais = models.CharField(max_length=100,default="country")
    user_numero_cartao = models.CharField(max_length=16,default="0000000000000000")
    user_dono_cartao = models.CharField(max_length=255,default="owner")
    user_data_validade = models.DateField("mm/yyyy",default="0001-01-01",null=True)

class Bike(models.Model):  # Corrigido de models.Models para models.Model
    bike_id = models.AutoField(primary_key=True)
    bike_model = models.CharField(max_length=100, default='', blank=False)  # Corrigido o max_length
    bike_year = models.IntegerField()
    bike_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bike_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
