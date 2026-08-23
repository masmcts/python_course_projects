grade = float(input("Enter grade (0-100): "))
attendance = float(input("Enter attendance percentage: "))

if grade >= 90 and attendance >= 70:
    result = "A"
elif grade >= 80 and attendance >= 70:
    result = "B"
elif grade >= 70 and attendance >= 70:
    result = "C"
elif grade >= 60 and attendance >= 70:
    result = "D"
else:
    result = "Fail"

print("Result:", result)
