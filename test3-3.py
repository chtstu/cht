from thinkdsp import decorate
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import SinSignal
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import SawtoothSignal
import numpy as np
import matplotlib.pyplot as plt


triangle = TriangleSignal(440).make_wave(duration=0.01)
triangle.plot()
decorate(xlabel='Time (s)')
spectrum = triangle.make_spectrum()
print(spectrum.hs[0])
spectrum.hs[0] = 100
triangle.plot(color='gray')
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')
plt.show()