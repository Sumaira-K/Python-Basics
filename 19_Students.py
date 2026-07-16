with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


#using variables
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


#sorted
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)  


#using dictionary
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {} # student = {"name" : name, "house" : house}
        student["name"] = name
        student["house"] = house
        students.append(student)

def get_name(student): #same can be done for house using value=get_house
    return student["name"]

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")


#nested dictionary

#lambda function - anonymous function
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {} # student = {"name" : name, "house" : house}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")