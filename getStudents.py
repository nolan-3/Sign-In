import csv
# Returns the list of students who have the given free period first

class Student:
    def __init__(self, grade, signedIn = False):
        self.grade = grade
        self.signedIn = signedIn

def getStudents(period):
    students = {}
    nameIndex = 1
    gradeIndex = 2
    periodIndex = 3
    with open("students.csv", 'r') as nameFile:
        # creating a csv reader object
        csvreader = csv.reader(nameFile)

        # extracting field names through first row,
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            free = row[periodIndex]
            if free == period:
                name = row[nameIndex]
                grade = row[gradeIndex]
                students[name] = Student(grade)
    return students
