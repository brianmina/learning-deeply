import matplotlib.pyplot as plt


x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth="6")
ax.scatter(x_values, y_values, edgecolor="r", linewidth=2, s=200)
ax.set_title("Square Number", loc="center", color="c", fontsize=24)
ax.set_xlabel("Value", color="c", fontstyle="normal", loc="right", fontsize=14)
ax.set_ylabel("Square of value",color="b", fontsize=24)

plt.show()