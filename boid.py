import os
import yaml


class Boid(object):

    def __init__(self, x, y, vx, vy):

        # Load initial config from initial_config.yml
        config = yaml.load(open(os.path.join(os.path.dirname(__file__), 'initial_config.yml')))

        self.num_boids = config["num_boids"]
        self.fly_mid_scale = config["fly_mid_scale"]
        self.fly_away_condition = config["fly_away_condition"]
        self.speed_match_condition = config["speed_match_condition"]
        self.speed_match_scale = config["speed_match_scale"]

        # Construct Boid
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    # Fly towards the middle
    def fly_mid(self, boid):
        self.vx += (boid.x - self.x) * self.fly_mid_scale / self.num_boids
        self.vy += (boid.y - self.y) * self.fly_mid_scale / self.num_boids

    # Fly away from nearby boids
    def fly_away(self, boid):
        if (boid.x - self.x) ** 2 + (boid.y - self.y) ** 2 < self.fly_away_condition:
            self.vx += (self.x - boid.x)
            self.vy += (self.y - boid.y)

    # Try to match speed with nearby boids
    def fly_speed_match(self, boid):
        if (boid.x - self.x) ** 2 + (boid.y - self.y) ** 2 < self.speed_match_condition:
            self.vx += (boid.vx - self.vx) * self.speed_match_scale / self.num_boids
            self.vy += (boid.vy - self.vy) * self.speed_match_scale / self.num_boids

    # Move according to velocities
    def move(self):
        self.x += self.vx
        self.y += self.vy
