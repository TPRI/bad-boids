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

    # Fly
    def fly(self, xs, xvs, ys, yvs):

        # differences
        diff_xs = np.subtract.outer(xs, xs)
        diff_ys = np.subtract.outer(ys, ys)
        total_diff = (diff_xs ** 2 + diff_ys ** 2)
        diff_xvs = np.subtract.outer(xvs, xvs)
        diff_yvs = np.subtract.outer(yvs, yvs)

        fly_mid_scale_avg = self.fly_mid_scale / self.num_boids
        fly_speed_match_average = self.speed_match_scale / self.num_boids


        for i in range(self.num_boids):
            for j in range(self.num_boids):
                # Fly towards the middle
                xvs[i] += diff_xs[j, i] * fly_mid_scale_avg
                yvs[i] += diff_ys[j, i] * fly_mid_scale_avg
                # Try to match speed with nearby boids
                if total_diff[j, i] < self.speed_match_condition:
                    xvs[i] += diff_xvs[j, i] * fly_speed_match_average
                    yvs[i] += diff_yvs[j, i] * fly_speed_match_average
                    # Fly away from nearby boids
                    if total_diff[j, i] < self.fly_away_condition:
                        xvs[i] += diff_xs[i, j]
                        yvs[i] += diff_ys[i, j]


    # Move according to velocities
    def move(self, xs, xvs, ys, yvs):
        xs += xvs
        ys += yvs

    # The main simulation
    def update_boids(self):
    
        xs, ys, xvs, yvs = self.boids
    
        # Fly
        self.fly(xs, xvs, ys, yvs)
        # Move according to velocities
        self.move(xs, xvs, ys, yvs)

