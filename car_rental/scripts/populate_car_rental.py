import os
import sys
import django
import pprint
from collections import defaultdict
from pathlib import Path
import csv
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_rental.settings')
django.setup()
from america_car_renting.models import *
#build the right file path
data_file = os.path.join(BASE_DIR, 'data\CarRentalData_cleaned.csv')

#create empty container for temporary data storage
vehicle = defaultdict(dict)
state = set()
city = set()
vehicle_owner = set()

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        state.add(row[6])
        vehicle[row[0]] = row[1:6] + row[7:13]
        city.add((row[5],row[6]))
        vehicle_owner.add(row[7])

#clear database for initialization
Vehicle.objects.all().delete()
Vehicle_owner.objects.all().delete() 
City.objects.all().delete()
State.objects.all().delete()

state_rows = {}
city_rows = {}
vehicle_rows = {}
vehicle_owner_rows = {}

for item in state:
    row = State.objects.create(state_name=item)
    row.save()
    state_rows[item]=row

for item in city:
    row = City.objects.create(city_name=item[0],state=state_rows[item[1]])
    row.save()
    city_rows[item[0]]=row
    
for item in vehicle_owner:
    row = Vehicle_owner.objects.create(owner_id = item)
    row.save()
    vehicle_owner_rows[item] = row

for vehicle_id,data in vehicle.items():
    row = Vehicle.objects.create(vehicle_id =vehicle_id,
                                    fuel_type=data[0],
                                    ranking = data[1],
                                    renter_trips_taken = data[2],
                                     review_count = data[3],
                                     rate_daily = data[6],
                                     vehicle_make = data[7],
                                     vehicle_model = data[8],
                                     vehicle_type = data[9],
                                     vehicle_year = data[10],
                                     city = city_rows[data[4]],
                                     vehicle_owner = vehicle_owner_rows[data[5]])
    row.save()
    vehicle_rows[vehicle_id] = row

pprint.pprint(state_rows)
pprint.pprint(city_rows)
pprint.pprint(vehicle_owner_rows)
pprint.pprint(vehicle_rows)
