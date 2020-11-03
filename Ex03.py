#-*- coding:utf-8
'''
Created on 2020. 10. 22.

@author: admin
'''
#BeautifulSoup : 웹페이지를 탐색하는 파이썬 웹 크롤링 라이브러리 툴
from bs4 import BeautifulSoup
import urllib.request


with open("example.html") as fp: #안쓰면 읽기용도인 'r'이 생략되어있다
 
    soup = BeautifulSoup(fp,'html.parser')

    print('1:',soup.title)
    print('2:',soup.title.name)
    print('3:',soup.title.string)
    print('4:',soup.title.parent.name)
    print('5:',soup.p)
    print('6:',soup.find_all('p'))
    print('7:',soup.find_all('div'))
    print('8:',soup.find_all('div','ex_class'))
    print('9:',soup.find_all('div',id='ex_id'))
#들여쓰기를 안하면 자동으로 닫힌다.     
print('-------------------------------------------')    

soup = BeautifulSoup(urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&tg=0&date=20201021').read(),'html.parser')
res = soup.find_all('div','tit5')
print('res:\n',res)
    
movieList = []
for n in res :
    print(n.get_text())
    movieList.append(n.get_text().replace("\n", " "))

print('movieList : ', movieList)

res2 = soup.find_all('td','point')  
pointList = []
for n in res2 :
    print(n.get_text())
    pointList.append(n.get_text())

print('pointList : ', pointList)
    
for i in range(len(movieList)) :
    print(movieList[i],':',pointList[i])
    