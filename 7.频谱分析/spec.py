# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   文件名：      spec
   描述：       频谱谱分析
   作者：       Pilot.Phil
   日期：       Tue Aug 11 23:21:53 2020
-------------------------------------------------

----------------------使用-----------------------
P1=saft(signal,Fs,pf) # DFT单边谱

-------------------------------------------------
"""

import math
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['font.family'] = 'SimHei'


#-----------------傅里叶单边谱分析-----------------#
def saft(signal,Fs,pf):
    # signal:信号
    # Fs：采样率
    # pf：是否绘图
    
    L=signal.size # 信号长度
    H=np.fft.fft(signal) # DFT
    P2=np.abs(H/L) # 双边谱
    P1=P2[0:L//2] # 单边谱
    P1[1:-2]=2*P1[1:-2]
    
    f=Fs*np.arange(0,L//2)/L # 真实频率轴 Hz/s
    # f=2*math.pi*Fs*np.arange(0,L//2)/L # 角频率轴 rad/s
    
    if pf==True:
        plt.figure() # 新画布
        plt.plot(f,P1)
        plt.title("DFT单边谱")
        plt.xlabel("f(Hz)")
        plt.ylabel("|P1(f)|")
    else:
        pass


#--------------------相关度分析--------------------#





if __name__ == "__main__":
    x=np.arange(0,1000)*1/100 # 时间向量
    signal=30*np.sin(26*x)+15*np.sin(40*x)+40*np.sin(60*x)+60*np.sin(50*x) # 信号    
    saft(signal,100,True)