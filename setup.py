import io
from setuptools import find_packages, setup


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='pysuffixarray',
      version='0.0.1',
      description='Suffix array implementation in python.',
      long_description=long_description(),
      url='https://github.com/dohlee/pysuffixarray',
      author='dohlee',
      author_email='apap950419@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      classifiers=[
          'Programming Language :: Python :: 3.5',
          ])