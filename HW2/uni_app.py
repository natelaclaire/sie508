from Course import Course
from Student import Student

# create the course
sie508 = Course("Object Oriented Programming", "SIE508", 3, 5)

# create the students
sheldon = Student("Sheldon Cooper", 1)
leonard = Student("Leonard Hofstadter", 2)
raj = Student("Rajesh Koothrappali", 3)
howard = Student("Howard Wolowitz", 4)

# attempt to enroll the students
sie508.enrollStudent(sheldon)
sie508.enrollStudent(leonard)
sie508.enrollStudent(raj)
sie508.enrollStudent(howard)

print()  # blank line to clean up the output

# check enrollment and waitlist
sie508.printEnrolledStudents()
sie508.printWaitlisted()

print()  # blank line to clean up the output

# drop one student
sie508.dropStudent("Leonard Hofstadter")

print()  # blank line to clean up the output

# check enrollment and waitlist
sie508.printEnrolledStudents()
sie508.printWaitlisted()
