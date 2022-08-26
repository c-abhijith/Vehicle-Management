from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializer import *
from userside.permission import UserPermission

# Create your views here.

class Vechicle_Data(APIView):
    permission_classes = (UserPermission,)  
    def get(self,request):
        prod = VechicleDetails.objects.all()
        serializer = VechicleSerializer(prod,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer =VechicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class Vechicle_Datas(APIView):
    permission_classes = (UserPermission,)  
    def get(self,request,pk):
        datas = VechicleDetails.objects.get(id=pk)
        serializer = VechicleSerializer(datas)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,pk):
        datas = VechicleDetails.objects.get(id=pk)
        serializer =VechicleSerializer(datas,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk):
        VechicleDetails.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)
