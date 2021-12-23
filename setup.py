from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: PyTorch Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Licence :: OSI Approved :: MIT License',
    'Programming Language:: Python :: 3'
]

setup(
    name='torchtilities',
    version='0.0.1',
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


