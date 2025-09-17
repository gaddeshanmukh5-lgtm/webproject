# visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r"C:\Users\HP\Downloads\student_marks_advanced (1).xlsx"
df = pd.read_excel(file_path)


subjects = ["Maths", "Science", "English", "History", "Computer"]


avg_marks = df[subjects].mean()
plt.figure(figsize=(8, 5))
plt.bar(subjects, avg_marks, color="skyblue")
plt.title("Average Marks per Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()


result_counts = df["Result"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(result_counts, labels=result_counts.index, autopct="%1.1f%%", colors=["green", "red"], startangle=90)
plt.title("Pass vs Fail Students")
plt.tight_layout()
plt.show()


class_avg = df.groupby("Class")["AverageMarks"].mean()
plt.figure(figsize=(8, 5))
plt.plot(class_avg.index, class_avg.values, marker="o", linestyle="-", color="purple")
plt.title("Average Marks by Class")
plt.xlabel("Class")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["Maths"], df["Science"], color="blue", alpha=0.6)
plt.title("Maths vs Science Marks")
plt.xlabel("Maths")
plt.ylabel("Science")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
plt.hist(df["TotalMarks"], bins=10, color="orange", edgecolor="black")
plt.title("Distribution of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.heatmap(df[subjects + ["TotalMarks"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Subjects")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x="Gender", y="TotalMarks", data=df, palette="Set2")
plt.title("Total Marks by Gender")
plt.tight_layout()
plt.show()

# 8. Countplot: Number of students in each class
plt.figure(figsize=(8, 5))
sns.countplot(x="Class", data=df, palette="Set1")
plt.title("Number of Students in Each Class")
plt.tight_layout()
plt.show()

# 9. Violin plot: English marks by gender
plt.figure(figsize=(8, 5))
sns.violinplot(x="Gender", y="English", data=df, palette="muted")
plt.title("Distribution of English Marks by Gender")
plt.tight_layout()
plt.show()

# 10. Pairplot: Relationships among subjects by gender
sns.pairplot(df[subjects + ["Gender"]], hue="Gender", palette="coolwarm")
plt.suptitle("Pairplot of All Subjects by Gender", y=1.02)
plt.show()

# 11. Print insights
pass_count = result_counts.get("Pass", 0)
print("\nInsights:")
print(f"1. Highest scoring subject on average: {avg_marks.idxmax()} ({avg_marks.max():.2f})")
print(f"2. Lowest scoring subject on average: {avg_marks.idxmin()} ({avg_marks.min():.2f})")
print(f"3. Pass percentage: {(pass_count / len(df)) * 100:.2f}%")
print(f"4. Class with highest average marks: {class_avg.idxmax()} ({class_avg.max():.2f})")
print("5. Maths & Science show moderate positive correlation (students strong in one tend to do well in the other).")
