#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 20:09:49 2018

@author: jinyi
"""


import numpy as np
import pandas as pd
n = 10
colors = np.random.choice(['red', 'green'], size=n)
foods = np.random.choice(['eggs', 'ham'], size=n)
index = pd.MultiIndex.from_arrays([colors, foods], names=['color', 'food'])
df = pd.DataFrame(np.random.randn(n, 2), index=index)
# df.index.names = [None, None]
df.query('color == "red"')
#                       0         1
#    color food                    
#    red   ham   0.990638  0.549925
#    green ham   0.908474  1.146405
#          ham   0.519298 -0.535438
#          eggs  0.986250 -0.632079
#    red   eggs -0.248902  2.182438
#    green eggs  0.989632  0.045932
#          eggs -0.342036 -1.289004
#          eggs  0.117596  1.071560
#    red   ham   0.735483  0.528593
#          eggs -0.483654 -1.061651

#MultiIndex(levels=[['green', 'red'], ['eggs', 'ham']],
#           labels=[[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]],
#           names=['color', 'food'])


#    df.xs('green',level=0)   # level 0 => color, level 1 => food
#    Out[112]: 
#                 0         1
#    food                    
#    ham   0.360225 -1.602105
#    eggs  1.353229 -1.981854
#    ham   0.228314 -0.374108
#    ham   0.714012 -2.519875