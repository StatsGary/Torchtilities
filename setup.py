from setuptools import setup, find_packages
#https://pypi.org/classifiers/
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Science/Research',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Unix',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]

setup(
    name='torchtilities',
    version='0.0.2',
    description='Utilities for PyTorch and conversion functions',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://hutsons-hacks.info/',
    author='Gary Hutson',
    author_email='hutsons-hacks@outlook.com',
    license='MIT',
    classifiers=classifiers,
    keywords='pytorch utilities python',
    packages=find_packages(),
    install_requires=['onnx', 'onnx-tf']
)


