
# Case 30: Student Email and Identifier Validation

email = input("Enter student email: ")
student_id = input("Enter student ID: ")

if "@" in email and "." in email and " " not in email:
    print("Valid email")
else:
    print("Invalid email")

if (student_id.startswith("STU")
        and len(student_id) == 6
        and student_id[3:].isdigit()):
    print("Valid student ID")
else:
    print("Invalid student ID")
