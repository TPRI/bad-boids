"""
An exercise in refactoring.

This code has been modified from a deliberately bad implementation of
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import random
import os
import yaml
import numpy as np

class Boids(object):
    
    def __init__(self):
        
        # Load initial config from initial_config.yml
        INIT_CONFIG = yaml.load(open(os.path.join(os.path.dirname(__file__), 'initial_config.yml')))
        
        self.num_boids = INIT_CONFIG["num_boids"]
        self.fly_mid_scale = INIT_CONFIG["fly_mid_scale"]
        self.fly_away_condition = INIT_CONFIG["fly_away_condition"]
        self.speed_match_condition = INIT_CONFIG["speed_match_condition"]
        self.speed_match_scale = INIT_CONFIG["speed_match_scale"]
        
        # Construct boids as a array of arrays
        boids_x = [random.uniform(INIT_CONFIG["x_min"], INIT_CONFIG["x_max"]) for x in range(self.num_boids)]
        boids_y = [random.uniform(INIT_CONFIG["y_min"], INIT_CONFIG["y_max"]) for x in range(self.num_boids)]
        boid_x_velocities = [random.uniform(INIT_CONFIG["vx_min"], INIT_CONFIG["vx_max"]) for x in range(self.num_boids)]
        boid_y_velocities = [random.uniform(INIT_CONFIG["vy_min"], INIT_CONFIG["vy_max"]) for x in range(self.num_boids)]
        self.boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

        # Convert to numpy arrays
        boids_x = np.array(boids_x)
        boids_y = np.array(boids_y)
        boid_x_velocities = np.array(boid_x_velocities)
        boid_y_velocities = np.array(boid_y_velocities)
        self.boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

    # Fly towards the middle
    def fly_mid(self, xs, xvs, ys, yvs):
        for i in range(self.num_boids):
            for j in range(self.num_boids):
                xvs[i] += (xs[j] - xs[i]) * self.fly_mid_scale / self.num_boids
                yvs[i] += (ys[j] - ys[i]) * self.fly_mid_scale / self.num_boids
    # Fly away from nearby boids
    def fly_away(self, xs, xvs, ys, yvs):
        for i in range(self.num_boids):
            for j in range(self.num_boids):
                if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < self.fly_away_condition:
                    xvs[i] = xvs[i] + (xs[i] - xs[j])
                    yvs[i] = yvs[i] + (ys[i] - ys[j])

    # Try to match speed with nearby boids
    def fly_speed_match(self, xs, xvs, ys, yvs):
        for i in range(self.num_boids):
            for j in range(self.num_boids):
                if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < self.speed_match_condition:
                    xvs[i] += (xvs[j] - xvs[i]) * self.speed_match_scale / self.num_boids
                    yvs[i] += (yvs[j] - yvs[i]) * self.speed_match_scale / self.num_boids

    # Move according to velocities
    def move(self, xs, xvs, ys, yvs):
        xs += xvs
        ys += yvs

    # The main simulation
    def update_boids(self):
    
        xs, ys, xvs, yvs = self.boids
    
        # Fly towards the middle
        self.fly_mid(xs, xvs, ys, yvs)
        # Fly away from nearby boids
        self.fly_away(xs, xvs, ys, yvs)
        # Try to match speed with nearby boids
        self.fly_speed_match(xs, xvs, ys, yvs)
        # Move according to velocities
        self.move(xs, xvs, ys, yvs)

