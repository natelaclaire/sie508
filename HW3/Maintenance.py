from datetime import date


class Maintenance:
    def __init__(self, maintenance_date, description):
        if isinstance(maintenance_date, date):
            self.__maintenance_date = maintenance_date

        if isinstance(description, str):
            self.__description = description

    @property
    def maintenance_date(self):
        return self.__maintenance_date

    @maintenance_date.setter
    def maintenance_date(self, new_maintenance_date):
        if isinstance(new_maintenance_date, date):
            self.__maintenance_date = new_maintenance_date

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            self.__description = new_description

    def __str__(self):
        return self.__maintenance_date.strftime("%m/%d/%Y") + ': ' + self.__description

    @staticmethod
    def sort_by_date(e):
        return e.maintenance_date