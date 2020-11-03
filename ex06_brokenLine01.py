# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

x1 = [1, 2, 3, 4]
y1 = [3, 7, 6, 4]
x2 = [1, 2, 3, 4]
y2 = [4, 6, 8, 5]

ymax =  max(max(y1), max(y2)) + 1 # max(7,8)=>8
ymin =  min(min(y1), min(y2)) - 1 # min(3,4)=>3
print(ymax,',',ymin)
font_location = 'c:/Windows/fonts/malgun.ttf' 
font_name = font_manager.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name) 

plt.plot(x1, y1, label = 'first line~',color='r') 
plt.plot(x2, y2, label='second line') #'bo,r+ 주황색 설정됨

print('arange:',np.arange(ymin, ymax + 1, 1)) # [2 3 4 5 6 7 8 9]

plt.yticks( np.arange(ymin, ymax + 1, 1)) # 2~9까지 눈금 설정이 된다. 

plt.xlabel("xlabel") # 라벨 출력
plt.ylabel("y축")


plt.title("Adding \nand Title") # 타이틀 출력
plt.legend() # 범례 출력

filename = 'brokenLine01.png'
plt.savefig( filename, dpi=400, bbox_inches='tight' )
print( filename + ' 파일이 저장되었습니다.')
plt.show()

