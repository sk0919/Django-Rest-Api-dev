# from django.shortcuts import render
# from .models import Restaurant

# from django.http import JsonResponse

# # Create your views here.


# # Complex Queryset Result  ->  python dictionary -> JsonResponse
# def restra_list(request):
#     restras = Restaurant.objects.all()
#     # print(restras)
#     data = {
#         'restaurants' : list(restras.values())
#         }
    
#     return JsonResponse(data)

# def restra_details(request, pk):
#     restra = Restaurant.objects.get(pk=pk)
#     # print(restra)
    
#     data = {
#         'name' : restra.name,
#         'description' : restra.description,
#         'active' : restra.active
#     }
    
#     return JsonResponse(data)
