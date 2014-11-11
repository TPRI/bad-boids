from boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml



# A regression test to check the model behaves as it did previously
def test_bad_boids_regression():

    my_boids = Boids()

    # Load the regression data from fixture.yaml
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))

    # Take the input data from the regression_data["before"]
    boid_data = regression_data["before"]

    # Set the boids to the before state
    my_boids.set_boids(boid_data)

    # Run the model
    my_boids.update_boids()

    boid_data  = [my_boids.get_x_coordinates(), my_boids.get_y_coordinates(), my_boids.get_vx_coordinates(), my_boids.get_vy_coordinates()]

    print regression_data["after"]
    print boid_data

    # Compare output of model boid_data with regression_data "after"
    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)