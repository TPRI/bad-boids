import random
import os
import yaml
from boid import Boid


class Boids(object):
    """ Describes a flock of boids and runs the main simulation"""
    
    def __init__(self):
        
        # Load initial config from initial_config.yml
        config = yaml.load(open(os.path.join(os.path.dirname(__file__), 'initial_config.yml')))
        
        self.num_boids = config["num_boids"]

        # Construct boids as a array of arrays
        self.boids = [Boid(random.uniform(config['x_min'], config['x_max']),
                           random.uniform(config['y_min'], config['y_max']),
                           random.uniform(config['vx_min'], config['vx_max']),
                           random.uniform(config['vy_min'], config['vy_max'])) for x in range(self.num_boids)]

    # Fly boids towards the middle of the flock
    def fly_mid(self):
        for boid_i in self.boids:
            for boid_j in self.boids:
                boid_i.fly_mid(boid_j)

    # Fly boids away from nearby boids
    def fly_away(self):
        for boid_i in self.boids:
            for boid_j in self.boids:
                boid_i.fly_away(boid_j)

    # Fly boids as to match speed of nearby boids
    def fly_speed_match(self):
        for boid_i in self.boids:
            for boid_j in self.boids:
                boid_i.fly_speed_match(boid_j)

    # Move all boids
    def move(self):
        for boid_i in self.boids:
            boid_i.move()

    # The main simulation of flocking behaviour
    def update_boids(self):

        # Fly boids towards the middle of the flock
        self.fly_mid()

         # Fly boids away from nearby boids
        self.fly_away()

        # Fly boids as to match speed of nearby boids
        self.fly_speed_match()

        # Move all boids
        self.move()

    # A method to set the Boids' parameters for testing
    def set_boids(self, data):
        self.boids = [Boid(data[0][i],
                           data[1][i],
                           data[2][i],
                           data[3][i],) for i in range(self.num_boids)]

    # A method to get the Boids' parameters for plotting and testing
    def get_boids(self):
        return zip(*[[self.boids[i].x,
                     self.boids[i].y,
                     self.boids[i].vx,
                     self.boids[i].vy] for i in range(self.num_boids)])
