#!/home/bard/miniconda3/envs/Juliet/bin/python

###############################################################################################
###############################################################################################
#
#   Welcome to Juliet -- your virtual assistant.
#
#   You can say "Julia Help" to get started.
#
###############################################################################################
###############################################################################################

import os
import sys
from SpeakAndHear import talktome
from SpeakAndHear import mycommand
from GreyMatter import julibrain
import initualizejuliet as ij

################################################################################################
###### Start myVars.
def myVars():
    myDir = os.getcwd()
    global playcounter 
    playcounter = 0
    wakeWord = "juli" 
################################################################################################
###### End myVars.

######## START MAIN PROGRAM.
def main():
    # Initialize.
    myVars()
    try:
        ij.CheckMyModel()
    except SystemExit as e:
        print(e)
    # End initialize.

    # Loop over and over to continuously execute multiple commands.

    talktome.talkToMe("To get started, You can say julia help.")
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

######## CALL FUNCTION
main()
###############################################################################################
