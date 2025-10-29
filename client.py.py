import pyttsx3
import tempfile
import os
import sounddevice as sd
import requests
from scipy.io.wavfile import write
from playsound import playsound
url="localhost url"
duration=5  # seconds
fs=44100
def record(filename):
    print("Recording...")
    audio=sd.rec(int(duration*fs),samplerate=fs,channels=1,dtype='int16')#1=mono #2=stereo
    sd.wait()
    write(filename,fs,audio)
    print("Recording complete.")
def send_audio(filename):
    with open(filename,'rb') as f:
        files={'file':f}
        response=requests.post(url,files=files)
    return response.content
def play_audio(data):
    tmp=tempfile.NamedTemporaryFile(delete=False,suffix='.wav')
    tmp.write(data)
    tmp.close()
    print("Playing response...")
    playsound(tmp.name)
    try:
        os.remove(tmp.name)
    except Exception as e:
        print(f"Error deleting temp file: {e}")
with tempfile.NamedTemporaryFile(delete=False,suffix='.wav') as tmp:
    record(tmp.name)
    response=send_audio(tmp.name)
    play_audio(response)
    try:
        os.remove(tmp.name)
    except Exception as e:
        print(f"Error deleting temp file: {e}")
