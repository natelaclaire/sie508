from Student import Student


class Course:
    def __init__(self, class_name, class_number, enrollment_capacity, waitlist_capacity):
        self.__class_name = class_name
        self.__class_number = class_number
        self.__enrollment_capacity = enrollment_capacity
        self.__waitlist_capacity = waitlist_capacity
        self.__enrolled = []
        self.__waitlist = []

    @property
    def class_name(self):
        return self.__class_name

    @class_name.setter
    def class_name(self, new_class_name):
        if isinstance(new_class_name, str):
            self.__class_name = new_class_name

    @property
    def class_number(self):
        return self.__class_number

    @class_number.setter
    def class_number(self, new_class_number):
        if isinstance(new_class_number, str):
            self.__class_number = new_class_number

    @property
    def enrollment_capacity(self):
        return self.__enrollment_capacity

    @enrollment_capacity.setter
    def enrollment_capacity(self, new_enrollment_capacity):
        if isinstance(new_enrollment_capacity, int):
            self.__enrollment_capacity = new_enrollment_capacity

    @property
    def waitlist_capacity(self):
        return self.__waitlist_capacity

    @waitlist_capacity.setter
    def waitlist_capacity(self, new_waitlist_capacity):
        if isinstance(new_waitlist_capacity, int):
            self.__waitlist_capacity = new_waitlist_capacity

    # determines the index of the named student in the enrollment list
    # or -1 if the student isn't enrolled
    def enrolledIndex(self, student_name):
        index = -1

        if isinstance(student_name, str):
            for i in range(0, len(self.__enrolled)):
                if self.__enrolled[i].name == student_name:
                    index = i

        return index

    # checks to see if enrollment is at capacity
    def atEnrollmentCapacity(self):
        at_capacity = False

        if len(self.__enrolled) == self.__enrollment_capacity:
            at_capacity = True

        return at_capacity

    # checks to see if waitlist is at capacity
    def atWaitlistCapacity(self):
        at_capacity = False

        if len(self.__waitlist) == self.__waitlist_capacity:
            at_capacity = True

        return at_capacity

    # fill the enrollment from the waitlist, unless waitlist is exhausted before
    # enrollment is filled; this is used by dropStudent() but is generic enough to
    # also be used if the enrollment capacity were increased
    def enrollFromWaitlist(self):
        while not self.atEnrollmentCapacity() and len(self.__waitlist) != 0:
            student = self.__waitlist.pop(0)
            self.__enrolled.append(student)
            print("Enrolled", student.name, "from waitlist")

    # enroll the provided student, assuming the student isn't enrolled and there
    # is space in the class; waitlist if the class is at capacity and there is room
    # in the waitlist; report that the student couldn't be enrolled or waitlisted
    # otherwise
    def enrollStudent(self, student):
        if isinstance(student, Student):
            if self.enrolledIndex(student.name) == -1:
                if not self.atEnrollmentCapacity():
                    self.__enrolled.append(student)
                    print("Enrolled", student.name)
                elif not self.atWaitlistCapacity():
                    self.__waitlist.append(student)
                    print("Waitlisted", student.name)
                else:
                    print("Unable to enroll or waitlist", student.name)

    # drop the named student and enroll the next from the waitlist
    def dropStudent(self, name):
        if isinstance(name, str):
            student_index = self.enrolledIndex(name)

            if student_index != -1:
                self.__enrolled.pop(student_index)
                print("Dropped", name)

        self.enrollFromWaitlist()

    # output the list of enrolled students
    def printEnrolledStudents(self):
        print("Enrolled:")

        for s in self.__enrolled:
            s.whoami()

    # output the list of waitlisted students
    def printWaitlisted(self):
        print("Waitlisted:")

        for s in self.__waitlist:
            s.whoami()
