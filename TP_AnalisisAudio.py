# %%
import IPython.display
import matplotlib.pyplot as plt
import numpy as np
# AUDIO
import librosa
import librosa.display
import soundfile as sf
from IPython.display import Audio


audio, sr = sf.read('AnalisisTextosSampleado.wav')

#4
print("vector de audio:", audio)
print("cantidad de muestras:", len(audio))
print("Frecuencia de Muestreo:",sr)
print("Duracion:", len(audio)/sr)


#5
print("señal sonora:")
plt.plot(audio)
plt.show()


# %%
#6
print("Audio original:")
Audio(audio,rate=sr)


# %%
#7
print("Audio con mayor duracion:")
Audio(audio,rate=sr*0.5)

# %%
print("Audio con menor duracion:")
Audio(audio,rate=sr*2)



# %%
#8
print("Audio con baja calidad:")
audio_baja_calidady = (audio*2**3).astype(np.int8)
Audio(audio_baja_calidady,rate=sr)

