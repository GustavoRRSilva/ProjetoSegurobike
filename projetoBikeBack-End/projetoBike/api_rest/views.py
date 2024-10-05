from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET'])
def get_users(request):
        if(request.method == 'GET'):
            users = User.objects.all()
            serializer = UserSerializer(users,many = True)
            return Response(serializer.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_id(request,id):
        try:
             user = User.objects.get(pk = id)
        except:
             return Response(status = status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
 

@api_view(['POST'])
def user_create(request):
     if request.method == 'POST':
          new_user = request.data
          serializer = UserSerializer(data=new_user)

          if serializer.is_valid():
                serializer.save()
                return Response('Usuario criado!',status = status.HTTP_201_CREATED)
          
@api_view(['DELETE'])
def delete_user(request, id):
    if request.method == 'DELETE':
        try:
            # Busca o usuário pelo id
            delete_user = User.objects.get(pk=id)
            # Deleta o usuário
            delete_user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            # Se o usuário não for encontrado
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Outros erros
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        

     









""" def databaseEmDjango():
    data = User.objects.get(pk="user_id") #objeto
    data = User.objects.filter( bike_user_id = 1)#QUERYSET

    data = User.objects.exclude(bike_user_id = 2)#QUERYSET

    data.save()

    data.delete() """