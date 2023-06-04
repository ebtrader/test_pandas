import numpy as np
import pandas as pd
import csv

# https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.digitize.html#numpy-digitize
# https://cmdlinetips.com/2019/12/how-to-discretize-bin-a-variable-in-python/

#with open('top150.csv') as i:
#    reader = csv.reader(i)
#    your_list = list(reader)

#x = your_list
#print(x)
df = pd.read_csv('top150.csv')
df.columns = ['height']

df1 = pd.read_csv('bins.csv')
df1.columns = ['bin_intervals']
print(df1)

df2 = pd.read_csv('label_rank.csv')
df2.columns = ['label_rank']
#print(df2)

df3 = pd.read_csv('label_numbers.csv')
df3.columns = ['label_number']

df['binned']=pd.cut(x=df['height'], bins=df1['bin_intervals'])

#print(df)

df['height_rank']=pd.cut(x = df['height'],
                        bins = df1['bin_intervals'],
                        labels = df3['label_number'])

#print(df)

df['height_bin']=pd.cut(x = df['height'],
                        bins = df1['bin_intervals'],
                        labels = df2['label_rank'],
                        )

print(df)
df.to_csv('height_ranker.csv')