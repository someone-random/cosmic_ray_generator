import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="Cosmic ray muon event generator",
    version="0.0.1",
    author="Singh Atipunumphai",
    author_email="sa958@cam.ac.uk",
    description=("A simple cosmic ray event generator. Generate muons"
                "with some energy, angle and time."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/someone-random/cosmic_ray_generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy", "scipy", "pandas"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "MuCreate = api.cli:main",
        ]
    }
)
