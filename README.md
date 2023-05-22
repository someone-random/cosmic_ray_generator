# Muon cosmic ray event generator
A cosmic ray event generator for muons at sea level. The original paper describing the generator is in writeup.pdf. Tests and corrections made to the generator is in cosmic_ray.pdf. The units for this generator are GeV for energy, seconds for time and cm^2 for detector area.

Dependencies: NumPy, SciPy

## Build instructions
Clone the git repo and build with pip
```console
someone@github:~$ git clone https://github.com/someone-random/cosmic_ray_generator.git
someone@github:~$ cd cosmic_ray_generator
someone@github:~$ pip install .
```
The program can be run by doing
```console
someone@github:~$ MuCreate 1000
```
which will create 1000 muons. Muons are generated with angles by default. To store the output, run
```console
someone@github:~$ MuCreate 1000 > output_file
```
## Optional arguments
| Name        | Description | Default|
| ----------- | ----------- |--------|
| -l, --llim  | Specify lower energy limit in GeV|0GeV|
| -u --ulim   | Specify upper energy limit in GeV|500GeV|
| --with-times| Tells the generator to produce timestamps for each muon|-|
| --no-angles | Tells the generator to not generate angles (vertical muons only)|-|
| -d, --det   | Specify detector area in cm^2|None|
