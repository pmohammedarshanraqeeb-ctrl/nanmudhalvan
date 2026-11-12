import pandas as pd
# Student feedback
data = {
    "Student_ID": [101, 102, 103, 104],
    "Department": ["CSE", "IT", "CSE", "AI&DS"],
    "Feedback": [
        "Good teaching",
        "Need more computers",
        "Good teaching",
        "Need more buses"
    ]
}
# Create DataFrame
df = pd.DataFrame(data)
# Categorize feedback
def category(feedback):
    if "teaching" in feedback.lower():
        return "Teaching"
    elif "computer" in feedback.lower():
        return "Infrastructure"
    elif "bus" in feedback.lower():
        return "Transport"
    else:
       return "Other"
df["Category"] = df["Feedback"].apply(category)
# Display feedback
print("STUDENT FEEDBACK")
print(df)
# Display summary
print("\nFEEDBACK SUMMARY")
print(df["Category"].value_counts())
