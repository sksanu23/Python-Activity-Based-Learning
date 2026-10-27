
# Case 41: Classroom Occupancy Analysis

rooms = ["Room A", "Room B", "Room C"]
sessions = ["Morning", "Afternoon", "Evening"]
attendance = []

for room in rooms:
    row = []
    print("\nEnter attendance for", room)

    for session in sessions:
        count = int(input(session + ": "))
        row.append(count)

    attendance.append(row)

totals = []

print("\n--- CLASSROOM REPORT ---")

for i in range(len(rooms)):
    total = sum(attendance[i])
    average = total / len(sessions)
    totals.append(total)

    print(rooms[i], "Total:", total,
          "Average:", round(average, 2))

top = totals.index(max(totals))
print("Highest attendance:", rooms[top])
print("Total attendance:", sum(totals))
