from django.urls import path
from .views import CarsListApiView, CarsRetrieveApiView, CarsAPIView

app_name = 'cars'

urlpatterns = [
    path('api/v1/cars-list/', CarsListApiView.as_view(), name='cars_list'),
    path('api/v1/cars-retrieve/<int:pk>/', CarsRetrieveApiView.as_view(), name='cars_retrieve'),
    path('api/v1/cars/', CarsAPIView.as_view(), name='cars'),

]