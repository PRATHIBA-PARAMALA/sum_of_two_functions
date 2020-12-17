import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss
def get_sin(F,Fs):
    n=np.arange(-50.0,50.0)
    x=np.sin(2*np.pi*F/Fs*n)
    return x
x1=get_sin(500,32000)
x2=get_sin(2000,32000)

x3=get_sin(1500,32000)
x4=get_sin(2000,32000)
n=np.arange(-10.0,100.0)
y=ss.square(2*np.pi*800/32000*n,duty=0.5)
plt.subplot(311);plt.plot(y)
plt.subplot(312);plt.plot(x1)
plt.subplot(313);plt.plot(x2+x1)
'''
plt.subplot(311);plt.stem(x1)
plt.subplot(312);plt.stem(x2)
plt.subplot(313);plt.stem(x3)
'''

plt.show()


