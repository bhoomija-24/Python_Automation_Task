import pandas as pd

# Read CSV file
data = pd.read_csv("students.csv")

print("Student Dataset")
print(data)

print("\nTotal Students:", len(data))

print("\nAverage Marks:", data["Marks"].mean())

print("Highest Marks:", data["Marks"].max())

print("Lowest Marks:", data["Marks"].min())

print("\nSummary Statistics")
print(data.describe())

print("\nStudents Department-wise")
print(data.groupby("Department")["Marks"].mean())