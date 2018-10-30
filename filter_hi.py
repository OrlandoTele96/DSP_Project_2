#Bibliotecas
import numpy
import wave
import struct
from scipy import signal

#Parámetros del filtro medios-graves.
fl=5000.0
fu=20000.0
fs=44100.0
fnyq=fs/2
finf=fl/fnyq
fsup=fu/fnyq
#Declarando el filtro de medios-graves[200-1000].
b4,a4=signal.butter(3,[finf,fsup],btype='band',analog=False)
G4=0.1
edo = numpy.zeros(6)
