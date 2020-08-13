# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   文件名：      
   描述：       
   作者：       Pilot.Phil
   日期：       Thu Aug 13 22:22:35 2020
-------------------------------------------------

----------------------使用-----------------------

-------------------------------------------------
#-----------------xxxxxxxxxxxxxx-----------------#
"""

import xlrd
import numpy as np
import scipy as sp
import matplotlib
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
matplotlib.rcParams['font.family'] = 'SimHei'
 

xls = xlrd.open_workbook('test.xlsx') # 打开表格
table = xls.sheets()[0] # 打开第一张表
nrows = table.nrows # 行数
ncols = table.ncols # 列数

data=np.zeros([nrows,ncols],dtype="float")

for i in range(0,nrows): # 将表格读取到数组
    for j in range(0,ncols):
        rawVal=table.cell(i, j).value 
        if isinstance(rawVal,str)==True: # 空单元格其实是空字符串 如果是字符串
            data[i,j]=np.nan
        else:
            data[i,j]=float(rawVal)
            
# A=(W,S,H) 半宽 站号 高度

pNum=(nrows-1)*(ncols-1) # 点总数 包括含nan的 以后再删

points=np.zeros([pNum,3],dtype="float")

for i in range(1,nrows):
    for j in range(1,ncols):
        print(i)
        col=(i-1)*(j-1)
        # W
        points[col,0]=data[i,j]
        
        # S
        points[col,1]=data[i,0]
        
        # H
        points[col,2]=data[0,j]
	
	

x = points[:, 0]  # [ 0  3  6  9 12 15 18 21]
y = points[:, 1]  # [ 1  4  7 10 13 16 19 22]
z = points[:, 2]  # [ 2  5  8 11 14 17 20 23]
  
  
# 绘制散点图
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z)
  
  
# 添加坐标轴(顺序是Z, Y, X)
ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
plt.show()

        
        























# =============================================================================
# # 数据
# data = np.arange(24).reshape((8, 3))
# # data的值如下：
# # [[ 0  1  2]
# #  [ 3  4  5]
# #  [ 6  7  8]
# #  [ 9 10 11]
# #  [12 13 14]
# #  [15 16 17]
# #  [18 19 20]
# #  [21 22 23]]
# x = data[:, 0]  # [ 0  3  6  9 12 15 18 21]
# y = data[:, 1]  # [ 1  4  7 10 13 16 19 22]
# z = data[:, 2]  # [ 2  5  8 11 14 17 20 23]
#  
#  
# # 绘制散点图
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(x, y, z)
#  
#  
# # 添加坐标轴(顺序是Z, Y, X)
# ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
# ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
# ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
# plt.show()
# =============================================================================

#---------------------测试-----------------------#
if __name__ == "__main__":
    pass
     