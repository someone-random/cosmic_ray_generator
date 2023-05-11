# Muon cosmic ray event generator
This is a simple sea-level cosmic ray generator, that generates sea-level muons' energies and zenith angles.

The functions for PDFs are given in functions.py
the function element_resolve depends on having elements.csv alailable. This function is not used in the code but may be handy.

Dependencies: NumPy, SciPy

## Build instructions
Clone the git repo and build with pip
```bat
someone@github:~$ git clone https://github.com/someone-random/cosmic_ray_generator.git
someone@github:~$ cd cosmic_ray_generator
someone@github:~$ pip install .
```
The program can be run by doing
```bat
someone@github:~$ MuCreate 1000
```
which will create 1000 muons. Muons are generated with angles by default.
## Optional arguments
| Name        | Description | Default|
| ----------- | ----------- |--------|
| -l, --llim  | Specify lower energy limit in GeV|0GeV|
| -u --ulim   | Specify upper energy limit in GeV|500GeV|
| --with-times| Tells the generator to produce timestamps for each muon|-|
| --no-angles | Tells the generator to not generate angles (vertical muons only)|-|
| -d, --det   | Specify detector area in cm^2|None|