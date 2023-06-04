import yfinance as yf
import pandas as pd
import csv
import numpy as np
import math

with open('top150.csv') as i:
    reader = csv.reader(i)
    your_list = list(reader)

x = your_list
x_length = int(len(x))
tkrs = []
tkrs = sum(x, [])

df_sma = pd.DataFrame()
df_wma = pd.DataFrame()
df_ema_of_wma = pd.DataFrame()
df_first_part = pd.DataFrame()
df_second_part = pd.DataFrame()
df_wtdehma = pd.DataFrame()
df_wtd_toggle = pd.DataFrame()
df_wtd_buy_sell = pd.DataFrame()

for j in tkrs:
    df = yf.download(j, period='3mo')
    df_sma['Close'+'_'+str(j)] = df['Close']
    num_periods = 6
    df_sma['SMA_' + str(j)] = df['Close'].rolling(num_periods).mean()
    weights = np.arange(1, (num_periods + 1))  # this creates an array with integers 1 to num_periods included
    df_wma['WMA_' + str(j)] = df['Close'].rolling(num_periods).apply(lambda prices: np.dot(prices, weights) / weights.sum(), raw=True)


#df_wma.to_csv('wma100.csv')
#print (df_wma)
list_ib = df_wma.columns.values
counter = x_length
for j in list_ib:
    wtdehma_length = num_periods
    wtdehma_length_half = int(wtdehma_length / 2)
    df_ema_of_wma['EMA'+ str(j)] = df_wma[j].ewm(span=wtdehma_length_half, adjust=False).mean()
    sqr_wtdehma_length = int(math.sqrt(wtdehma_length))
    df_first_part[str(counter)] = df_wma[j].ewm(span=sqr_wtdehma_length, adjust=False).mean()
    counter = counter + 1

list_ic = df_ema_of_wma.columns.values
counter_1 = 0
for column in list_ic:
    df_first_part[str(counter_1)] = df_ema_of_wma[column]*2
    counter_1 = counter_1 + 1

counter_2 = 0
counter_3 = x_length
max_number = counter_3
while counter_2 < max_number:
    df_wtdehma[tkrs[counter_2]] = df_first_part[str(counter_2)] - df_first_part[str(counter_3)]
    counter_2 = counter_2 + 1
    counter_3 = counter_3 + 1

df_wtd_toggle = df_wtdehma.diff()
#wtd_buy_sell = np.where(df_wtd_toggle>0,"Long","Short")


#print(df_ema_of_wma)
#print(df_wma)
#print(df_first_part)
#print(df_wtdehma)
df_wtd_toggle[df_wtd_toggle > 0] = 1
df_wtd_toggle[df_wtd_toggle < 0] = 0



print(df_wtd_toggle)

#print(df_wtd_buy_sell)

dfobj = df_wtd_toggle
dfobj.to_csv('test_run_multi_buy_sell.csv')