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

# Import system modules.
import os
# Import my own modules in sub directories.
from SpeakAndHear import talktome
from SpeakAndHear import mycommand
from GreyMatter import julibrain
# Import my own modules in this directory.
import initualizejuliet as ij

################################################################################################
###### Start myVars.
def myVars():
    # Current working directory.
    myDir = os.getcwd()
    # Global variables that control how many songs are played at a time (Julia play music.)
    global playcounter 
    playcounter = 1
    # totalsongstoplay is set below in main()
    global totalsongstoplay 
################################################################################################
###### End myVars.

######## START MAIN PROGRAM.
def main():
    # Initialize.
    myVars()
    try:
        #kaldi.Recognizer requires a model.  Make sure we have it.  Otherwise say where to get it.
        ij.CheckMyModel()
    except SystemExit as e:
        print(e)
    # This is where to set the number of songs to play when you say "Julie play music."     
    totalsongstoplay = 2
    # End initialize.

    # Say and print some helpful infomtion.
    talktome.talkToMe("To get started, You can say Julie Julie help.")
    print("To get started, You can say 'Julie Julie help.'")
    talktome.talkToMe("I am Julie Julie. How can I help?")  
    print("How can I help?")

    # Loop over and over to continuously execute multiple commands.
    while True:
        # listen for command. The listener logic is inside the myCommand function.
        output = mycommand.myCommand()[3:]
        # The assistant function responds to wake words "Julie," "Julia," "Julius," or "Juliet."
        # It also gets whatever else you said, like "Julie what's up?""
        if 'juli' in output:
            print('Julia responds:\n')
            # The assistant function performs whatever action is found that matches the variable named "output."
            # Also, variables are passed in case you ask to play music.
            julibrain.assistant(output, playcounter, totalsongstoplay)
            # Whatever you said is printed out, so you can see what Julie understood.
            # This will help you speak more clearly, if you see she doesn't understand.
            print(output)

        elif '""' in output:
            pass
######## END MAIN FUNCTION

# None of the code up above this line runs unless main is called.

######## CALL THE MAIN FUNCTION HERE
main()
###############################################################################################
