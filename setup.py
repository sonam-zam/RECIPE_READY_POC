# coding: utf-8

from setuptools import setup, find_packages

NAME = "RecipeGenerator"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Simple Recipe Generator - ML",
    author_email="mariadona8019@gmail.com",
    url="",
    keywords=["Swagger", "Simple Recipe Generator - ML"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['run=server.main']},
    long_description="""\
    Chef&#x27;s recipe generation API using machine learning
    """
)
