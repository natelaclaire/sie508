from Vehicle import Vehicle


class RackStoredVehicle(Vehicle):
    def __init__(self, rack_number="", **kwargs):
        super().__init__(**kwargs)

        if isinstance(rack_number, int):
            self.__rack_number = rack_number

    @property
    def rack_number(self):
        return self.__rack_number

    @rack_number.setter
    def rack_number(self, new_rack_number):
        if isinstance(new_rack_number, int):
            self.__rack_number = new_rack_number

    def __str__(self):
        return super().__str__() + \
            '\nLocation: ' + self.location()

    def location(self):
        return 'Rack # ' + str(self.__rack_number)