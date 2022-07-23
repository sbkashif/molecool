"""
Unit and regression test for the measure module

"""

import molecool
import numpy as np
import pytest

@pytest.mark.slow
def test_calculate_distance():
    
    r1 = np.array([0,0,0])
    r2 = np.array ([0,1,0])

    expected_distance = 1

    calculate_distance = molecool.calculate_distance(r1,r2)

    assert expected_distance == calculate_distance


@pytest.mark.parametrize(
"r1,r2,r3,expected_angle",
[
    (np.array([1,0,0]), np.array([0,0,0]),np.array([0,1,0]),90),
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60  ),
    (np.array([np.sqrt(3)/2, (1/2), 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 30),
])

def test_calculate_angle(r1,r2,r3,expected_angle):

    calculate_angle=molecool.calculate_angle(r1,r2,r3,degrees=True)
    
    assert pytest.approx(calculate_angle,abs=1e-2) == expected_angle
