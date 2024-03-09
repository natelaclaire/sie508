from Course import Course
from UnableToEnrollOrWaitlist import UnableToEnrollOrWaitlist
from StudentAlreadyEnrolled import StudentAlreadyEnrolled
from Student import Student

# create the course
try:
    sie508 = Course("Object Oriented Programming", "SIE508", 3, 5)
except Exception as e:
    print(e)
    exit()

''' Tested Course constructor validation:
try:
    sie507 = Course("Information Systems Software Engineering", "SIE507", "3", 5)
except Exception as e:
    print(e)
    exit()'''

# create and register the students
try:
    sheldon = Student("Sheldon Cooper", 1)
    sie508.enrollStudent(sheldon)

    # try registering student a second time
    sie508.enrollStudent(sheldon)
except (StudentAlreadyEnrolled, UnableToEnrollOrWaitlist) as e:
    # print and then continue if the student is already enrolled or the waitlist is full
    print(e)
except Exception as e:
    # for any other exception, print and exit
    print(e)
    exit()

try:
    leonard = Student("Leonard Hofstadter", 2)
    sie508.enrollStudent(leonard)
except (StudentAlreadyEnrolled, UnableToEnrollOrWaitlist) as e:
    print(e)
except Exception as e:
    print(e)
    exit()

try:
    raj = Student("Rajesh Koothrappali", 3)
    sie508.enrollStudent(raj)
except (StudentAlreadyEnrolled, UnableToEnrollOrWaitlist) as e:
    print(e)
except Exception as e:
    print(e)
    exit()

try:
    howard = Student("Howard Wolowitz", 4)
    sie508.enrollStudent(howard)
except (StudentAlreadyEnrolled, UnableToEnrollOrWaitlist) as e:
    print(e)
except Exception as e:
    print(e)
    exit()

''' Tested Student constructor validation
try:
    penny = Student("Penny Hofstadter", "5")
    sie508.enrollStudent(penny)
except Exception as e:
    print(e)'''

try:
    penny = Student("Penny Hofstadter", 5)
    sie508.enrollStudent(penny)
except (StudentAlreadyEnrolled, UnableToEnrollOrWaitlist) as e:
    print(e)
except Exception as e:
    print(e)
    exit()

try:
    leslie = Student("Leslie Winkle", 6)
    sie508.enrollStudent(leslie)
except (StudentAlreadyEnrolled, UnableToEnrollOrWaitlist) as e:
    print(e)
except Exception as e:
    print(e)
    exit()

try:
    bernadette = Student("Bernadette Rostenkowski", 7)
    sie508.enrollStudent(bernadette)
except (StudentAlreadyEnrolled, UnableToEnrollOrWaitlist) as e:
    print(e)
except Exception as e:
    print(e)
    exit()

try:
    amy = Student("Amy Farrah Fowler", 8)
    sie508.enrollStudent(amy)
except (StudentAlreadyEnrolled, UnableToEnrollOrWaitlist) as e:
    print(e)
except Exception as e:
    print(e)
    exit()

# enrollment and waitlist at capacity - should fail
try:
    stuart = Student("Stuart Bloom", 9)
    sie508.enrollStudent(stuart)
except (StudentAlreadyEnrolled, UnableToEnrollOrWaitlist) as e:
    print(e)
except Exception as e:
    print(e)
    exit()


print()  # blank line to clean up the output

# check enrollment and waitlist
sie508.printEnrolledStudents()
sie508.printWaitlisted()

print()  # blank line to clean up the output

# drop one student using student object, should fail
try:
    sie508.dropStudent(leonard)
except Exception as e:
    print(e)

# drop one student using name, should succeed
try:
    sie508.dropStudent("Leonard Hofstadter")
except Exception as e:
    print(e)

# drop a previously dropped student, should fail
try:
    sie508.dropStudent("Leonard Hofstadter")
except Exception as e:
    print(e)

# drop a student who doesn't exist, should fail with the same message as above
try:
    sie508.dropStudent("Mary Cooper")
except Exception as e:
    print(e)

# testing name property validation
try:
    bernadette.name = 7
except Exception as e:
    print(e)

try:
    bernadette.name = "Bernadette Rostenkowski-Wolowitz"
except Exception as e:
    print(e)

print()  # blank line to clean up the output

# check enrollment and waitlist
sie508.printEnrolledStudents()
sie508.printWaitlisted()
