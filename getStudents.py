import csv
# Returns the list of students who have the given free period first


def getStudents(period):
    students = []
    nameIndex = 1
    periodIndex = 3
    with open("data.csv", 'r') as nameFile:
        # creating a csv reader object
        csvreader = csv.reader(nameFile)

        # extracting field names through first row,
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            free = row[periodIndex]
            if free == period:
                name = row[nameIndex]
                students.append(name)
    return students
