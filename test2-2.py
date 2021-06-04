import os
import matplotlib.pyplot as plt
import thinkdsp as dsp
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from thinkdsp import play_wave
from ipywidgets import interact, fixed

wave = read_wave('C:/Users/LENOVO/Desktop/xinhao/ThinkDSP/ThinkDSP/code/18871__zippi1__sound-bell-440hz.wav')
wave.normalize()
wave.make_audio()
plt.subplot(231)
wave.plot()

segment = wave.segment(start=1.1, duration=0.5)
segment.make_audio()
plt.subplot(232)
segment.plot()
#plt.subplot(333)
#segment.segment(start=1.1, duration=0.005).plot()


spectrum = segment.make_spectrum()
plt.subplot(233)
spectrum.plot(high=7000)

spectrum.low_pass(3500)
plt.subplot(234)
spectrum.plot(high=7000)

spectrum = segment.make_spectrum()
spectrum.high_pass(3500)
plt.subplot(235)
spectrum.plot(high=7000)

spectrum = segment.make_spectrum()
spectrum.band_stop(2000,5000)
spectrum.make_wave().make_audio()
plt.subplot(236)
spectrum.plot(high=7000)

wave.write('output1-2.wav')
#play_wave('output1-2.wav', player='')
plt.show()


