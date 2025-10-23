classes_held = int(input("Enter total number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

attendance = (classes_attended / classes_held) * 100
status = "Eligible for exams" if attendance >= 75 else "Not eligible for exams"

print(f"Classes Held: {classes_held}")
print(f"Classes Attended: {classes_attended}")
print(f"Attendance: {attendance:.2f}%")
print(f"Status: {status}")
