import pandas as pd
import numpy as np

firstProductSet = {'Product1': ['Computer','Phone','Printer','Desk'],
                   'Price1': [1200,800,200,350]
                   }
df1 = pd.DataFrame(firstProductSet,columns= ['Product1', 'Price1'])


secondProductSet = {'Product2': ['Computer','Phone','Printer','Desk'],
                    'Price2': [900,800,300,350]
                    }
df2 = pd.DataFrame(secondProductSet,columns= ['Product2', 'Price2'])


df1['Price2'] = df2['Price2'] #add the Price2 column from df2 to df1

df1['pricesMatch?'] = np.where((df1['Price1'] > df2['Price2']) & (df1['Price1'] > 300), 'True', df1['Product1'])  #create new column in df1 to check if prices match
#df1['priceDiff?'] = np.where(df1['Price1'] > df2['Price2'], 0, df1['Price1'] - df2['Price2']) #create new column in df1 for price diff
print (df1)