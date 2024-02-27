from RackStoredVehicle import RackStoredVehicle


class Bicycle(RackStoredVehicle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return 'Bicycle\n' + \
               super().__str__()