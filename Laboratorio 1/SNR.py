import librosa
import numpy as np

def calculate_snr(audio_path, noise_start, noise_end):
    # Cargar el archivo de audio
    audio, sr = librosa.load(audio_path, sr=None)

    # Si el archivo de audio es estéreo, promediar los canales para obtener una señal mono
    if len(audio.shape) > 1:
        audio = np.mean(audio, axis=1)

    # Cargar la sección de audio que contiene solo ruido para calcular el nivel de ruido
    noise_audio = audio[noise_start:noise_end]

    # Calcular el nivel de ruido como el valor RMS del audio de ruido
    noise_rms = np.sqrt(np.mean(noise_audio ** 2))

    # Calcular el valor RMS del audio completo para obtener la señal
    signal_rms = np.sqrt(np.mean(audio ** 2))

    # Calcular el SNR en decibelios
    snr_db = 20 * np.log10(signal_rms / noise_rms)

    return snr_db

# Ruta del archivo de audio
audio_path = 'cel_1_ruido.wav'

# Definir el inicio y final de la sección del audio que contiene solo ruido
noise_start = 10 # Puedes ajustar esto según el tiempo en segundos
noise_end = 15  # Puedes ajustar esto según el tiempo en segundos

# Calcular el SNR
snr = calculate_snr(audio_path, noise_start, noise_end)

print(f"SNR: {snr:.2f} dB")
