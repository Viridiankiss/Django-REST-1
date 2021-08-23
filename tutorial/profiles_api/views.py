from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status

class helloApiView(APIView):

    serializer_class=serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview=[
            'Hola mundo'
        ]
        return Response ({'message': 'Hello', 'an_api_view': an_apiview})

    def post(self, request):
        '''Crea un mensaje con nuestro nombre'''
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''Maneja actualizar un objeto'''
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        '''Maneja actualizar parcialmente un objeto'''
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        '''Borrar un objeto'''
        return Response({'method':'DELETE'})
