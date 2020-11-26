from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-af',
    version='1.0.0',
    description='A python package that automates your workflow',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MLH-Fellowship/autoflow',
    author='Team Autoflow',
    platforms=['posix'],
    license ='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'PyGithub',
        'gitpython'
    ],
    entry_points={
        'console_scripts': [
            'af = autoflow.main:main'
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords='autoflow, python-af, workflow automation, productivity',
    python_requires='>=3.6',
)
