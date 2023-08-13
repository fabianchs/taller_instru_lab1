% Cargar el archivo de audio
archivo_audio = 'pc_1.wav'; % Cambia la ruta al archivo de audio
[y, Fs] = audioread(archivo_audio);

% Parámetros
duracion = 10; % Duración del análisis en segundos
inicio_frecuencia = 50; % Frecuencia de inicio en Hz
fin_frecuencia = 50000; % Frecuencia de fin en Hz

% Calcular la Transformada de Fourier
N = duracion * Fs; % Número de muestras para la duración deseada
f = linspace(inicio_frecuencia, fin_frecuencia, N);
Y = fft(y(1:N));
P = abs(Y/N);

% Graficar la Transformada de Fourier
figure;
semilogx(f, P, 'b');
title('Transformada de Fourier del audio con laptop');
xlabel('Frecuencia (Hz)');
ylabel('Amplitud');
grid on;

xlim([inicio_frecuencia, fin_frecuencia]);

