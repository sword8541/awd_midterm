from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView, TemplateView, DetailView,CreateView,DeleteView,UpdateView
from django.db.models import Avg,Min,Max,Count

# Create your views here.

def index(request):
    return render(request,'america_car_renting/index.html')

#a function based view for a simple demo 
def OwnerWithMostVehicles(request):
    queryset = Vehicle_owner.objects.annotate(num_vehicles=Count('vehicle')).order_by('-num_vehicles')[:5]
    template_name = "america_car_renting/top5_owners.html"
    list_of_dicts = [l for l in queryset.values()]
    return render(request,template_name,{'data':list_of_dicts})

#a class based view of creating a new vehicle
class Vehicle_create(CreateView):
    model = Vehicle
    template_name = 'america_car_renting/create_vehicle.html'
    form_class = VehicleForm
    success_url = '/create_vehicle/'
    
