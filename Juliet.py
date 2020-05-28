#!/usr/bin/env python

#############################################################
#############################################################
#
#   Welcome to Juliet -- your virtual assistant.
#   I'm hoping this code will read a lot like a
#   book on computer science.  I hope to include enough
#   comments to make this code easy to understand and
#   modify.
#
#   You can say "Julia Help" to get started.
#
#############################################################
#############################################################

# Import system modules.
# import os
# Import my own modules in sub directories.
from SpeakAndHear import talktome
from SpeakAndHear import mycommand
from GreyMatter import julibrain
# Import my own modules in this directory.
import initualizejuliet as ij

##############################################################
# Start myVars.


def myVars():
    # Global variables that control how many songs are
    # played at a time for "Julia play music."
    global playcounter
    # songs2play used below in main().
    global songs2play
##############################################################
# End myVars.

# START MAIN PROGRAM.
# only definitions for variables and functions happen
# above this.  Nevertheless, this code doesn't run either
# until it is called at the bottom of this file.
# Similarly, this file will be called by some sort of
# front-end.  Currently, only startJuliet.sh exists
# to do that.


def main():
    # Initialize.
    myVars()
    playcounter = 1
    # This is where to set the number of songs
    # to play when you say "Julie play music."
    songs2play = 2
    try:
        # kaldi.Recognizer requires a model.  Make sure
        # we have it.  Otherwise say where to get it.
        # The vosk module:
        # https://github.com/alphacep/vosk-api
        #  contains the recognizer module
        # that uses the model built by Alphacephei:
        # https://alphacephei.com/en/
        # I find it works very well for my voice.
        # Alphacephei do have other models however
        # if this one doesn't work well for you.
        ij.CheckMyModel()
    except SystemExit as e:
        print(e)
    # End initialize.

    # Say and print some helpful infomtion.
    # If you get sick of hearing this every time you start
    # just comment it out.  Conversely, feel free to add
    # additional messages with the print and talktome.
    talktome.talkToMe("I am Julie Julie. How can I help?")
    print("How can I help?")
    # functions.
    talktome.talkToMe("To get started, You can say Julie Julie help.")
    print("To get started, You can say 'Julie Julie help.'")
    # Also feel free to write some code to supress messages
    #  after the first use.  Eventuall, I will add a
    #  database and facial recognition so that the
    #  experience can be customized by user.
    # Loop over and over to continuously execute multiple commands.
    while True:
        # listen for command. Speech to text listener
        # logic is called from inside the myCommand function.
        output = mycommand.myCommand()[3:]
        # Remember,  the mycommand function takes in
        # audio from the microphone and returns text.
        # Therefore, the "output" variable is text.
        if 'juli' in output:
            print('Julia responds:\n')
        # The assistant function responds to wake words
        # "Julie," "Julia," "Julius," or "Juliet."
        # It also gets whatever else you said, like
        # "Julie what's up?"
        # If a wake word isn't found in what you
        # said, nothing is done.
        # The assistant function performs whatever
        # action is found that matches the variable named "output."
        # Also, other variables are parsed out and passed
        #  in case you ask to play music.
        # Don't run code for unit testing
            runtest = False
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # We wrap code that may fail in try blocks.
        # That way, if the code fails, our program doesn't
        # crash.  It simply prints out there's been an
        # error, etc.
        # The assistant function is in the julibrain.py
        # file.  It needs four arguments.
        # It needs the text in the "output" variable
        # so it can figure out what actions to perform.
        # It needs the playcounter and songs2play
        # variables for playing music.
        # And it needs the runtest variable to turn on
        # and off some of the actions.
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            try:
                julibrain.assistant(output, playcounter, songs2play, runtest)
            except Exception as e:
                print(e)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

            # Whatever you said is printed out,
            # so you can see what Julie understood.
            # This may show you what to speak more clearly,
            # if you see she doesn't understand.
            print(output)

# END MAIN FUNCTION

# None of the code up above this line runs unless main is called.


# CALL THE MAIN FUNCTION HERE
main()
