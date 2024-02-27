from GarageStoredVehicle import GarageStoredVehicle
from VehicleWithMotor import VehicleWithMotor


class MotorBike(GarageStoredVehicle, VehicleWithMotor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return 'Motor Bike\n' + \
               super().__str__()