import numpy as np
import wave
from scipy.signal import chirp

def save_wav(file_path, data, sample_rate=44100):
    with wave.open(file_path, 'wb') as wav_file:
        n_channels = 1  # 1 para audio mono, 2 para audio estéreo
        sample_width = 2  # 2 bytes por muestra para formato PCM de 16 bits
        n_frames = len(data)
        comptype = 'NONE'
        compname = 'not compressed'
        wav_file.setparams((n_channels, sample_width, sample_rate, n_frames, comptype, compname))
        wav_file.writeframes(data.tobytes())

if __name__ == "__main__":
    # Frecuencias inicial y final (en Hz)
    start_frequency = 50.0
    end_frequency = 5000.0

    # Duración total de la onda (en segundos)
    total_duration = 10.0

    # Tasa de muestreo del audio (en Hz)
    sample_rate = 44100

    # Crea una señal de chirp (sin ruido) con las frecuencias deseadas
    t = np.linspace(0, total_duration, int(total_duration * sample_rate), endpoint=False)
    signal = chirp(t, f0=start_frequency, f1=end_frequency, t1=total_duration, method='linear')

    # Normaliza la señal para que esté en el rango [-1, 1]
    signal /= np.max(np.abs(signal))

    # Guarda la señal en un archivo WAV
    save_wav("sinusoidal_wave.wav", (signal * 32767).astype(np.int16), sample_rate)
