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
#   Welcome to Juliet -- your virtual assistant
#
#   You can say "Julia Help" to get started
#
###############################################################################################
###############################################################################################

###############################################################################################
#####myVars
def myVars():
    myDir = os.getcwd()
    global playcounter 
    playcounter = 0
    wakeWord = "juli" 
###############################################################################################
#####end myVars 

######## START MAIN PROGRAM
def main():
    myVars()
    #loop to continue executing multiple commands
    #talkToMe("To get started, You can say julia help.")
    print("To get started, You can say 'Julia help.'")
    talktome.talkToMe("Hello, Sir.  How can I be of assistance?")
    print("Hello, Sir.  How can I be of assistance?")

    while True:
        output = mycommand.myCommand()[3:]
        # respond to Julie, Julia, Julius, or Juliet
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
