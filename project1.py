import numpy as np
import pandas as pd
marks=np.array([[85, 80, 90],[70, 75, 65],[92, 88, 95],[60, 72, 68],[78, 82, 80]])
df = pd.DataFrame(marks)
print(df)
print(df.info())
total = np.sum(marks, axis=1)
print(total)
average = np.mean(marks, axis=1)
print(average)
