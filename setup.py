from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='This project aims to develop machine learning models for drowsiness detection using Behind-The-Ears EEG  signal. After training and evaluating on PC, those pretrained models are also deployed on microcontroller-based edge device for real-time test.',
    author='Ha-Trung Nguyen',
    license='MIT',
)
