# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='michellepylib',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description="Michelle's Python toolkit",
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/anonmily/pythonlib',

    # Author details
    author='Michelle Liu',
    author_email='michelle@michelleliu.io',

    # Choose your license
    license='MIT',

    # What does your project relate to?
    keywords='files loggin message email mongodb aws sqs diff',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)