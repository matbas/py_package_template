# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='{{ cookiecutter.project_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/matbas/{{ cookiecutter.project_name }}',
    packages=find_packages(exclude=('tests', 'docs'))
)
