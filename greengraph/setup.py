from setuptools import setup, find_packages

setup(
    name = "myGreengraph",
    version = "0.1",
    description='Assingment 4 - RSE with Python @ UCL',
    packages = find_packages(exclude=['*test','*png']),
    #scripts = [''],
    install_requires = ['argparse',
                        'requests',
                        'pypng',
                        'numpy',
                        'matplotlib',
                        'geopy']
)
