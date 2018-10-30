#Bibliotecas
import numpy
import wave
import struct
from scipy import signal
#Parámetros del filtro grave.
fl=20.0
fu=200.0
fs=44100.0
fnyq=fs/2
finf=fl/fnyq
fsup=fu/fnyq
#Declarando el filtro de graves[20-200].
b1,a1=signal.butter(3,[finf,fsup],btype='band',analog=False)
G1=0.9
edo = numpy.zeros(6)
#Lector
lector = wave.open('whitenoise.wav','rb')

#Escritor
escritor = wave.open('graves.wav','wb')

#subespacio de cabecera
escritor.setparams(lector.getparams())

#Espacio de muestras
strAudioPackage = lector.readframes(16)

while len(strAudioPackage)==2*16:
    #Decodificacion
    audioPackage = struct.unpack(16*'h',strAudioPackage)


    #filtrado
    audioPackage,edo=signal.lfilter(b1*G1,a1,audioPackage,zi=edo)

    #codificacion
    strAudioPackage=''.encode() #debe creae una estructura fija
    for k in audioPackage:
        strAudioPackage+=struct.pack('h',int(k))

    #escritura
    escritor.writeframes(strAudioPackage)

    #lectura
    strAudioPackage=lector.readframes(16)


#cierre
lector.close()
escritor.close()
