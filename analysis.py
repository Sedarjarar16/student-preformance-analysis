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
data["G1"] = y["G1"]
data["G2"] = y["G2"]
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
print(data[["absences", "G3"]].head(10))
print(data.groupby("absences")["G3"].mean())
plt.scatter(data["absences"], data["G3"])

plt.xlabel("Number of Absences")
plt.ylabel("Final Grade (G3)")
plt.title("Absences vs Final Grade")

plt.show()
print(data["absences"].corr(data["G3"]))
print(data.groupby("failures")["G3"].mean())
print(data["absences"].corr(data["G3"]))

data.groupby("failures")["G3"].mean().plot(kind="bar")

plt.xlabel("Number of Previous Failures")
plt.ylabel("Average Final Grade (G3)")
plt.title("Average Final Grade by Previous Failures")

plt.show()

print(data.groupby("studytime")["G3"].agg(["count", "mean"]))
print("G1 vs G3:", data["G1"].corr(data["G3"]))
print("G2 vs G3:", data["G2"].corr(data["G3"]))