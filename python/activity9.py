
# Case 46: Inventory Matrix Reconciliation

items = ["Books", "Pens", "Bags", "Pencils"]

for item in items:
    print("\nItem:", item)

    recorded = int(input("Recorded stock: "))
    actual = int(input("Actual stock: "))

    difference = actual - recorded

    print("Difference:", difference)

    if difference == 0:
        print("Stock matches")
    elif difference < 0:
        print("Missing stock:", abs(difference))
    else:
        print("Extra stock:", difference)

print("\nInventory checking completed.")
