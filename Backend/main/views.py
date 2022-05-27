from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

class UserTechAPIView(APIView):

    def get(self, request, pk=''):
        if pk == '':
            user = UserTech.objects.all()
            serializer = UserTechSerializer(user, many=True)
            return Response({'data': serializer.data})
        else:
            user = UserTech.objects.get(id=pk)
            serializer = UserTechSerializer(user, many=True)
            return Response({'data': serializer.data})

    def post(self, request):
        if 'auth' in request.GET:
            password = request.data['password']
            # print(password)
            user = UserTech.objects.filter(password=password)
            if user:
                serializer = UserTechSerializer(user, many=True)
                return Response({'data': serializer.data})
            else:                
                return Response({'msg': 'Usuário não encontrado'})
        else:
            serializer = UserTechSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'msg': 'Inserido com sucesso'})

    def put(self, request, pk=''):
        if pk != '':
            user = UserTech.objects.get(id=pk)            
            serializer = UserTechSerializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'msg': 'Falta Informar PK'})

    def delete(self, request, pk=''):
        if pk != '':
            user = UserTech.objects.get(id=pk)            
            user.delete()
            return Response({'msg': 'Deletado com sucesso!'})
        else:
            return Response({'msg': 'Falta Informar PK'})



class DevicesAPIView(APIView):

    def get(self, request, pk=''):
        if 'ano' in request.GET:
            ano = request.GET['ano']
            device = Devices.objects.filter(date__gte=datetime.date(int(ano),1,1))
            serializer = DevicesSerializer(device, many=True)
            return Response({'data': serializer.data})
        elif pk == '':
            device = Devices.objects.all()
            serializer = DevicesSerializer(device, many=True)
            return Response({'data': serializer.data})
        else:
            device = Devices.objects.get(id=pk)
            serializer = DevicesSerializer(device, many=True)
            return Response({'data': serializer.data})

    def post(self, request):
        serializer = DevicesSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': 'Inserido com sucesso'})

    def put(self, request, pk=''):
        if pk != '':
            device = Devices.objects.get(id=pk)            
            serializer = DevicesSerializer(device, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'msg': 'Falta Informar PK'})

    def delete(self, request, pk=''):
        if pk != '':
            devices = Devices.objects.get(id=pk)            
            devices.delete()
            return Response({'msg': 'Deletado com sucesso!'})
        else:
            return Response({'msg': 'Falta Informar PK'})



class CommentsAPIView(APIView):

    def get(self, request, pk=''):
        if 'orderByUser' in request.GET:
            comments = Comments.objects.all().order_by('userFK__name', 'userFK')
            serializer = CommentsGetSerializer(comments, many=True)
            return Response({'data': serializer.data})
        elif pk == '':
            comments = Comments.objects.all()
            serializer = CommentsGetSerializer(comments, many=True)
            return Response({'data': serializer.data})
        else:
            comments = Comments.objects.get(id=pk)
            serializer = CommentsGetSerializer(comments, many=True)
            return Response({'data': serializer.data})

    def post(self, request):
        serializer = CommentsSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': 'Inserido com sucesso'})

    def put(self, request, pk=''):
        if pk != '':
            comments = Comments.objects.get(id=pk)            
            serializer = CommentsSerializer(comments, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'msg': 'Falta Informar PK'})

    def delete(self, request, pk=''):
        if pk != '':
            comments = Comments.objects.get(id=pk)            
            comments.delete()
            return Response({'msg': 'Deletado com sucesso!'})
        else:
            return Response({'msg': 'Falta Informar PK'})