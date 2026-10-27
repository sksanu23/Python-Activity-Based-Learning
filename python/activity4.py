
# Student Marks Matrix Analysis

students = ["Anu", "Balu", "Charan"]
subjects = ["Python", "Maths", "English"]
marks = []

# Input marks
for student in students:
    row = []
    print("\nEnter marks for", student)

    for subject in subjects:
        mark = int(input(subject + ": "))
        row.append(mark)

    marks.append(row)

# Display student results
print("\n--- STUDENT REPORT ---")

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("\nStudent:", students[i])
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)

# Find the highest total
totals = []

for row in marks:
    totals.append(sum(row))

top = totals.index(max(totals))

print("\nTop Student:", students[top])
print("Highest Total:", totals[top])