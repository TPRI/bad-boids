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

    # The main simulation
    def update_boids(self):

        xs, ys, xvs, yvs = self.boids
    
        # Fly
        ###########

        # differences
        diff_xs = np.subtract.outer(xs, xs)
        diff_ys = np.subtract.outer(ys, ys)
        total_diff = (diff_xs ** 2 + diff_ys ** 2)
        diff_xvs = np.subtract.outer(xvs, xvs)
        diff_yvs = np.subtract.outer(yvs, yvs)

        # constants
        fly_mid_scale_avg = self.fly_mid_scale / self.num_boids
        fly_speed_match_average = self.speed_match_scale / self.num_boids

        # scaled differences
        diff_xs_fly_mid_scale_avg = diff_xs * fly_mid_scale_avg
        diff_ys_fly_mid_scale_avg = diff_ys * fly_mid_scale_avg
        diff_xvs_fly_speed_match_average = diff_xvs * fly_speed_match_average
        diff_yvs_fly_speed_match_average = diff_yvs * fly_speed_match_average

        # evaluate conditions into truth tables
        speed_match_condition_truth = np.less(total_diff, self.speed_match_condition)
        fly_away_condition_truth = np.less(total_diff, self.fly_away_condition)

        # combine differences with truth tables
        diff_xvs_fly_speed_match_average_combine = diff_xvs_fly_speed_match_average * speed_match_condition_truth
        diff_yvs_fly_speed_match_average_combine = diff_yvs_fly_speed_match_average * speed_match_condition_truth
        diff_xvs_fly_away_combine = np.transpose(diff_xs) * fly_away_condition_truth
        diff_yvs_fly_away_combine = np.transpose(diff_ys) * fly_away_condition_truth
        # TRANSPOSE MAY BE A TYPO?

        # combine all together
        # Fly towards the middle + Try to match speed with nearby boids + Fly away from nearby boids
        combined_xvs = diff_xs_fly_mid_scale_avg + diff_xvs_fly_speed_match_average_combine + diff_xvs_fly_away_combine
        combined_yvs = diff_ys_fly_mid_scale_avg + diff_yvs_fly_speed_match_average_combine + diff_yvs_fly_away_combine

        # Sum over axis 0 and augmented assignment
        xvs += np.sum(combined_xvs, axis=0)
        yvs += np.sum(combined_yvs, axis=0)

        # move
        #########

        xs += xvs
        ys += yvs

