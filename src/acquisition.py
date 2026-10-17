import numpy as np
import sounddevice as sd


def list_devices():
    print(sd.query_devices())


def read_block(sample_rate, block_size, channels=1, device=None):
    data = sd.rec(block_size, samplerate=sample_rate, channels=channels,
                  dtype="float32", device=device)
    sd.wait()
    if channels == 1:
        return data[:, 0]
    return data.mean(axis=1)