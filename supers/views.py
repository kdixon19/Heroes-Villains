from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET','POST'])
def supers_list(request):

    if request.method == 'GET':
        super_type_name = request.query_params.get('super_types')
        print(super_type_name)
        queryset = Super.objects.all()
        if super_type_name:
            queryset = queryset.filter(super_types__name=super_type_name)
        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def supers_detail(request,pk):
    car = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':   
        serializer = SuperSerializer(car);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

