""" File to create regression test data """

import yaml
from boids import Boids

# Create a Boids object
my_boids = Boids()

# Create a copy of the initial state of the boids
before = my_boids.get_boids()

# Run the simulation
my_boids.update_boids()

# Create a copy of the final state of the boids
after = my_boids.get_boids()

# Create a yaml file of the before and after states
fixture = {"before": before, "after": after}
fixture_file = open("fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
