import pandas as pd

df0 = pd.read_csv('file1.csv')
df1 = pd.read_csv('file2.csv')

v = df1.loc[:, 'Mile_min':'Mile_,max'].apply(tuple, 1).tolist()
idx = pd.IntervalIndex.from_tuples(v, closed='both') # you can also use `from_arrays`


df0['Score'] = df1.iloc[idx.get_indexer(df0.Mileage.values), 'Score'].values

df0.to_csv('file3.csv')
