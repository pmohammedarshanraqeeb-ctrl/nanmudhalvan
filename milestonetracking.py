tasks = [
    ["Design",  "Completed"],
    ["Testing", "Pending"],
    ["Coding",  "Pending"]
]
print("PROJECT MILESTONE TRACKER")
for task in tasks:
    print("\nTask:", task[0])
    if task[1] == "Completed":
        print("Status: Completed")
    else:
        print("Status: Overdue")
        print("Alert: Notify Staff")
