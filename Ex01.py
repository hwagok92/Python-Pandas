#-*- coding:utf-8
'''
Created on 2020. 10. 21.

@author: user
'''
import numpy as np
import pandas as pd
from pandas import Series

arr = np.array([10,40,30,20])
print('arr:', arr)
print(type(arr))
print()

# Series : 객체를 담을 수 있는 1차원 배열과 같은 자료구조
#          index,value로 구성
            
sr = Series([10,40,30,20])
print('sr:\n', sr)
print()
print(sr[1])
print(type(sr))
print()

sr = Series([79,90,80,50], index=['윤아','태연','써니','수영'])
print('sr:\n', sr)
print()
print(sr['태연'])
# print(sr['티파니']) 에러 
print()

sr['태연'] = 100
sr['티파니'] = 30
print('sr:\n', sr)
print()

print(sr.values)
print(sr.values < 70)
print(sr[sr.values < 70])

print(sr.index)
print('태연' in sr)
print('효연' in sr)
print(79 in sr)
print(79 in sr.values)












print('\n\n\n\n\n\n\n')



