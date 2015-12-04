from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

version = '0.2'

try:
    REQUIREMENTS = open('requirements.txt').read()
except:
    REQUIREMENTS = [
    ]

setup(name='pipdiff',
    version=version,
    description="View a summary list of package release differences between your local environment and PyPI.",
    long_description=README,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='Evgeny Demchenko',
    author_email='little_pea@list.ru',
    url='https://github.com/ogt/pipdiff',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': ['pipdiff = pipdiff.pipdiff:main']
    }
)
