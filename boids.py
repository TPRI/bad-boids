"""
An exercise in refactoring.

This code has been modified from a deliberately bad implementation of
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import random
import os
import yaml


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
        self.boids = [{'boid_label': x,
                       'x': random.uniform(INIT_CONFIG['x_min'], INIT_CONFIG['x_max']),
                       'y': random.uniform(INIT_CONFIG['y_min'], INIT_CONFIG['y_max']),
                       'vx': random.uniform(INIT_CONFIG['vx_min'], INIT_CONFIG['vx_max']),
                       'vy': random.uniform(INIT_CONFIG['vy_min'], INIT_CONFIG['vy_max'])} for x in range(self.num_boids)]

    # Fly towards the middle
    def fly_mid(self):
        for i in range(self.num_boids):
            for j in range(self.num_boids):
                self.boids[i]['vx'] += (self.boids[i]['x'] - self.boids[i]['x']) * self.fly_mid_scale / self.num_boids
                self.boids[i]['vy'] += (self.boids[j]['y'] - self.boids[i]['y']) * self.fly_mid_scale / self.num_boids

    # Fly away from nearby boids
    def fly_away(self):
        for i in range(self.num_boids):
            for j in range(self.num_boids):
                if (self.boids[i]['x'] - self.boids[i]['x']) ** 2 + (self.boids[j]['y'] - self.boids[i]['y']) ** 2 < self.fly_away_condition:
                    self.boids[i]['vx'] = self.boids[i]['vx'] + (self.boids[i]['x'] - self.boids[i]['x'])
                    self.boids[i]['vy'] = self.boids[i]['vy'] + (self.boids[i]['y'] - self.boids[j]['y'])

    # Try to match speed with nearby boids
    def fly_speed_match(self):
        for i in range(self.num_boids):
            for j in range(self.num_boids):
                if (self.boids[i]['x'] - self.boids[i]['x']) ** 2 + (self.boids[j]['y'] - self.boids[i]['y']) ** 2 < self.speed_match_condition:
                    self.boids[i]['vx'] += (self.boids[j]['vx'] - self.boids[i]['vx']) * self.speed_match_scale / self.num_boids
                    self.boids[i]['vy'] += (self.boids[j]['vy'] - self.boids[i]['vy']) * self.speed_match_scale / self.num_boids

    # Move according to velocities
    def move(self):
        for i in range(self.num_boids):
            self.boids[i]['x'] = self.boids[i]['x'] + self.boids[i]['vx']
            self.boids[i]['y'] = self.boids[i]['y'] + self.boids[i]['vy']

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
