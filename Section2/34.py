student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))


# print(student.average())


class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 90, 93, 78, 90)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student()
print(student.name)
print(student.grades)
print(student.average_grade())


class Student2:
    def __init__(self, name, *args):
        self.name = name
        self.grades = (args)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student2 = Student2("Pepe", 80, 85, 90, 90, 90)
student3 = Student2("Antonio", 80, 100, 100, 90, 90)
print(student2.name)
print(student2.grades)
print(student2.average_grade())
print(student3.name)
print(student3.grades)
print(student3.average_grade())
