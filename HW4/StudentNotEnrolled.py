class StudentNotEnrolled(Exception):
    def __init__(self, student_name):
        super().__init__()
        self._value = student_name

    def __str__(self):
        msg = self._value + " is not enrolled for the course"
        return repr(msg)
