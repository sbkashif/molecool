import pytest
import molecool
import numpy as np

@pytest.fixture
def methane_molecule():
    symbols=['C','H','H','H','H']
    coordinates = np.array([[1, 1, 1], [2.4, 1, 1],[-0.4, 1, 1],[1, 1, 2.4],[1, 1, -0.4],])
    return symbols, coordinates

