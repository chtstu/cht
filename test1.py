import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,3*np.pi,100) #将[0，3Π]进行100等分
y=np.sin(x) #y=sin（x）

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文
plt.rcParams['axes.unicode_minus']=False #显示正负
plt.subplot(131) #将图片显示到第一行第一列
plt.title(r'$f(x)=sin(x)$') #显示图片标题
plt.plot(x,y)   #显示连续信号

x1=[t*0.375*np.pi for t in x] #将t转变带换成x赋值给x1
y1=np.sin(x1)
plt.subplot(132) #将图片显示到第一行第二列
plt.title(r'$f(x)=sin(\omega x),\omega=\frac{3}{8}\pi$') #显示标题
plt.plot(x,y1) #显示连续信号

x2=np.linspace(0,10)
y2=np.cos(x2)
plt.subplot(133)
plt.title(r'自己编写$y=cos(x)$')
plt.plot(x2,y2)

plt.show() #图片显示