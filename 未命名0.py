# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   文件名：      
   描述：       
   作者：       Pilot.Phil
   日期：       Mon Aug 17 20:23:46 2020
-------------------------------------------------

----------------------使用-----------------------

-------------------------------------------------
#-----------------xxxxxxxxxxxxxx-----------------#
"""

import numpy as np
import scipy as sp
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['font.family'] = 'SimHei'


# a=np.random.randn(16)
a=np.ones(8)

xa=sp.fft.fft(a)
print(xa)

plt.plot(np.abs(xa))








#---------------------测试-----------------------#
if __name__ == "__main__":
    pass
     
