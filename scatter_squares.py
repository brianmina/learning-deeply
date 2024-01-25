import matplotlib.pyplot as plt


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth="3")
ax.scatter(x_values, y_values, edgecolor="r", linewidth=2, s=20)


ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", color="c", fontsize=14)
ax.set_ylabel("Square of value", color="b", fontsize=24)

ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_00])
ax.tick_params(labelsize=14)
plt.show()
