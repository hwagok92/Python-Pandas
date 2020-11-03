#-*- coding:utf-8
'''
Created on 2020. 11. 2.

@author: hwago
'''
import pandas as pd
import numpy as np
from pandas import *
from Ex04 import filename
from openpyxl.utils.cell import col

mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드', \
            'TCS하이패스구분코드', '1종교통량', '2종교통량', \
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량', 'Noname']

# 20170201|00|101 |0|1|379|7|7|43|4|1|441|
# 20170201|00|101 |0|2|1000|70|124|78|43|55|1370|
# 20170201|00|101 |1|1|391|22|10|34|8|24|489|
#이렇게 한줄로 되어있는걸 | 기준으로 나눴다

filename='capital_area.csv'

myframe = pd.read_table(filename,sep='|',names=mycolumn)
print('myframe:\n',myframe)
print(type(myframe))


a = myframe.reindex(columns=['영업소코드','총교통량','1종교통량'])
print('a:\n',a)

b = myframe[['영업소코드','총교통량','1종교통량']]
print('b:\n',b)
print()



mygrouping = myframe.groupby('영업소코드')
print('mygrouping:\n',mygrouping)
print()
#영업소 코드로 묶고 같은 영업소코드 여러개를 한번에 묶어서 출력
result = mygrouping.sum()
print('result(mygrouping.sum()):\n',result)
print()


#콕 찝어서 원하는 것만 출력하게 하는 코드 전부 다 볼 필요는 없으니
mygrouping = myframe.groupby('영업소코드')['총교통량']
print('mygrouping:\n',mygrouping)
print()

result2 = mygrouping.sum()
print('result2(mygrouping.sum()):\n',result2)
print()

grouping = myframe.groupby('집계일자')['5종교통량']
result3 = grouping.sum()
print('result3(mygrouping.sum()):\n',result3)
print()

#영업소코드가 190인것만 가져와라
result4 = myframe[myframe['영업소코드']==190]
print('result4:\n',result4)

#이건 가능하긴 한데 쩝..안됀다네
# result5 = myframe[myframe['영업소코드']==190][myframe['입출구구분코드']==1]
# print('result5:\n',result5)

result5 = myframe[(myframe['영업소코드']==190) & (myframe['입출구구분코드']==1)]
print('result5:\n',result5)

#집계일자별로 총교통량의 합계가 800000이 넘는 레코드
grouping = myframe.groupby('집계일자')['총교통량']
sortSum = grouping.sum()
result6 = sortSum[sortSum>800000]
print(result6)
print()


print('-------------오늘의 과제-------------------')
# 선생님 답
# col = ['class','kor','eng']
# df = DataFrame(['2반',33,44],['1반',13,24],['3반',34,84],['2반',63,14],
#                ['3반',88,77],['1반',88,77],columns=col)
# print('df:\n',df)
# print()

# korAvg = df.groupby('class')['kor'].mean()
# print('각 반별로 kor평균:\n',korAvg)
# print()

# engAvg = df.groupby('class')['eng'].mean()
# print('각 반별로 kor평균:\n',engAvg)
# print()

# gb_class = df.groupby('class').mean()
# print('gb_class',gb_class)
# print()

df = DataFrame({'class':['2반','1반','3반','2반','3반','1반'],
                 'kor':[33,13,34,63,88,88],
                 'eng':[44,24,84,14,77,77]})
print('df:\n',df)
print()

grouping = df.groupby('class')['kor']
korAvg = grouping.mean()
print('각 반별로 kor평균:\n',korAvg)
print()

grouping = df.groupby('class')['eng']
engAvg = grouping.mean()
print('각 반별로 eng평균:\n',engAvg)
print()

print(pd.merge(korAvg,engAvg,on='class'))
print()








