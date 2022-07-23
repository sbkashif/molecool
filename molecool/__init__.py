"""
molecool
A Python package for analyzing and visualizing xyz files. For MolSSI Workshop Python Package development workshop
"""

# Add imports here
from .functions import *
from .molecule import build_bond_list
from .measure import calculate_distance
from .measure import calculate_angle
from .visualize import draw_molecule, bond_histogram
from .atom_data import atomic_weights, atom_colors
from .io import open_pdb, open_xyz,write_xyz


# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
