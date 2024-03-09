class Student:
    def __init__(self, name, student_id):
        if not isinstance(name, str) or not isinstance(student_id, int):
            raise TypeError("student ID must be an integer and student name must be a string")
        else:
            self.__name = name
            self.__student_id = student_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("student name must be a string")
        else:
            self.__name = new_name

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, new_student_id):
        if not isinstance(new_student_id, int):
            raise TypeError("student ID must be an integer")
        else:
            self.__student_id = new_student_id

    def whoami(self):
        print("Student Id: ", self.__student_id, ", Student Name: ", self.__name, sep="")
