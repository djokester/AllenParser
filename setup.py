#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""

import sys
from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

if sys.version_info[:2] < (3, 5):
    print(('AllenParser requires Python version 3.5 or later (%d.%d detected).' %sys.version_info[:2]))
    sys.exit(-1)

try:                  
    import anytree
except ImportError:
    print('gensim must be installed to use lingatagger')
    sys.exit(-1)

try:                  
    import allennlp
except ImportError:
    print('re must be installed to use lingatagger')
    sys.exit(-1)

sys.path.insert(0, 'AllenParser')


if __name__ == "__main__":
    setup(
        name = "AllenParser",
        version = "1.0",
        author = "Samriddhi Sinha",
        author_email = "samridhhisinha.iitkgp@gmail.com",
        description = "A simple functional implementation of Allen NLP's constituency Parser",
        url='https://github.com/djokester/AllenParser',
        keywords= ['nlp', 'parsing', 'linguistics'],
        packages = ['AllenParser'],
        license = 'Apache License',
        install_requires = ['allennlp', 'anytree']
    )


