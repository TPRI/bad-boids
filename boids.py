"""
An exercise in refactoring.

This code has been modified from a deliberately bad implementation of
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import os
import yaml

# Load initial config from initial_config.yml
INIT_CONFIG = yaml.load(open(os.path.join(os.path.dirname(__file__), 'initial_config.yml')))

NUM_BOIDS = INIT_CONFIG["num_boids"]

# Construct boids as a array of arrays
boids_x = [random.uniform(INIT_CONFIG["x_min"], INIT_CONFIG["x_min"]) for x in range(NUM_BOIDS)]
boids_y = [random.uniform(INIT_CONFIG["y_min"], INIT_CONFIG["y_min"]) for x in range(NUM_BOIDS)]
boid_x_velocities = [random.uniform(INIT_CONFIG["vx_min"], INIT_CONFIG["vx_min"]) for x in range(NUM_BOIDS)]
boid_y_velocities = [random.uniform(INIT_CONFIG["vy_min"], INIT_CONFIG["vy_min"]) for x in range(NUM_BOIDS)]
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)


# The main simulation
def update_boids(boids):

    xs, ys, xvs, yvs = boids

    # Fly towards the middle
    for i in range(len(xs)):
        for j in range(len(xs)):
            xvs[i] = xvs[i] + (xs[j] - xs[i]) * 0.01 / len(xs)
    for i in range(len(xs)):
        for j in range(len(xs)):
            yvs[i] = yvs[i] + (ys[j] - ys[i]) * 0.01 / len(xs)

    # Fly away from nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < 100:
                xvs[i] = xvs[i] + (xs[i] - xs[j])
                yvs[i] = yvs[i] + (ys[i] - ys[j])

    # Try to match speed with nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < 10000:
                xvs[i] = xvs[i] + (xvs[j] - xvs[i]) * 0.125 / len(xs)
                yvs[i] = yvs[i] + (yvs[j] - yvs[i]) * 0.125 / len(xs)

    # Move according to velocities
    for i in range(len(xs)):
        xs[i] = xs[i] + xvs[i]
        ys[i] = ys[i] + yvs[i]


# Create a plot figure
figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boids[0], boids[1])


# A function to run the simulation and update the plot
def animate(frame):
    update_boids(boids)
    scatter.set_offsets(zip(boids[0], boids[1]))

# Animate the plot
anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

# Run if module is called directly
if __name__ == "__main__":
    plt.show()
