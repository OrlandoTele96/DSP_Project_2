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
#Lector
lector = wave.open('whitenoise.wav','rb')

#Escritor
escritor = wave.open('agudos.wav','wb')

#subespacio de cabecera
escritor.setparams(lector.getparams())

#Espacio de muestras
strAudioPackage = lector.readframes(16)

while len(strAudioPackage)==2*16:
    #Decodificacion
    audioPackage = struct.unpack(16*'h',strAudioPackage)


    #filtrado
    audioPackage,edo=signal.lfilter(b4*G4,a4,audioPackage,zi=edo)

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
