from setuptools import setup, find_packages
setup(name='battleship',
version='1.0.0',
description='Battleship game library',
url='#',
author='Serop Kelkelian',
author_email='skelkelian88@gmail.com',
license='MIT',
packages=find_packages('src', exclude=['tests']),
zip_safe=False)