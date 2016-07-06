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
    version='1.0.0',
    description="Michelle's Python toolkit",
    long_description=long_description,
    url='https://github.com/anonmily/pythonlib',
    author='Michelle Liu',
    author_email='michelle@michelleliu.io',
    license='MIT',
    keywords='files loggin message email mongodb aws sqs diff',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
      'pymongo',
      'boto3',
      'yaml'
  ]
)