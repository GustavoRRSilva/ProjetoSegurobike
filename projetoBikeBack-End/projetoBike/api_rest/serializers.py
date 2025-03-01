from rest_framework import serializers


from .models import User,Bike;

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = ["user_id","user_fullname","user_age","user_email","user_plan","user_number","user_birthday","user_gender","user_nome_rua","user_cidade","user_cidade","user_cidade","user_estado","user_pais","user_numero_cartao","user_dono_cartao","user_data_validade"]


class BikeSerializer(serializers.ModelSerializer):
        class Meta: 
                model=Bike
                fields = "__all__"