from Vehicle import Vehicle


class VehicleWithMotor(Vehicle):
    def __init__(self, fuel_type="", fuel_level="", **kwargs):
        super().__init__(**kwargs)

        if isinstance(fuel_type, str):
            self.__fuel_type = fuel_type

        if isinstance(fuel_level, float):
            self.__fuel_level = fuel_level

    @property
    def fuel_level(self):
        return self.__fuel_level

    @fuel_level.setter
    def fuel_level(self, new_fuel_level):
        if isinstance(new_fuel_level, float):
            self.__fuel_level = new_fuel_level

    @property
    def fuel_type(self):
        return self.__fuel_level

    @fuel_type.setter
    def fuel_type(self, new_fuel_type):
        if isinstance(new_fuel_type, str):
            self.__fuel_type = new_fuel_type

    def __str__(self):
        return super().__str__() + \
            '\nFuel Type: ' + self.__fuel_type + \
            '\nFuel Level: ' + "{:.0%}".format(self.__fuel_level)