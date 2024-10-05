from rest_framework import serializers


from .models import User,Bike;

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = ["user_id","user_fullname","user_age"]


class BikeSerializer(serializers.ModelSerializer):
        class Meta: 
                model:Bike
                fields = "__all__"