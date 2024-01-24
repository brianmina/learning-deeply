import matplotlib.pyplot as plt


plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(2, 4, edgecolor="r", facecolor="g", linewidth=2, s=200)

ax.set_title("Square Number", loc="center", color="c", fontsize=24)
ax.set_xlabel("Value", color="c", fontstyle="normal", loc="right", fontsize=14)
ax.set_ylabel("Square of value",color="b", fontsize=24)

plt.show()