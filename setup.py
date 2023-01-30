#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Sudeepta Sarkar",
    author_email='sudsarkar13@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A GUI based python program which can take input of pre-declared grading system, session, semester, subjects, credits of each subject, and calculate the total marks secured as well as calculate the SGPA and CGPA.",
    entry_points={
        'console_scripts': [
            'kiit_gpa_calculator=kiit_gpa_calculator.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='kiit_gpa_calculator',
    name='kiit_gpa_calculator',
    packages=find_packages(include=['kiit_gpa_calculator', 'kiit_gpa_calculator.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sudsarkar13/kiit_gpa_calculator',
    version='0.1.0',
    zip_safe=False,
)
