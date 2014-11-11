from boids import Boids
from matplotlib import pyplot as plt
from matplotlib import animation

my_boids = Boids()

# Create a plot figure
figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(my_boids.get_boids()[0], my_boids.get_boids()[1])


# A function to run the simulation and update the plot
def animate(frame):
    my_boids.update_boids()
    scatter.set_offsets(zip(my_boids.get_boids()[0], my_boids.get_boids()[1]))

# Animate the plot
anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

# Run if module is called directly
if __name__ == "__main__":
    plt.show()