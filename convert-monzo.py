#!/usr/bin/env python3
import pandas as pd

df = pd.read_csv("MonzoDataExport_November_2018-11-08_180311.csv")

df.created = df.created.str[:10]


#print(df[['created','local_amount','local_currency','category','notes','description']])

for index, row in df.iterrows():
    print('Date:',row['created']),
    print('Description:',row['description']),
    print('Amount:',row['local_amount'],),
    print('Balance:\n')
