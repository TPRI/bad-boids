"""
An exercise in refactoring.

This code has been modified from a deliberately bad implementation of
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import random
import os
import yaml
from boid import Boid


class Boids(object):
    
    def __init__(self):
        
        # Load initial config from initial_config.yml
        config = yaml.load(open(os.path.join(os.path.dirname(__file__), 'initial_config.yml')))
        
        self.num_boids = config["num_boids"]
        self.fly_mid_scale = config["fly_mid_scale"]
        self.fly_away_condition = config["fly_away_condition"]
        self.speed_match_condition = config["speed_match_condition"]
        self.speed_match_scale = config["speed_match_scale"]

        # Construct boids as a array of arrays
        self.boids = [Boid(random.uniform(config['x_min'], config['x_max']),
                           random.uniform(config['y_min'], config['y_max']),
                           random.uniform(config['vx_min'], config['vx_max']),
                           random.uniform(config['vy_min'], config['vy_max'])) for x in range(self.num_boids)]

    # Fly towards the middle
    def fly_mid(self):
        for boid_i in self.boids:
            for boid_j in self.boids:
                boid_i.fly_mid(boid_j)

    # Fly away from nearby boids
    def fly_away(self):
        for boid_i in self.boids:
            for boid_j in self.boids:
                boid_i.fly_away(boid_j)

    # Try to match speed with nearby boids
    def fly_speed_match(self):
        for boid_i in self.boids:
            for boid_j in self.boids:
                boid_i.fly_speed_match(boid_j)

    # Move according to velocities
    def move(self):
        for boid_i in self.boids:
            boid_i.move()

    # Temp: get x coordinates
    def get_x_coordinates(self):
        return [self.boids[i].x for i in range(self.num_boids)]

    # Temp: get y coordinates
    def get_y_coordinates(self):
        return [self.boids[i].y for i in range(self.num_boids)]

    # The main simulation
    def update_boids(self):

        # Fly towards the middle
        self.fly_mid()
        # Fly away from nearby boids
        self.fly_away()
        # Try to match speed with nearby boids
        self.fly_speed_match()
        # Move according to velocities
        self.move()
