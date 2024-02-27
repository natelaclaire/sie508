from datetime import datetime
from datetime import date
from Maintenance import Maintenance


class Vehicle:
    def __init__(self, vehicle_id="", license_plate="", **kwargs):
        super().__init__(**kwargs)

        if isinstance(vehicle_id, int):
            self.__vehicle_id = vehicle_id

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

    def add_maintenance(self, maint_date="", description=""):
        # allow adding maintenance for today (no value for date), or some date in the past (using date object or string)
        if isinstance(maint_date, str) and maint_date != "":
            maint_date_obj = datetime.strptime(maint_date, '%Y-%m-%d').date()
        elif isinstance(maint_date, date):
            maint_date_obj = maint_date
        else:
            maint_date_obj = date.today()

        if isinstance(description, str):
            self.__maintenance_record.append(Maintenance(maint_date_obj, description))

    def list_maintenance(self):
        for maint in self.__maintenance_record:
            print(maint)

    def latest_maintenance(self):
        num_records = len(self.__maintenance_record)

        if num_records > 0:
            self.__maintenance_record.sort(key=Maintenance.sort_by_date)

            return self.__maintenance_record[num_records-1]
        else:
            return 'No maintenance records'

    def __str__(self):
        return 'Vehicle ID: ' + str(self.__vehicle_id) + \
               '\nLicense Plate: ' + self.__license_plate + \
               '\nLast Maintenance: ' + str(self.latest_maintenance())
