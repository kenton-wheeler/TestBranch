# Program to calculate a student's alphabetic grade
# based on their numeric mark
mark = int(input("What was the student's assessment mark (0-100)?"))
if mark >= 0 and mark <= 39:
    grade = 'F'
elif 40<=mark<=49:
    grade = 'D'
elif 50 <= mark <= 59:
    grade = 'C'
elif 60 <= mark <= 69:
    grade = 'B'
elif 70 <= mark <= 100:
    grade = 'A'
else:
#   handle invalid mark
    grade = "invalid (mark must be between 0 and 100)"
print("The student's grade is",grade)


