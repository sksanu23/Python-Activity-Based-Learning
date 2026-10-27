
# Case 58: Library Borrowing and Fine Reconciliation

fine_rate = 5
total_fine = 0

for book in range(1, 4):
    days = int(input("Enter overdue days for book: "))

    fine = days * fine_rate
    total_fine = total_fine + fine

    print("Book", book, "Fine: Rs.", fine)

print("\nTotal library fine: Rs.", total_fine)
