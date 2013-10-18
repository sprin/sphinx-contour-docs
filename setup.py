# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requires = ['Sphinx>=0.6']

setup(
    name='contour_docs',
    version='0.1',
    url='https://github.com/sprin/sphinx-contour-docs',
    license='MIT',
    author='sprin',
    description='Sphinx extension for Contour Document Links',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
