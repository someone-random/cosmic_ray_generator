import functions
from rejection_sampler import generator
import numpy

my_generator = generator(times=True,detector_area=1)

print(my_generator.create(10))

my_generator2 = generator(times=False,with_angles=True)

print(my_generator2.create(20))