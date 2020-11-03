#-*- coding:utf-8
'''
Created on 2020. 11. 2.

@author: hwago
'''


import numpy as np
import pandas as pd
from pandas import *


df1 = DataFrame([[1001,'윤아'],[1002,'수영'],[1003,'서현'],[1004,'효연'],[1005,'써니']],
               columns=['고객번호','이름'])
print(df1)
print()

df2 = DataFrame({'고객번호':[1001,1007,1003,1004,1002,1001],
                 '금액':[10000,20000,15000,5000,100000,30000]})
print(df2)
print()

print('pd.merge(df1,df2):\n',pd.merge(df1,df2))
print()

print('pd.merge(df1,df2):\n',pd.merge(df1,df2,how='inner'))
print()

#합집합 조인
print('pd.merge(df1,df2):\n',pd.merge(df1,df2,how='outer'))
print()

#교집합을하면서 df1에 있는건 다 나오게 해라
print('pd.merge(df1,df2):\n',pd.merge(df1,df2,how='left'))
print()

#교집합을하면서 df2에 있는건 다 나오게 해라
print('pd.merge(df1,df2):\n',pd.merge(df1,df2,how='right'))
print()

print('----------------------------------------')

df1 = DataFrame({'고객명':['춘향','춘향','몽룡'],
                 '날짜':['2018-01-01','2018-01-02','2018-01-03'],
                 '데이터':[100,200,300]})
print('df1:\n',df1)
print()

df2 = DataFrame({'고객명':['춘향','몽룡','향단'],
                 '데이터':['여자','남자','여자'],
                 '주소':['경기','서울','부산']})
print('df2:\n',df2)
print()


# print('pd.merge(df1,df2):\n',pd.merge(df1,df2,how='inner')) 에러

print('pd.merge(df1,df2):\n',pd.merge(df1,df2,on='고객명',suffixes=['1','2'],how='inner'))






