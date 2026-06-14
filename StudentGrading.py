print("Student Grading System")

students = {}

number_of_students = int(input("How many students? "))

for i in range(number_of_students):
    name = input("Enter student name: ")
    mark = float(input("Enter mark out of 100: "))
    students[name] = mark

print("Name and Grade")

for student_name in students:
    student_mark = students[student_name]

    if student_mark >= 80:
        grade = "A"
    elif student_mark >= 70:
        grade = "B"
    elif student_mark >= 60:
        grade = "C"
    elif student_mark >= 50:
        grade = "D"
    else:
        grade = "F"

    print(student_name, "-", student_mark, "-", grade)

all_marks = []
for name in students:
    all_marks.append(students[name])

print("Highest mark:", max(all_marks))
print("Lowest mark:", min(all_marks))
print("Average:", sum(all_marks) / len(all_marks))