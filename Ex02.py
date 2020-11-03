#-*- coding:utf-8
'''
Created on 2020. 10. 22.

@author: user
'''
# Ex02.py

import numpy as np
import pandas as pd  
from dask.dataframe.io.tests.test_json import df

arr = np.array([[1,2,3],[4,5,6]])
print('arr:\n',arr)
print('차원:',arr.ndim)
print(arr.shape)
print(arr[1][2])
print()

df = pd.DataFrame([[1,2,3],[4,5,6]])
print('df:\n',df)
print(type(df))
print(df.ndim)
print(df.shape)
print(df[2][1])# df[칼럼명][index]
print()

my_dict = {'a':['1','3'],'b':['4','7'], 'c':['2','5']}
df2 = pd.DataFrame(my_dict)
print('df2:\n',df2)

my_dict = {'도시':['서울','부산','대구','부산','서울'], 
           'year':[2000,2001,2002,2002,2001],
           'pop':[1.5,1.7,1.2,1.8,2.3]
           }

df3 = pd.DataFrame(my_dict)
print('df3:\n',df3)

# df3:
#     도시  year  pop
# 0  서울  2000  1.5
# 1  부산  2001  1.7
# 2  대구  2002  1.2
# 3  부산  2002  1.8
# 4  서울  2001  2.3

print(df3['pop'][2]) #pop에 있는 1.2뽑는 코드
print(df3['도시'])
print()

print(df3.year)
print(df3[['도시','year']])
print()
#    도시  year
# 0  서울  2000
# 1  부산  2001
# 2  대구  2002
# 3  부산  2002
# 4  서울  2001

df3['income']=12.34
print('df3:\n',df3)
print()

# df3:
#     도시  year  pop  income
# 0  서울  2000  1.5   12.34
# 1  부산  2001  1.7   12.34
# 2  대구  2002  1.2   12.34
# 3  부산  2002  1.8   12.34
# 4  서울  2001  2.3   12.34

df3['income']=[11,12,13,14,15]
print('df3:\n',df3)
print()

# df3:
#     도시  year  pop  income
# 0  서울  2000  1.5      11
# 1  부산  2001  1.7      12
# 2  대구  2002  1.2      13
# 3  부산  2002  1.8      14
# 4  서울  2001  2.3      15

my_series = pd.Series([1.1,2.2,3.3,4.4,5.5], index=['one','two','three','four','five'])

print('my_series:\n', my_series)


myindex = ['one','two','three','four','five']
df3 = pd.DataFrame(my_dict,index=myindex)
print('df3:\n',df3)
print()

df3['pop'] = my_series
print('df3:\n',df3)
print()