import os
import matplotlib.pyplot as plt
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from ipywidgets import interact, fixed
from thinkdsp import SinSignal
from thinkdsp import play_wave
from IPython.display import display

wave3 = read_wave('C:/Users/LENOVO/Desktop/xinhao/ThinkDSP/ThinkDSP/code/18871__zippi1__sound-bell-440hz.wav')
wave3.normalize()
display(data=wave3.ys, rate=wave3.framerate)
wave3.make_audio()

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave3, 1)
wave3.make_audio()
plt.subplot(121)
wave3.plot()

stretch(wave3, 0.1)
wave3.make_audio()
plt.subplot(122)
wave3.plot()

wave3.write(filename='output1-4.wav')
#play_wave('output1-4.wav', player='')
plt.show()