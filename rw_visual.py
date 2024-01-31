import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:

    # make a random walk.
    rw = RandomWalk(500)
    rw.fill_walk()

    # Plot the point in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    print(point_numbers)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect("equal")

    # Emphasize the first and last points.
    #ax.plot(0, 0, c="green", edgecolor="none", s=100)
    #ax.plot(rw.x_values[-1], rw.y_values[-1], c="red", edgecolor="none", s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


