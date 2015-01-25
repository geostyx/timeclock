from setuptools import setup, find_packages

setup(
    name='timeclock',
    version='0.1.1.dev',
    description='Module for tracking hours such as at a job',
    author='GeoStyx (Jacob Hands)',
    author_email='',
    packages=find_packages(),
    test_suite='timeclock.tests',
    install_requires=[
        'mongoengine>=0.8.7'
    ],
    entry_points={
        'console_scripts': [
            'timeclock-start = timeclock.main:main'
        ]
    })
