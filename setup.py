"""Setup script for pytodoist"""
import os
from setuptools import setup

CWD = os.path.dirname(os.path.abspath(__file__))
VERSION_NS = {}
with open(os.path.join(CWD, 'src', 'todoist', '_version.py')) as f:
    exec(f.read(), {}, VERSION_NS)

setup(
    name='pytodoist',
    version=VERSION_NS['__version__'],
    packages=[
        'todoist', 'todoist.models'
    ],
    package_dir={'': 'src'},
    package_data={},
    author='Vincent Moret',
    author_email='moret.vincent@gmail.com',
    url='https://github.com/vmoret/pytodoist',
    install_requires=[
        'requests'
    ]
)
