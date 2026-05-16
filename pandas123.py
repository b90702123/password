import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "sales": [120, 150, 170, 160, 190, 220],
    "cost": [80, 90, 100, 95, 110, 130]
}

df = pd.DataFrame(data)

print(df.head())

plt.figure(figsize=(8, 4))
plt.plot(df["month"], df["sales"], marker="o", label="sales")
plt.plot(df["month"], df["cost"], marker="o", label="cost")
plt.title("Monthly Sales and Cost")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
sns.barplot(data=df, x="month", y="sales", color="steelblue")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
sns.scatterplot(data=df, x="cost", y="sales", s=100)
plt.title("Cost vs Sales")
plt.xlabel("Cost")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()