from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework import generics, mixins
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.db.models import Avg,Min,Max,Count
from rest_framework.generics import ListAPIView
from django.forms.models import model_to_dict




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
    

# @api_view(['Get'])
# def genes_list(request):
#     try:
#         genes = Gene.objects.all()
#     except Gene.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = GeneListSerializer(genes, many=True)
#         return Response(serializer.data)
    
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
    
class CityWithMostVehicles(generics.ListAPIView):
    pass 

# class OwnerWithMostVehicles(generics.ListAPIView):
#     queryset = Vehicle_owner.objects.annotate(num_vehicles=Count('vehicle')).order_by('-num_vehicles')[:5]
#     serializer_class = VehicleOwnerSerializer
    

class CityWithMostVehicles(generics.ListAPIView):
    queryset = City.objects.annotate(num_vehicles=Count('vehicle')).order_by('-num_vehicles')[:5]
    serializer_class = VehicleOwnerSerializer 

def OwnerWithMostVehicles(request):
    queryset = Vehicle_owner.objects.annotate(num_vehicles=Count('vehicle')).order_by('-num_vehicles')[:5]
    # print(queryset.values())
    # print(queryset[0].owner_id,queryset[0].num_vehicles)
    # serialized_data = VehicleOwnerSerializer(queryset,many=True)
    # for data in list(serialized_data.data):
    #     # data['count'] = 
    #     print(data)
    # print(serialized_data)
    template_name = "america_car_renting/top5_owners.html"
    # return render(request, template_name,{'data': queryset.values()})
    
  


class StatListView(ListAPIView):
    # queryset = Vehicle_owner.objects.raw("SELECT id,owner_id FROM america_car_renting_vehicle_owner LIMIT 10")
    queryset = Vehicle_owner.objects.annotate(num_vehicles=Count('vehicle')).order_by('-num_vehicles')[:5]

    # data = [{'id': q.pk, 'owner_id': q.owner_id, 'count':q.count} for q in queryset]
    print(queryset)
    
    def list(self, request):
        queryset = self.get_queryset()
        list_of_dicts = [model_to_dict(l) for l in queryset]
        # the serializer didn't take my RawQuerySet, so made it into a list
        # serializer = StatSerializer(list(queryset), many=True)
        # return Response(serializer.data)
        return JsonResponse(list_of_dicts,safe=False)

class CityWithMostVehicles(generics.ListAPIView):
    queryset = City.objects.annotate(num_vehicles=Count('vehicle')).order_by('-num_vehicles')[:5]
    serializer_class = VehicleOwnerSerializer 