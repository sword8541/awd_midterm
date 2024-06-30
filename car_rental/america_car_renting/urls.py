from django.urls import include, path
from . import views  # from the same path
from . import api

urlpatterns = [
    # main page to list all the entrypoints and package versions
    path('',views.index,name='index'),
    # a simple page with a form that we make the post request
    path('create_vehicle/',views.Vehicle_create.as_view(),name='create-vehicle'),
    path('api/vehicles/<int:pk>',api.VehicleDetails.as_view(),name='vehicle-detail'),
    path('api/vehicles',api.VehicleList.as_view()),
    path('api/vehicles/fuel-type',api.FuelTypeOverView.as_view()),
    path('api/vehicles/vehicle-type',api.VehicleType.as_view()),
    path('api/vehicles/vehicle-make',api.VehicleMake.as_view()),
    path('api/vehicles/ev-make',api.EVMake.as_view()),
    path('api/vehicles/highest-ranking',api.VehicleWithHighestRanking.as_view()),
    path('owners/top5',views.OwnerWithMostVehicles,name='owner-with-most-renting-vehicles'),
    path('api/owners/top5',api.apiOwnerWithMostVehicles.as_view()),
    path('api/cities/ev-top5',api.CityWithMostEVs.as_view()),
    path('api/cities/vehicle-by-fuel-type',api.CityByFuelType.as_view()),
        
]

