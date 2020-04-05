friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friends_ages["Adam"])

friends_ages["Rolf"] = 20

print(friends_ages["Rolf"])

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]

print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("No student found")
