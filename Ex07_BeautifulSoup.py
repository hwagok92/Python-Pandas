#-*- coding:utf-8
'''
Created on 2020. 10. 22.

@author: user
'''
# BeautifulSoup : 웹페이지를 탐색하는 파이썬 웹 크롤링 라이브러리 툴
from bs4 import BeautifulSoup
import urllib.request

with open("example.html") as fp :
    soup = BeautifulSoup(fp,'html.parser')

    print('1:', soup.title)
    print('2:',soup.title.name)
    print('3:',soup.title.string)
    print('4:',soup.title.parent.name)
    print('5:', soup.p)
    print('6:', soup.find_all('p'))
    print('7:', soup.find_all('div'))
    print('8:', soup.find_all('div','ex_class'))
    print('9:', soup.find_all('div',id='ex_id'))
    
print('---------')
    
    
soup = BeautifulSoup(urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&tg=0&date=20201021').read(),'html.parser')
res = soup.find_all('div','tit5')
print('res:\n',res)

movieList = []
gradeList = []
for n in res :
    print(n.get_text())
    movieList.append(n.get_text().replace("\n",""))

print('movieList : ', movieList)
    

res2 = soup.find_all('td','point')
print('res2:\n',res2)

for n2 in res2 :
    print(n2.get_text())
    gradeList.append(n2.get_text())
    
print('gradeList : ', gradeList)    

for i in range(len(movieList)) :
    print(movieList[i],':',gradeList[i])



            
    
    
    
    
    
    
    
print('\n'*10)
    
# C:\Users\user\anaconda3\Library\bin폴더안의 아래 2화일을 복사해서
# libcrypto-1_1-x64.dll, libssl-1_1-x64.dll
# C:\Users\user\anaconda3\DLLs에 붙여넣기 하면 된다. 
    













