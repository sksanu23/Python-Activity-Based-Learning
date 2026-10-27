
# Weekly Electricity Consumption Matrix

houses = ["House A", "House B", "House C"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
data = []

# Input electricity consumption
for house in houses:
    row = []
    print("\nEnter units for", house)

    for day in days:
        units = float(input(day + ": "))
        row.append(units)

    data.append(row)

# Display weekly totals
totals = []

print("\n--- WEEKLY REPORT ---")

for i in range(len(houses)):
    total = sum(data[i])
    average = total / 7
    totals.append(total)

    print(houses[i], "Total:", total, "Average:", round(average, 2))

# Find highest and lowest consumption
print("Highest consumption:", houses[totals.index(max(totals))])
print("Lowest consumption:", houses[totals.index(min(totals))])
print("Total units used:", sum(totals), "kWh")
