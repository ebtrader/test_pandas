import pandas as pd

df = pd.DataFrame([[4,9],[2,5],[3,6],[1,4]], columns=['start','end'])
print(df)

pos = 3

df_result = df[df.eval('(start <= {}) & ({} <= end)'.format(pos,pos))]

print(df_result)