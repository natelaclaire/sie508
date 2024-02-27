from datetime import date

from Maintenance import Maintenance


class Vehicle:
    def __init__(self, vehicle_id, license_plate, ev):
        if isinstance(vehicle_id, int):
            self.__vehicle_id = vehicle_id

        if isinstance(ev, bool):
            self.__ev = ev

        self.__license_plate = license_plate

        self.__maintenance_record = list()

    @property
    def vehicle_id(self):
        return self.__vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, new_vehicle_id):
        if isinstance(new_vehicle_id, int):
            self.__vehicle_id = new_vehicle_id

    @property
    def license_plate(self):
        return self.__license_plate

    @license_plate.setter
    def license_plate(self, new_license_plate):
        if isinstance(new_license_plate, str):
            self.__license_plate = new_license_plate

    @property
    def ev(self):
        return self.__ev

    @ev.setter
    def ev(self, new_ev):
        if isinstance(new_ev, str):
            self.__ev = new_ev

    def add_maintenance(self, description):
        if isinstance(description, str):
            self.__maintenance_record.append(Maintenance(date.today(), description))

    def list_maintenance(self):
        for maint in self.__maintenance_record:
            print(maint)