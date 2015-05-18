from setuptools import setup
# you may need setuptools instead of distutils

setup(
    name = 'sbrowser'
    version = '0.0.1'
    scripts = ['sbrowser'],
    package_data={'': ['LICENSE'], '': ['README.md']},
    include_package_data=True
)
