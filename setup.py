from setuptools import setup
# you may need setuptools instead of distutils

setup(
    # basic stuff here
    scripts = ['sbrowser'],
    package_data={'': ['LICENSE'], '': ['README.md']},
    include_package_data=True
)
