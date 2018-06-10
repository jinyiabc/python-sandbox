#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 20:09:02 2018

@author: jinyi
"""

import pandas as pd
df = pd.DataFrame(
        {'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40],
         'CCC': [100, 50, -30, -50]})

print(df[(df.AAA <= 6) & (df.index.isin([0, 2, 4]))])


data = {'AAA':  [4, 5, 6, 7], 'BBB': [10, 20, 30, 40],
        'CCC': [100, 50, -30, -50]}
df = pd.DataFrame(data=data, index=['foo', 'bar', 'boo', 'kar'])
print(df)


# There are 2 explicit slicing methods, with a third general case
# 1.Positional-oriented (Python slicing style : exclusive of end)
# 2.Label-oriented (Non-Python slicing style : inc  lusive of end)
# 3.General (Either slicing style : depends on if the slice
#  contains labels or positions)

pos_oriented = df.loc['bar':'kar']
print(pos_oriented)

label_oriented = df.iloc[0:3]
print(label_oriented)

general = df.loc['bar':'kar']
print(general)

df2 = pd.DataFrame(data=data, index=[1, 2, 3, 4])  # Note index starts at 1.
print(df2.iloc[1:3])  # Position-oriented
print(df2.loc[1:3])  # label-oriented
print(df[~((df.AAA <= 6) & (df.index.isin([0, 2, 4])))])
# Using inverse operator(~) to take the complement.

# NEW COLUMNS
df = pd.DataFrame(
        {'AAA': [1, 2, 3, 4], 'BBB': [1, 1, 2, 2], 'CCC': [2, 1, 3, 1]})
# print(df)
source_cols = df.columns  # or some subset would work too.
new_cols = [str(x) + "_cat" for x in source_cols]
categories = {1: 'Alpha', 2: 'Beta', 3: 'Charlie'}
df[new_cols] = df[source_cols].applymap(categories.get)
print(df)
