import pandas as pd
import numpy as np
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

file_path = r"C:\Users\HP\Downloads\student_marks.xlsx"  # Update if needed

df = pd.read_excel(file_path)

marks = df[['Maths', 'Science', 'English', 'History', 'Computer']].to_numpy()

avg_marks = np.mean(marks, axis=1)

highest_marks = np.max(marks, axis=0)
lowest_marks = np.min(marks, axis=0)

class_avg_subject = np.mean(marks, axis=0)

total_marks = np.sum(marks, axis=1)

sorted_indices = np.argsort(-total_marks)
rank_array = np.empty_like(sorted_indices)
rank_array[sorted_indices] = np.arange(1, len(total_marks) + 1)

top_3_indices = sorted_indices[:3]
bottom_3_indices = sorted_indices[-3:]

pass_mark = 40
pass_fail = np.where(np.all(marks >= pass_mark, axis=1), 'Pass', 'Fail')

passed_all = np.sum(pass_fail == 'Pass')

df['TotalMarks'] = total_marks
df['AverageMarks'] = avg_marks
df['Result'] = pass_fail
df['Rank'] = rank_array

output_path = "student_report.xlsx"
df.to_excel(output_path, index=False)

print("\n[✓] Analysis Complete!\n")

print("Highest marks per subject:")
for subject, mark in zip(['Maths', 'Science', 'English', 'History', 'Computer'], highest_marks):
    print(f"  {subject}: {mark}")

print("\nLowest marks per subject:")
for subject, mark in zip(['Maths', 'Science', 'English', 'History', 'Computer'], lowest_marks):
    print(f"  {subject}: {mark}")

print("\nClass average per subject:")
for subject, avg in zip(['Maths', 'Science', 'English', 'History', 'Computer'], class_avg_subject):
    print(f"  {subject}: {avg:.2f}")

print("\nTop 3 Students:")
print(df.loc[top_3_indices, ['Name', 'TotalMarks', 'Rank']])

print("\nBottom 3 Students:")
print(df.loc[bottom_3_indices, ['Name', 'TotalMarks', 'Rank']])

print(f"\nTotal students who passed all subjects: {passed_all}")
print(f"Report saved as: {output_path}")
