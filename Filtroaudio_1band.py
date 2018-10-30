
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
edo = numpy.zeros(6)
#Parámetros del filtro medios-graves.
fl=200.0
fu=1000.0
finf=fl/fnyq
fsup=fu/fnyq
#Declarando el filtro de medios-graves[200-1000].
b2,a2=signal.butter(3,[finf,fsup],btype='band',analog=False)
#Parámetros del filtro medios-agudos.
fl=1000.0
fu=5000.0
finf=fl/fnyq
fsup=fu/fnyq
#Declarando el filtro de medios-agudos[1000-5000].
b3,a3=signal.butter(3,[finf,fsup],btype='band',analog=False)
#Parámetros del filtro agudos.
fl=5000.0
fu=20000.0
finf=fl/fnyq
fsup=fu/fnyq
#Declarando el filtro de agudos[5000-20000].
b4,a4=signal.butter(3,[finf,fsup],btype='band',analog=False)
#Lector
lector = wave.open('whitenoise.wav','rb')

#Escritor
escritor = wave.open('copiagain.wav','wb')

#subespacio de cabecera
escritor.setparams(lector.getparams())

#Espacio de muestras
strAudioPackage = lector.readframes(16)

while len(strAudioPackage)==2*16:
    #Decodificacion
    audioPackage = struct.unpack(16*'h',strAudioPackage)


    #filtrado
    audioPackage,edo=signal.lfilter(b1*0.1,a1,audioPackage,zi=edo)

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
