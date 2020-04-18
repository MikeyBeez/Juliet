###############################################################################################
######## STT SPEECH TO TEXT FUNCTION THAT RETURNS THE VARIABLE: command
import pyaudio
from vosk import Model, KaldiRecognizer

def myCommand():
    # "listens for commands"
    # We imported vosk up above.
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    model = Model("model-en")
    rec = KaldiRecognizer(model, 16000)
    while True:
        data = stream.read(2000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
        #print(rec.Result())
        # I commented out this line and added the 3 lines below
            myResult = rec.Result()
            myList = myResult.split("text")
            command = myList[1]
            return command
######## END STT SPEECH TO TEXT FUNCTION THAT RETURNS THE VARIABLE: command
###############################################################################################