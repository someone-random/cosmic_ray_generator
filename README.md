This is a simple sea-level cosmic ray generator, that generates sea-level muons' energies and zenith angles.

The functions for PDFs are given in functions.py
the function element_resolve depends on having elements.csv alailable. This function is not used in the code but may be handy.

A simple rejection sampler is given in rejection_sampler.py

Dependencies: NumPy, SciPy

Build instructions: Clone the git repo and build with pip
```console
someone@github: ~$ git clone https://github.com/someone-random/cosmic_ray_generator.git
someone@github: ~$ cd cosmic_ray_generator
someone@github: ~$ pip install .
```
