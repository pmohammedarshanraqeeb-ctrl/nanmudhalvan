students = [
    {"id": 101, "name": "Arun", "attendance": 90, "marks": 85},
    {"id": 102, "name": "Bala", "attendance": 65, "marks": 70},
    {"id": 103, "name": "Divya", "attendance": 72, "marks": 92},
    {"id": 104, "name": "Ravi", "attendance": 95, "marks": 88}
]
print("STUDENT DETAILS")
for s in students:
    print(s["id"], s["name"])
print("\nATTENDANCE ALERTS")
for s in students:
    if s["attendance"] < 75:
        print("Alert:", s["name"],
              "has low attendance:", s["attendance"], "%")
print("\nSTUDENT PERFORMANCE DASHBOARD")
for s in students:
    print(s["name"],
          "Attendance:", s["attendance"],
          "Marks:", s["marks"])


