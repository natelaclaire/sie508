class UnableToEnrollOrWaitlist(Exception):
    def __init__(self, student):
        super().__init__()
        self._student = student

    def __str__(self):
        msg = "unable to enroll or waitlist " + self._student.name + ": the enrollment and waitlist are at capacity"
        return repr(msg)
