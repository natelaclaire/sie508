from GarageStoredVehicle import GarageStoredVehicle
from VehicleWithMotor import VehicleWithMotor


class Car(GarageStoredVehicle, VehicleWithMotor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return 'Car\n' + \
               super().__str__()