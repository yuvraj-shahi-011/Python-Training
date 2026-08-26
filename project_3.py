import numpy as np
import matplotlib.pyplot as plt
dataset = np.array([
    [75, 80, 85],
    [80, 75, 90],
    [70, 95, 85]
])
total = dataset.sum(axis=1)
plt.bar(["S1", "S2", "S3"], total)
plt.title("Total Marks")
plt.show()
avg = dataset.mean(axis=0)
plt.plot(["Sub1","Sub2","Sub3"], avg, marker="o", label="Average")
plt.plot(["Sub1","Sub2","Sub3"], dataset[0], marker="o", label="S1")
plt.plot(["Sub1","Sub2","Sub3"], dataset[1], marker="o", label="S2")
plt.plot(["Sub1","Sub2","Sub3"], dataset[2], marker="o", label="S3")
plt.title("Subject Average vs Students")
plt.legend()
plt.show()