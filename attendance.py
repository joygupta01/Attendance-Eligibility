TotalDays = int(input("Enter total number of working days: "))
AbsentDays = int(input("Enter number of days absent: "))

AttendedDays = TotalDays - AbsentDays
percentage = (AttendedDays / TotalDays) * 100

if TotalDays > 0:
    if percentage >= 75:
        print("You are allowed to sit for the exam.")
    else:
        print("You are NOT allowed to sit for the exam.")
else:
    print("Invalid input. Total working days must be more than 0.")