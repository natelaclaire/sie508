class ProductivitySystem:
    def __init__(self):
        self._roles = {
            "general_manager": GeneralManagerRole,
            "shift_leader": ShiftLeaderRole,
            "crew_member": CrewMemberRole,
            "team_member": TeamMemberRole,
            "custodial": CustodialRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError(role_id)
        return role_type()

    def track(self, employees, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
        print("")


class GeneralManagerRole:
    def perform_duties(self, hours):
        return f"is available to deal with customers who shout 'I want to speak with your manager!' for {hours} hours."


class ShiftLeaderRole:
    def perform_duties(self, hours):
        return f"screams and yells for {hours} hours."


class CrewMemberRole:
    def perform_duties(self, hours):
        return f"expends {hours} hours making faces at customers during peak and hard to fill times."


class TeamMemberRole:
    def perform_duties(self, hours):
        return f"makes barely edible food with limited availability for {hours} hours."


class CustodialRole:
    def perform_duties(self, hours):
        return f"mops floors and cleans toilets for {hours} hours."
