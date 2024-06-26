from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from restaurantList_app.models import Restaurant, Location
from restaurantList_app.api.serializers import RestaurantSerializer



class RestarauntListAV(APIView):
    
    def get(self, request):
        restras = Restaurant.objects.all()
        serializer = RestaurantSerializer(restras, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        
        serializer =RestaurantSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
        
        
class RestaurantDetailAV(APIView):
    def get(self, request, pk):
        try:
            restra = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response({'error' :'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RestaurantSerializer(restra)
        return Response(serializer.data)
        
        
    def put(self, request, pk):
        restra = Restaurant.objects.get(pk=pk)
        serializer = RestaurantSerializer(restra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restra = Restaurant.objects.get(pk=pk)
        restra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    