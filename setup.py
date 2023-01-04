from setuptools import setup
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='dreams',
    version='0.0.8.3',
    url='https://github.com/reinanbr/dreams',
    license='BSD v3',
    author='Reinan Br',
    #entry_points = {
    #    'console_scripts': ['getmusic=tubemp3.get_music_line:main'],
    #},
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='video link api porn',
    description=u"Library for getting educative url video's",
    packages=find_packages(),
    install_requires=['requests','mechanicalsoup','bs4','toml'],)
