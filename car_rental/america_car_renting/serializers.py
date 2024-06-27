from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import *

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['state_name']

class VehicleOwnerSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Vehicle_owner
        fields = ['owner_id']

class CitySerializer(WritableNestedModelSerializer):
    state = StateSerializer()
    class Meta:
        model = City
        fields = ['city_name','state']

        def create(self,validated_data):
            state_data = self.initial_data.get('state')
            city = City(**{**validated_data,
                        'state':State.objects.get(pk=state_data['id']),
                        })
            city.save()
            return city


class VehicleSerializer(WritableNestedModelSerializer):
    city = CitySerializer()
    vehicle_owner = VehicleOwnerSerializer()
    class Meta:
        model = Vehicle
        fields = ['vehicle_id','vehicle_model','vehicle_make','vehicle_type','vehicle_year','renter_trips_taken',
                  'review_count','rate_daily','ranking','fuel_type','city','vehicle_owner']
    
    def create(self,validated_data):
        city_data = self.initial_data.get('city')
        vehicle_owner_data = self.initial_data.get('vehicle_owner')
        vehicle = Vehicle(**{**validated_data,
                       'city':City.objects.get(pk=city_data['id']),
                       'vehicle_owner':Vehicle_owner.objects.get(pk=vehicle_owner_data['id'])
                       })
        vehicle.save()
        return vehicle
    
       
class VehicleListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields = ['id','vehicle_id','vehicle_model','vehicle_make','vehicle_type','vehicle_year']

        
class StatSerializer(serializers.Serializer):
    owner_id = serializers.CharField(max_length=128, required=True)
    count = serializers.IntegerField(required=True)

    class Meta:
        fields = ('owner_id','count')