###############################################################################################
######## STT SPEECH TO TEXT FUNCTION THAT RETURNS THE VARIABLE: command
import pyaudio
from vosk import Model, KaldiRecognizer

################################################################################################
######Check Model 
def CheckMyModel():
    if not os.path.exists("../model-en"):
        print ("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases and unpack as 'model-en' in the current folder.")
        exit(1)
################################################################################################
######End Check Model 



def myCommand():
    # "listens for commands"
    # We imported vosk up above.
    try:
        CheckMyModel()
        print("checking model")
    except SystemExit as e:
        print(e)
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
            stream.stop_stream()
            stream.close()
            p.terminate()
            return command
######## END STT SPEECH TO TEXT FUNCTION THAT RETURNS THE VARIABLE: command
###############################################################################################