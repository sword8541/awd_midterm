from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework import generics, mixins
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.db.models import Avg,Min,Max,Count,Sum
from rest_framework.generics import ListAPIView
from django.forms.models import model_to_dict
from django.db.models import Q




class VehicleDetails(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView
                  ):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

    
class VehicleList(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleListSerializer

class StateDetails(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView
                  ):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class CityDetails(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView
                  ):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

        
class VehicleOwnerDetails(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView
                  ):
    queryset = Vehicle_owner.objects.all()
    serializer_class = VehicleOwnerSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

    
class CityWithMostEVs(ListAPIView):
    ev_count = Count('vehicle',filter=Q(vehicle__fuel_type__exact = 'ELECTRIC'))
    queryset = City.objects.annotate(num_EVs=ev_count).order_by('-num_EVs')[:5]
    def list(self, request):
        queryset = self.get_queryset()
        list_of_dicts = [l for l in queryset.values()]
        # the serializer didn't take my RawQuerySet, so made it into a list
        # serializer = StatSerializer(list(queryset), many=True)
        # return Response(serializer.data)
        return JsonResponse(list_of_dicts,safe=False) 

class FuelTypeOverView(ListAPIView):
    queryset =Vehicle.objects.values('fuel_type').annotate(num_vehicles=Count('fuel_type')).order_by('-num_vehicles') 
    def list(self, request):
        queryset = self.get_queryset()
        list_of_dicts = [l for l in queryset]
        return JsonResponse(list_of_dicts,safe=False) 


    
# This is a class based api view
class apiOwnerWithMostVehicles(ListAPIView):
    queryset = Vehicle_owner.objects.annotate(num_vehicles=Count('vehicle')).order_by('-num_vehicles')[:5]
    
    def list(self, request):
        queryset = self.get_queryset()
        list_of_dicts = [l for l in queryset.values()]
        return JsonResponse(list_of_dicts,safe=False)
    
  
class CityByFuelType(ListAPIView):
    queryset = City.objects.values('city_name','vehicle__fuel_type').annotate(num_vehicles=Count('vehicle__fuel_type'))
    def list(self, request):
        queryset = self.get_queryset()
        list_of_dicts = [l for l in queryset]
        return JsonResponse(list_of_dicts,safe=False)

class VehicleType(ListAPIView):
    queryset =Vehicle.objects.values('vehicle_type').annotate(num_vehicles=Count('vehicle_type')).order_by('-num_vehicles') 
    def list(self, request):
        queryset = self.get_queryset()
        list_of_dicts = [l for l in queryset]
        return JsonResponse(list_of_dicts,safe=False) 

class VehicleMake(ListAPIView):
    queryset =Vehicle.objects.values('vehicle_make').annotate(num_vehicles=Count('vehicle_make')).order_by('-num_vehicles') 
    def list(self, request):
        queryset = self.get_queryset()
        list_of_dicts = [l for l in queryset]
        return JsonResponse(list_of_dicts,safe=False)  
    
class EVMake(ListAPIView):
    queryset =Vehicle.objects.filter(fuel_type__exact = 'ELECTRIC').values('vehicle_make').annotate(num_EVs=Count('vehicle_make')).order_by('-num_EVs') 
    def list(self, request):
        queryset = self.get_queryset()
        list_of_dicts = [l for l in queryset]
        return JsonResponse(list_of_dicts,safe=False)  


class VehicleWithHighestRanking(ListAPIView):
    #vehicle average ranking with over 1000 user reviews  
    queryset =Vehicle.objects.values('vehicle_make','vehicle_model').annotate(review_count=Sum('review_count'),ranking=Avg('ranking')).filter(review_count__gt=1000).order_by('-ranking') 
    def list(self, request):
        queryset = self.get_queryset()
        list_of_dicts = [l for l in queryset]
        return JsonResponse(list_of_dicts,safe=False)  