from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin

# # Create your views here.
# #patch is for partial update and put for complete update
# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def student_crud(request,pk=None):
#     if request.method=='GET':
#         # id=request.data.get('id') #only possible when using api_view
#         id=pk
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data)
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)
#     if request.method=='POST':
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'})
#         return Response(serializer.errors)
#     if request.method=='PUT':
#         # id=request.data.get('id')
#         id=pk
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data updated full'})
#         return Response(serializer.errors)
#     if request.method=='PATCH':
#         id=pk
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data updated partial'})
#         return Response(serializer.errors)
#     if request.method=='DELETE':
#         # id=request.data.get('id')
#         id=pk
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         return Response({'msg':'Data deleted'})

#GENERIC API VIEW AND MODEL MIXINS  use CBV FOR IT 

class StudentList(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
        
class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def retrieve(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)