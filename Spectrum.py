import numpy as np
import pyaudio
import time

def audio_callback(in_data, frame_count, time_info, status):
    audio_data = np.frombuffer(in_data, dtype=np.float32)
    fft_data = np.abs(np.fft.fft(audio_data))[:len(audio_data)//2]
    print(fft_data)  # Here you would send this data to the Android app or visualize it
    return (in_data, pyaudio.paContinue)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                input=True,
                stream_callback=audio_callback)

stream.start_stream()

try:
    while stream.is_active():
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
p.terminate()
