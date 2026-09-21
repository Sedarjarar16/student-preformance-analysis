from ucimlrepo import fetch_ucirepo
student_performance = fetch_ucirepo(id=320)
X = student_performance.data.features
y = student_performance.data.targets
print(X.head())
print(y.head())
print(X.shape)
print(X.isnull().sum())
print(X.columns)
data = X.copy()
data["G3"] = y["G3"]
print(data[["studytime", "absences", "failures", "G3"]].head()) 
print(data.groupby("studytime")["G3"].mean())
print(data["studytime"].value_counts().sort_index())
print(student_performance.variables[student_performance.variables["name"] == "studytime"])
import matplotlib.pyplot as plt

data.groupby("studytime")["G3"].mean().plot(kind="bar")

plt.xlabel("Weekly Study Time Level")

plt.ylabel("Average Final Grade (G3)")

plt.title("Average Final Grade by Weekly Study Time")

plt.show()