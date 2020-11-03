#-*- coding:utf-8
'''
Created on 2020. 11. 2.

@author: hwago
'''

import numpy as np
from pandas import *
import pandas as pd

df = DataFrame([[3,5,1],[9,2]],
               index=['apple','banana'],
               columns=['kim','park','jung'])

print('df:\n',df)
print()

#끝자리에 값을 넣고 싶지않으면 그냥 안넣으면 돼지만 중간에 데이터를 넣고 싶다면 np.NaN을 넣어야 한다
df = DataFrame([[3,np.NaN,1],[9,2]],
               index=['apple','banana'],
               columns=['kim','park','jung'])

print('df:\n',df)
print()

filename = 'mynan.csv'
table = pd.read_csv(filename,encoding='euc-kr')
print('table:\n',table)

table = pd.read_csv(filename,encoding='euc-kr',
                    index_col=0)
print('table:\n',table)
print(type(table))
print(table.size)

#데이터가 있으면 False 없으면 True
print(table.isna())
print()

print(pd.isna(table))
print()

#데이터 없으면 True 있으면 False
print(table.notnull())
print()

#이용할 수 없는걸 빼라=데이터가 없으면 빼라
table2 = table.dropna()
print('table2:\n',table2)
print()
#기본값 how='any' 어디라도 데이터가 없으면 지워라
table2 = table.dropna(how='any')
print('table2:\n',table2)
print()

table2 = table.dropna(how='all')
print('table2:\n',table2)
print()

#데이터가 없는 곳에 값을 넣는 코드 fillna
table = table.fillna({'kor':20,'eng':90})
print('table:\n',table)

filename="mynan2.csv"
table.to_csv(filename,encoding='euc-kr')








