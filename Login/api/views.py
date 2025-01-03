from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status


class LoginView(APIView):
     def post(self,request):
         serializer=UserSerializer(data=request.data)
         if serializer.is_valid():
            username=serializer.validated_data["username"]
            password=serializer.validated_data["password"]
            try:
                user=User.objects.get(username=username)
                if user.password==password:
                    return Response({'message':'Login successfull'}, status= status.HTTP_200_OK)
                else:
                   return Response({'message':'invalid password'},status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
               return Response({'message':'invalid username'},status=status.HTTP_401_UNAUTHORIZED)
            else:
               return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST )                    
            
""" 
class LoginView(APIView):
   def post(self,request):
      serializer=UserSerializer(data=request.data)
      if serializer.is_valid():
         username=serializer.validated_data["username"]
         password=serializer.validated_data["password"]
         try:
            user=User.objects.get(username=username)
               if user.password==password:
                  return Response({'message':'Login Successfull'},status=status.HTTP_200_OK)
               else:
                  return response({'message':'invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
         except User.DoesNotExist:
            return Response({message':'invalid username'},ststus=status.HTTP_401_UNAUTHORIZED)
         else:
            return Response(serializer.error,status=status.HTTP_400_BAD_Request)
"""