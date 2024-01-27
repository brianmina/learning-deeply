import matplotlib.pyplot as plt

x_cubes = list(range(1, 5001))
y_cubes = [value**3 for value in range(1, 5001)]
print(y_cubes)

fig, ax = plt.subplots()
ax.scatter(x_cubes, y_cubes, c=y_cubes, cmap="Blues")


ax.set_title("Cubes_5", loc='right', color="b")
ax.set_xlabel("Axis X")
ax.set_ylabel("Axis Y")

ax.tick_params(labelsize=9)
plt.show()

plt.
