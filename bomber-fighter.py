#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import random
import math
XB=[80,90,99,108,116,125,133,141,151,160,169,179,180]#position
YB=[-2,-5,-9,-15,-18,-23,-29,-28,-25,-21,-20,-17]
vf=20
time=0
flag=0
xf=0
yf=50
y=math.sqrt((0-xf)**2+(0-yf)**2)#distan from orgin
xb=80 #bomber initial
yb=0
while flag==0:
    dis=math.sqrt((xf-xb)**2+(yf-yb)**2)
    if(dis<=10):
        print("The Bomber Shutdown and Time and distance:",time,dis )
        x=math.sqrt((0-xb)**2+(0-yb)**2)
        a=np.linspace(x,0,20)
        b=np.linspace(0,y,20)
        plt.plot(a,b,color='blue',label='Success')
        plt.grid()
        plt.legend()
        flag=1
    elif(time>11):
        print("The Bomber plane in escape:",time,dis)
        flag=1
    else:
        
        xf=xf+vf*((xb-xf)/dis)
        yf=yf+vf*((yb-yf)/dis)
        x=math.sqrt((0-xb)**2+(0-yb)**2)
        a=np.linspace(x,0,30)
        b=np.linspace(0,y,30)
        plt.plot(a,b,color='red',label='Miss')
        plt.legend()
        plt.grid()
        xb=XB[time]
        yb=XB[time]
        time=time+1
        print(time,xb,yb)


# In[ ]:




