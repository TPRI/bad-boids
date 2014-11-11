"""
An exercise in refactoring.

This code has been modified from a deliberately bad implementation of
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from boids import Boids
from matplotlib import pyplot as plt
from matplotlib import animation
import yaml
import os

# Load plot config from plot_config.yml
plot_config = yaml.load(open(os.path.join(os.path.dirname(__file__), 'plot_config.yml')))
xlim_max = plot_config["xlim_max"]
xlim_min = plot_config["xlim_min"]
ylim_max = plot_config["ylim_max"]
ylim_min = plot_config["ylim_min"]
framesT = plot_config["frames"]
intervalT = plot_config["interval"]

# Create a Boid object (ie a flock of boids)
my_boids = Boids()

# Create a plot figure
figure = plt.figure()
axes = plt.axes(xlim=(xlim_min, xlim_max), ylim=(ylim_min, ylim_max))
scatter = axes.scatter(my_boids.get_boids()[0], my_boids.get_boids()[1])


# A function to run the simulation and update the plot
def animate(frame):
    my_boids.update_boids()
    scatter.set_offsets(zip(my_boids.get_boids()[0], my_boids.get_boids()[1]))

# Animate the plot
anim = animation.FuncAnimation(figure, animate, frames=framesT, interval=intervalT)

# Run if module is called directly
if __name__ == "__main__":
    plt.show()