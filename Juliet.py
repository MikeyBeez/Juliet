#!/home/bard/miniconda3/envs/Juliet/bin/python

###############################################################################################
import pyaudio
import pyautogui
import subprocess 
import os
import webbrowser
from time import localtime, strftime
import re
import requests
import wikipedia
from random import randrange
import psutil
import sys
from vosk import Model, KaldiRecognizer
from SpeakAndHear import talktome
from SpeakAndHear import mycommand
from GreyMatter import julibrain
###############################################################################################
###############################################################################################
#
#   Welcome to Juliet -- your virtual assistant.
#
#   You can say "Julia Help" to get started.
#
###############################################################################################
###############################################################################################

###############################################################################################
##### Start myVars.
def myVars():
    myDir = os.getcwd()
    global playcounter 
    playcounter = 0
    wakeWord = "juli" 
###############################################################################################
##### End myVars.

################################################################################################
######Check Model. 
def CheckMyModel():
    if not os.path.exists("model-en"):
        print ("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases and unpack as 'model-en' in the current folder.")
        exit(1)
################################################################################################
######End Check Model.

######## START MAIN PROGRAM.
def main():
    # Initialize.
    myVars()
    try:
        CheckMyModel()
    except SystemExit as e:
        print(e)
    # End initialize.

    # Loop over and over to continuously execute multiple commands.

    talkToMe("To get started, You can say julia help.")
    print("To get started, You can say 'Julia help.'")
    talktome.talkToMe("Hello, Sir.  How can I be of assistance?")
    print("Hello, Sir.  How can I be of assistance?")

    while True:
        # listen for command.
        output = mycommand.myCommand()[3:]
        # Respond to wake words "Julie," "Julia," "Julius," or "Juliet."
        if 'juli' in output:
            print('The Julia responds:\n')
            julibrain.assistant(output, playcounter)
            print(output)

        elif '""' in output:
            pass
######## END MAIN FUNCTION
######## CALL MAIN FUNCTION
main()
###############################################################################################
