from django.urls import path, include
# from . import views
from restaurantList_app.api.views import restra_list , restra_details


urlpatterns = [
    # path('list/', views.restra_list),
    path('list/', restra_list, name='restra-list'),
    path('<int:pk>/', restra_details, name='restra-details'),
]