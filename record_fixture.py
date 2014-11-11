# File to create regression test data

import yaml
from boids import Boids

my_boids = Boids()

# Create a deepcopy of the initial state of the boids object before simulation
before = my_boids.get_boids()

# Run the simulation
my_boids.update_boids()

# Assign the result of the simulation to after
after = my_boids.get_boids()

# Create a yaml file of with the before and after state
fixture = {"before": before, "after": after}
fixture_file = open("fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
