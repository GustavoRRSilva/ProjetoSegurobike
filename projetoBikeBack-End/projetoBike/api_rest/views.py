from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User,Bike
from .serializers import UserSerializer,BikeSerializer

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


@api_view(['PUT'])
def att_user(request, id):
    user = get_object_or_404(User, pk=id)  # Trata o erro caso o usuário não seja encontrado
    serializer = UserSerializer(user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)  # Status 200 para sucesso
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna erros de validação
    


@api_view(['GET'])
def get_bikes(request):
    bikes = Bike.objects.all()
    serializer = BikeSerializer(bikes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_bike_by_id(request, id):
    bike = get_object_or_404(Bike, pk=id)
    serializer = BikeSerializer(bike)
    return Response(serializer.data)

@api_view(['POST'])
def bike_create(request):
    serializer = BikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def bike_update(request, id):
    bike = get_object_or_404(Bike, pk=id)
    serializer = BikeSerializer(bike, data=request.data, partial=True)  # 'partial=True' permite atualização parcial

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def bike_delete(request, id):
    bike = get_object_or_404(Bike, pk=id)
    bike.delete()
    return Response(messsage="Bicicleta deletada",status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_bikes_by_user(request, user_id):
    # Obtém o usuário ou retorna 404 se não existir
    user = get_object_or_404(User, pk=user_id)
    
    # Busca todas as bicicletas associadas ao usuário
    bikes = Bike.objects.filter(bike_user_id=user)
    
    # Serializa as bicicletas
    serializer = BikeSerializer(bikes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

