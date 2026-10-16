import numpy as np


def compute_rms(signal):
    signal = np.asarray(signal, dtype=np.float64)
    if signal.size == 0:
        return 0.0
    return float(np.sqrt(np.mean(signal ** 2)))


def moving_average(signal, window):
    signal = np.asarray(signal, dtype=np.float64)
    if window <= 1 or signal.size == 0:
        return signal.copy()
    kernel = np.ones(window, dtype=np.float64) / window
    return np.convolve(signal, kernel, mode="same")


def compute_fft(signal, sample_rate):
    signal = np.asarray(signal, dtype=np.float64)
    n = signal.size
    if n == 0:
        return np.array([]), np.array([])
    window = np.hanning(n)
    spectrum = np.fft.rfft(signal * window)
    freqs = np.fft.rfftfreq(n, d=1.0 / sample_rate)
    magnitude = np.abs(spectrum) / (n / 2.0)
    return freqs, magnitude


def peak_frequency(freqs, magnitude):
    if freqs.size == 0 or magnitude.size == 0:
        return 0.0, 0.0
    index = int(np.argmax(magnitude))
    return float(freqs[index]), float(magnitude[index])