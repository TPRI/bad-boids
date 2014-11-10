from boids import update_boids
from nose.tools import assert_almost_equal
import os
import yaml


# A regression test to check the model behaves as it did previously
def test_bad_boids_regression():
    # Load the regression data from fixture.yaml
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))

    # Take the input data from the regression_data["before"]
    boid_data = regression_data["before"]

    # Run the model
    update_boids(boid_data)

    # Compare output of model boid_data with regression_data "after"
    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)