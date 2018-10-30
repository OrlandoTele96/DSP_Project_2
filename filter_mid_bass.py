#Bibliotecas
import numpy
import wave
import struct
from scipy import signal

#Parámetros del filtro medios-graves.
fl=200.0
fu=1000.0
fs=44100.0
fnyq=fs/2
finf=fl/fnyq
fsup=fu/fnyq
#Declarando el filtro de medios-graves[200-1000].
b2,a2=signal.butter(3,[finf,fsup],btype='band',analog=False)
edo = numpy.zeros(6)
G2=0.8

#Lector
lector = wave.open('whitenoise.wav','rb')

#Escritor
escritor = wave.open('mediosgraves.wav','wb')

#subespacio de cabecera
escritor.setparams(lector.getparams())

#Espacio de muestras
strAudioPackage = lector.readframes(16)

while len(strAudioPackage)==2*16:
    #Decodificacion
    audioPackage = struct.unpack(16*'h',strAudioPackage)


    #filtrado
    audioPackage,edo=signal.lfilter(b2*G2,a2,audioPackage,zi=edo)

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
