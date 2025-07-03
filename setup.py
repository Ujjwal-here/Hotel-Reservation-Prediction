from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel-Reservation-Prediction",
    version="0.1",
    author="chiku",
    packages=find_packages(),
    install_requires = requirements,
    description="Hotel Reservation Prediction (MLOPS)",
    
)