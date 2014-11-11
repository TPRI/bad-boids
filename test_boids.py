""" A regression test to check the boids model behaves as it did previously """

from boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml


def test_bad_boids_regression():

    my_boids = Boids()

    # Load the regression data from fixture.yaml
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))

    # Take the input data from the regression_data["before"]
    boid_data_before = regression_data["before"]

    # Set the boids to the before state
    my_boids.set_boids(boid_data_before)

    # Run the model
    my_boids.update_boids()

    # Get the boids after state
    boid_data_after = my_boids.get_boids()

    # Compare output of model boid_data_after with regression_data["after"]
    for after, before in zip(regression_data["after"], boid_data_after):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)