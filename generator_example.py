"""
A small test script to demonstrate the generator's useage.
"""

import functions
from rejection_sampler import generator
import numpy

time_gen = generator(times=True,detector_area=1)

print("10 Random energies and times:", time_gen.create(10), sep='\n',end='\n\n')

angle_gen = generator(times=False,with_angles=True)

print("20 Random energies and angles:", angle_gen.create(20), sep='\n',end='\n\n')