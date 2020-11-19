from os import name
from setuptools import setup, find_packages

setup(
    name='Autoflow',
    version='0.1.0',
    description='A package that automates your workflow',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'af = autoflow.main:main'
        ]
    }
)
