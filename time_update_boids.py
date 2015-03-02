""" File to time update_boids"""

import timeit
import numpy as np

time_boids = timeit.repeat('my_boids.update_boids()', setup='from boids import Boids\nmy_boids = Boids()', repeat=100, number=100)

print np.mean(time_boids)


