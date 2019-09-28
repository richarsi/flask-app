# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()
print ("running Setup.py")
setup(
    name='mee.flaskr',
    version='0.1.0',
    description='Sample flask app',
    long_description=readme,
    author='Simon Richardson',
    author_email='claretnbluester@gmail.com',
    url='https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    namespace_packages=['mee'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'mock',
        'sphinx',
        'setuptools',
    ],
    extras_require={
        'test': [
        ]
    },
    entry_points="""
    # -*- Entry points: -*-
    """,
)
