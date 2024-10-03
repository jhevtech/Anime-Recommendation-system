from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Jhevtech'
SRC_REPO = 'src'
List_of_Requirements = ['streamlit']


setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    description = 'Something to help with finding your next anime series',
    package = [SRC_REPO],
    install_requirements = List_of_Requirements,
)