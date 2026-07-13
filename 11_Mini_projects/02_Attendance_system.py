# Attendance system project for collage:

print(" STUDENT LIST FOR MCA SECTION A 👍 ")

students = ["Mayank", "Aditya", "Abhijeet", "Bhola", "Rahul", "Niraj", "Satya", "Aplav", "Jinali", "Lokesh", "Dawlu", "Aman", "Jayant", "Rohit"]


present = 0
absent = 0

print()

for student in students:
    attendance = input(f"Enter Attendaance for {student} (present/absent): ").title()
    if attendance == "Present":
        print(student, "- Present")
        present += 1
    elif attendance == "Absent":
        print(student, "- Absent")
        absent += 1
    else:
        print("Invalid Input.")
        absent += 1
        
print ("\n" + "=" * 45)
print("         Attendance Report")
print("=" * 45)

print("Total Student :", len(students))
print("Present student", present)
print("Absebt student ", absent)

attendance_precentage = (present / len(students)) * 100
print("Attendance Percantage :",attendance_precentage, "%")

if attendance_precentage >= 75:
    print("Status : Good Attendance")
else:
    print("Status : Attendance is low")
    
print("=" *  45)
    