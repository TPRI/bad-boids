# File to create regression test data

import yaml
import boids
from copy import deepcopy

# Create a deepcopy of the initial state of the boids object before simulation
before = deepcopy(boids.boids)

# Run the simulation
boids.update_boids(boids.boids)

# Assign the result of the simulation to after
after = boids.boids

# Create a yaml file of with the before and after state
fixture = {"before": before, "after": after}
fixture_file = open("fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
