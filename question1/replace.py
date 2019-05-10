#!/usr/bin/env python

import os
import sys
import glob

if len(sys.argv) != 3:
    raise ValueError('replace.py takes 2 arguments')

find = sys.argv[1]
replace = sys.argv[2]

if not os.path.exists(replace):
    os.mkdir(replace)

for filename in glob.glob('*.txt'):
    with open(filename, 'r') as f:
        text = f.read()
    
    replaced = text.replace(find, replace)   

    with open(os.path.join(replace, filename), 'w') as f:
        f.write(replaced)
