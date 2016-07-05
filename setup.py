# -*- coding: utf-8 -*-
from setuptools import setup
import nmtpy

setup(
        name='nmtpy',
        version=nmtpy.__version__,
        description='NMT framework for Python based on Theano',
        url='http://github.com/ozancaglayan/nmtpy.git',
        author='Ozan Çağlayan',
        author_email='ozancag@gmail.com',
        license='MIT',
        packages=['nmtpy', 'nmtpy.models', 'nmtpy.iterators', 'nmtpy.metrics', 'pycocoevalcap'],
        install_requires=[
          'numpy',
          'theano',
          'six',
        ],
        scripts=[
                    # These will be installed into your system
                    'bin/nmt-train',
                    'bin/nmt-extract',
                    'bin/nmt-translate',
                    'bin/nmt-build-dict',
                    'bin/nmt-coco-metrics',
                ],
        zip_safe=False)
