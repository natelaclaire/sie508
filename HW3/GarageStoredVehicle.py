from Vehicle import Vehicle


class GarageStoredVehicle(Vehicle):
    def __init__(self, bay_number="", **kwargs):
        super().__init__(**kwargs)

        if isinstance(bay_number, int):
            self.__bay_number = bay_number

    @property
    def bay_number(self):
        return self.__bay_number

    @bay_number.setter
    def bay_number(self, new_bay_number):
        if isinstance(new_bay_number, int):
            self.__bay_number = new_bay_number

    def __str__(self):
        return super().__str__() + \
            '\nLocation: ' + self.location()

    def location(self):
        return 'Bay # ' + str(self.__bay_number)
