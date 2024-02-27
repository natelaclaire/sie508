from datetime import date
from Bicycle import Bicycle
from GolfCart import GolfCart
from Car import Car
from MotorBike import MotorBike
from VehiclePark import VehiclePark

vehicles = VehiclePark()

bicycle1 = Bicycle(rack_number=1, vehicle_id=1, license_plate="LUV VACA 1")
bicycle1.add_maintenance(maint_date='2024-02-25', description='Replaced chain')
bicycle1.add_maintenance(description='Repaired tire')
vehicles.append(bicycle1)

motorbike1 = MotorBike(bay_number=103, vehicle_id=2, license_plate="LUV VACA 2", fuel_type="Electric", fuel_level=0.75)
motorbike1.add_maintenance(maint_date=date(2023, 12, 31), description="Replaced battery")
vehicles.append(motorbike1)

motorbike2 = MotorBike(bay_number=101, vehicle_id=3, license_plate="LUV VACA 3", fuel_type="Gas", fuel_level=1.0)
vehicles.append(motorbike2)

golfcart1 = GolfCart(bay_number=201, vehicle_id=4, license_plate="LUV VACA 4", fuel_type="Gas", fuel_level=0.33)
vehicles.append(golfcart1)

golfcart2 = GolfCart(bay_number=202, vehicle_id=5, license_plate="LUV VACA 5", fuel_type="Gas", fuel_level=0.91)
vehicles.append(golfcart2)

car1 = Car(bay_number=301, vehicle_id=6, license_plate="LUV VACA 6", fuel_type="Electric", fuel_level=1.00)
vehicles.append(car1)

vehicles.list()

# Testing the search function
# search_string = 'LUV'
# found_vehicles = vehicles.search(search_string)
# print('\n\nSearch Results for License Plate with ' + search_string + ':')
# print('-----')
# for v in found_vehicles:
#     print(v)
#     print('-----')
