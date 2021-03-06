import os
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import SinSignal
from thinkdsp import Chirp
from thinkdsp import normalize, unbias
from thinkdsp import read_wave


wave = read_wave('F:/宁理/xinhao/ThinkDSP/ThinkDSP/code/72475__rockwehrmann__glissup02.wav')
wave.make_audio()

wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')

plt.show()