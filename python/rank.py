students = [
    {"name": "Evan", "math": 85, "science": 90},
    {"name": "John", "math": 45, "science": 60},
    {"name": "Mary", "math": 95, "science": 92},
    {"name": "Peter", "math": 55, "science": 48},
    {"name": "Sarah", "math": 78, "science": 88}
]

average = 0

for student in students:
    average = (student['math'] + student['science'])/2
    print(f"average for {student['name']} is {average}")

for passed in students:
    if passed['math'] >= 50 and passed['science'] >= 50:
        print(f"{passed['name']} passed")
    else:
        print(f"{passed['name']} failed")




check = all(student['math'] >= 50 and student['science'] >= 50 for student in students)
if check == False:
    print("no 100% pass rate")
else:
    print("100% pass rate")

#rankings
sortted = sorted(
    students,
    key=lambda student: student['math'] and student['science'],
    reverse=True
)
number = 1
for student in sortted:
    print(f"{number} {student['name']}")
    number += 1