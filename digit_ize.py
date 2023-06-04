import numpy as np
import pandas as pd

x = np.array([42, 82, 91, 108, 121])

df = pd.DataFrame({"height":x})

#df['binned']=pd.cut(x=df['height'], bins=[0,25,50,100,200])

df['height_category']=pd.cut(x = df['height'],
                        bins = [0,25,50,100,200],
                        labels = [0, 1, 2,3])

df['height_bin']=pd.cut(x = df['height'],
                        bins = [0,25,50,100,200],
                        labels = ["very short", " short", "medium","tall"],
                        )

print(df)
