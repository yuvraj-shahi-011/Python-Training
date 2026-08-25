import numpy as np
import pandas as pd
marks=np.array([[85, 80, 90],[70, 75, 65],[92, 88, 95],[60, 72, 68],[78, 82, 80]])
total = np.sum(marks, axis=1)
print("total marks:", total)
average = np.mean(marks, axis=1)
print("student averages:", average)
subject_average = np.mean(marks, axis=0)
print("subject averages:", subject_average)
highest = np.max(marks, axis=0)
print("highest score:", highest)
lowest = np.min(marks, axis=0)
print("lowest score:", lowest)
students_above_80 = np.where(average > 80)[0]
print("students above 80:", students_above_80)
status = np.where(np.all(marks >= 40, axis=1), "pass", "fail")
print("7. pass/fail:", status)
highest_student_index = np.argmax(average)
print("highest-performing student index:", highest_student_index)
std = np.std(marks, axis=0)
print("subject standard deviation:", std)
df = pd.DataFrame({
    "student": ["student 1", "student 2", "student 3", "student 4", "student 5"],
    "subject 1": marks[:, 0],
    "subject 2": marks[:, 1],
    "subject 3": marks[:, 2],
    "total": total,
    "average": average,
    "status": status
})

print("\n final dataframe:")
print(df)
