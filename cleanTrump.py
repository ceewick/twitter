from extractTrump import df
import pandas as pd
import numpy as np
import sqlite3
import os, sys

'''
This is not accurate/complete
starting to learn Pandas. Was trying to create a list or
pd.Series with the df columns datatypes, then
automatically input that when creating SQL.

Also need to clean up this data.

Going to come back to this later.
'''

col = df.columns
df2 = pd.Series(index=col)
# df2 = pd.Series(data=,index=col)
# df2[col] = type(col)
# for x in df2:
#     print(x)
# l = []
# print(df2.head())
# print(type(df))

s = set()
by_column = [df[x].values.tolist() for x in df.columns]
for x in by_column:
    print(type(x[0]),'\n')
    print(type(x[4]))

