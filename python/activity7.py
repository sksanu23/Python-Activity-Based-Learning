
# Case 37: Nested Loop Calendar Generator

days = int(input("Enter days in month (28-31): "))
start = int(input("Enter starting weekday (Mon=0, Sun=6): "))

if 28 <= days <= 31 and 0 <= start <= 6:
    print("\nMon Tue Wed Thu Fri Sat Sun")

    for i in range(start):
        print("    ", end="")

    for date in range(1, days + 1):
        print(f"{date:3}", end=" ")

        if (date + start) % 7 == 0:
            print()

    print()
else:
    print("Invalid input")

