import os
import matplotlib.pyplot as plt
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from ipywidgets import interact, fixed
from thinkdsp import SinSignal
from thinkdsp import play_wave

signal = (SinSignal(freq=400, amp=1.0) +
          SinSignal(freq=600, amp=0.5) +
          SinSignal(freq=800, amp=0.25))
plt.subplot(131)
signal.plot()

wave2 = signal.make_wave(duration=1)
wave2.apodize()
wave2.make_audio()

spectrum = wave2.make_spectrum()
plt.subplot(132)
spectrum.plot(high=2000)

signal += SinSignal(freq=550)
signal.make_wave().make_audio()
plt.subplot(133)
signal.plot()

wave2.write(filename='output1-3.wav')
#play_wave('output1-3.wav', player='')
plt.show()