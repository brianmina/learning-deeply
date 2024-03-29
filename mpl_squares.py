import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]


# Adding a style
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.scatter(2, 4, edgecolor="r", facecolor="g", linewidth=2, s=200)


# set a chart title and label axes.
ax.set_title("Square Number", loc="center", color="c", fontsize=24)
ax.set_xlabel("Value", color="c", fontstyle="normal", loc="right", fontsize=14)
ax.set_ylabel("Square of value",color="b", fontsize=24)

# Set size of thick labels.
ax.tick_params(labelcolor="r", labelsize=10)

plt.show()



