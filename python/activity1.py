
# Case Study 25: Progressive Water Tariff Analysis

while True:
    try:
        units = int(input("Enter water consumption in units: "))
        if units >= 0:
            break
        print("Consumption cannot be negative.")
    except ValueError:
        print("Enter a valid whole number.")

if units <= 10:
    bill = units * 5
elif units <= 20:
    bill = 10 * 5 + (units - 10) * 8
else:
    bill = 10 * 5 + 10 * 8 + (units - 20) * 12

print("\n--- WATER BILL ---")
print("Water consumption:", units, "units")
print("Total bill: Rs.", format(bill, ".2f"))
