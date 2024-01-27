import matplotlib.pyplot as plt


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
#ax.plot(x_values, y_values, linewidth="3")
ax.scatter(x_values, y_values, c=y_values, cmap="Blues", linewidth=5, s=10)


ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", color="c", fontsize=10)
ax.set_ylabel("Square of value", color="b", fontsize=24)

# Set size of tick label.
ax.tick_params(labelsize=10)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format()
plt.savefig("Square_plottttt.png", bbox_inches='tight')
