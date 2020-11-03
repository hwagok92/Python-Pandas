#-*- coding:utf-8
'''
Created on 2020. 11. 3.

@author: admin
'''
#<웹에서 이미지 가져오기>
from bs4 import BeautifulSoup
import os,shutil
from urllib.request import urlopen

myfolder = 'c:\\imsi\\'

weekday_dict = {'mon':'월요일','tue':'화요일','wed':'수요일','thu':'목요일',\
                'fri':'금요일','sat':'토요일','sun':'일요일'}

#items() 튜플들이 리스트 안에 출력되게 하는 코드
print(weekday_dict.items())
# dict_items([('mon', '월요일'), ('tue', '화요일'), ('wed', '수요일'), ('thu', '목요일'), ('fri', '금요일'), ('sat', '토요일'), ('sun', '일요일')])
print()

print(weekday_dict.values())
# dict_values(['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'])
print()
try:
    for mydir in weekday_dict.values():
        mypath=myfolder+mydir
        print('mypath',mypath)
        if os._exists(mypath):
            #기존의 파일이 있으면 지워라는 코드
            shutil.rmtree(mypath)
        
        os.mkdir(mypath)
except FileExistsError:
    pass 
####################################################

#saveFile을 만들어 정의
def saveFile(image_url,weekday,mytitle):
    image_file = urlopen(image_url)
    myfile = open('c:\\imsi\\'+weekday_dict[weekday]+'\\'+mytitle+'.jpg','wb')
    
    myfile.write(image_file.read())
####################################################
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'

soup = BeautifulSoup(urlopen(myurl),'html.parser')

mytarget = soup.find_all('div',{'class':'thumb'})
print('mytarget:\n',mytarget)
print(len(mytarget)) #360개

for one in mytarget:
# <div class="thumb">
# <a href="/webtoon/list.nhn?titleId=721109&amp;weekday=sun" onclick="nclk_v2(event,'thm*S.img','','42')">
# <img alt="Here U Are" height="90" onerror="this.src='https://ssl.pstatic.net/static/comic/images/migration/common/blank.gif'" src="https://shared-comic.pstatic.net/thumb/webtoon/721109/thumbnail/thumbnail_IMAG10_844cec4a-9b1b-4e38-9c0c-d1ab94059edc.jpg" title="Here U Are" width="83"/><span class="mask"></span>
# </a>
# </div>
    #a태그의 속성이 href인것을 출력해라
    atag = one.find('a')
    myhref = atag.attrs['href']
    print('myhref:',myhref)
# myhref: /webtoon/list.nhn?titleId=738547&weekday=sun
    # ?까지 빈칸으로 대체해라 = 지워라
    myhref = myhref.replace('/webtoon/list.nhn?',' ')
    #결과물 titleId=738547&weekday=sun
    
    result = myhref.split('&')
    print('result:',result)
    #[' titleId=738547', 'weekday=sun']
    print()
    
    myweekday = result[1].split('=')[1]
    print('myweekday:',myweekday)
    print()
#----------------------------------------------------
# 지금 one에 들어가 있는 정보:
# <div class="thumb">
# <a href="/webtoon/list.nhn?titleId=721109&amp;weekday=sun" onclick="nclk_v2(event,'thm*S.img','','42')">
# <img alt="Here U Are" height="90" onerror="this.src='https://ssl.pstatic.net/static/comic/images/migration/common/blank.gif'" src="https://shared-comic.pstatic.net/thumb/webtoon/721109/thumbnail/thumbnail_IMAG10_844cec4a-9b1b-4e38-9c0c-d1ab94059edc.jpg" title="Here U Are" width="83"/><span class="mask"></span>
# </a>
# </div>
    imgtag = one.find('img')
    mytitle = imgtag.attrs['title']
    mytitle = mytitle.replace('?','').replace(':','')
    print('mytitle:',mytitle)
    print()
    #mytitle 선녀야 야옹해봐!
    
    
    mysrc = imgtag.attrs['src']
    print('mysrc:',mysrc)
#   mysrc: https://shared-comic.pstatic.net/thumb/webtoon/738547/thumbnail/thumbnail_IMAG10_877b93b2-26d0-4191-a71f-40d58fff32bb.jpg
    print()
    
    #정의한 saveFile을 호출
    saveFile(mysrc,myweekday,mytitle)
    

    













