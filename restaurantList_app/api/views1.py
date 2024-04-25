from restaurantList_app.models import Restaurant
from restaurantList_app.api.serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(http_method_names=['GET', 'POST'])
def restra_list(request):
    
    if request.method == 'GET' :
        restras = Restaurant.objects.all()
        serializer = RestaurantSerializer(restras, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST' :
        serializer = RestaurantSerializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def restra_details(request, pk):
    
    if request.method == 'GET':
        try :
            restra = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response({'error' :'Restaurant Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = RestaurantSerializer(restra)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        restra = Restaurant.objects.get(pk=pk)
        serializer = RestaurantSerializer(restra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        restra = Restaurant.objects.get(pk=pk)
        restra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    