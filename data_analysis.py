import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Program started")

# Read the CSV file
df = pd.read_csv(r"C:\Users\dhanalakshmi\OneDrive\Documents\DataAnalysisProject\students.csv")


print("\nDataset:")
print(df)

# Calculate average of Marks column
average_marks = df["Marks"].mean()
print("\nAverage Marks:", average_marks)

# Bar chart
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Students")
plt.show()

# Scatter plot
plt.scatter(df["Age"], df["Marks"])
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Age vs Marks")
plt.show()

# Heatmap (correlation)
numeric_df = df[["Age", "Marks"]]
correlation = numeric_df.corr()

sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()


print("Program ended")
