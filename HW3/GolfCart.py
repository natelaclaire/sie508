from GarageStoredVehicle import GarageStoredVehicle
from VehicleWithMotor import VehicleWithMotor


class GolfCart(GarageStoredVehicle, VehicleWithMotor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return 'Golf Cart\n' + \
               super().__str__()