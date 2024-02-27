class VehiclePark(list):
    # add (append) and remove methods are provided by list
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def list(self):
        print('-----')
        for vehicle in self:
            print(vehicle)
            print('-----')

    def search(self, license_plate):
        matching_vehicles = []
        for vehicle in self:
            if license_plate in vehicle.license_plate:
                matching_vehicles.append(vehicle)
        return matching_vehicles
