

'''
   The julibrain module contains command-word/action pairs.

'''

# Import all the required modules.
# Pyaudio is for the microphone and may be required by mpg123.
# Pyautogui is for moving the mouse around
#  robotically and automating key presses.
# Subprocess is for running operating system commands and programs.
# Os is for access operating system calls.  For example, it is
# used to get the current working directory.
# Webrowser is used to open and control whatever your default webbrowser is.
# The time module give us access to time related functionality.
# Re is python3's regular expression module.
# Requests is used for making get requests to http servers.
# Wikipedia is python3's module to access Wikipedia's API.
# Random access's random generator functionality.
# Psutils adds process utilities -- access information about
# processes running on the system.
# Sys adds access to system commands. I don't seem to be using this
# module.  (Possibly remove.)
# SpeakAndHear is a local module.  You'll find this is the
# SpeakAndHear subdirectory.
# SkeakAndHear has modules for speech to text and text to speech.
# GreyMatter is the program's brain.  It contains a
# large if statement that contains
# all the keywords and subsequent actions. I shouldn't need to load
# this, as I'm in this file already.
# (Possibly delete "import GreyMatter.")

##############################################################

# import pyaudio
import pyautogui
import subprocess
# import os
import webbrowser
# from time import localtime, strftime, sleep
from time import sleep
import re
# import requests
import wikipedia
from random import randrange
# import psutil
# import sys  (Possibly delete this line.)
from SpeakAndHear import talktome
# from GreyMatter import julibrain  (Possibly delete this line.)
#############################################################
# end import statements
##############################################################

#############################################################
# This is Juliet's brain.
# All her commands and logic are called here.
#############################################################


def cleanj(command):
    command = command.replace("julia", "")
    command = command.replace("julie", "")
    command = command.replace("julie julie", "")
    command = command.replace("julius", "")
    command = command.replace("look up", "")
    return command

# BEGIN GIGANTIC ASSISTANT FUNCTION


def assistant(command, playcounter, songs2play, runtest):
    '''
    Check if command exists and execute corresponding action.
    '''
# Big If Statement for Executing Commands

# Open Stuff
    # print("test = " + str(test) +".")

# First command. This will open reddit in your browser.
# -------------------------------------------------------------
    if 'open reddit' in command:
        url = 'https://www.reddit.com/'
        if not runtest:
            webbrowser.open(url)
            print('Done!')
            talktome.talkToMe('reddit is opening.')
        if runtest:
            return url
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command. This will open youtube in your brower.
# -------------------------------------------------------------
    if 'open youtube' in command:
        url = 'https://www.youtube.com/'
        if not runtest:
            webbrowser.open(url)
            print('Done!')
            talktome.talkToMe('youtube is opening.')
        if runtest:
            return url
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command. This will open Google Docs and activate the microphone.
# The first time you use this, you will need to give Google permission to
# access the microphone.
# -------------------------------------------------------------
    if 'dict' in command:
        talktome.talkToMe(
            'Opening a new document. After the new document is open you can ask me to open the microphone.')
        url = 'https://docs.google.com/document/u/0/'
        webbrowser.open(url)
        # Maximize the window
        pyautogui.hotkey('winleft', 'up')
        # I have a 4k display.  You may need to find
        # your own point.  I used
        # xdotool getmouselocation --shell
        # to find the location where to click
        # change duration if your internet is slow.
        # The lines below click on new document
        pyautogui.moveTo(777, 777, duration=.4)
        pyautogui.click()
        pyautogui.click()
        return url
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command Will open whatever website you request --
# requires you to say dot com, etc.
# -------------------------------------------------------------
    if 'search' in command:
        url = 'https://google.com'
        webbrowser.open_new_tab(url)
        # Maximize the window
        pyautogui.hotkey('winleft', 'up')
        # I have a 4k display.  You may need to find
        # your own point.  I used
        # xdotool getmouselocation --shell
        # to find the location where to click
        # change duration if your internet is slow.
        pyautogui.moveTo(2716, 1209, duration=.3)
        pyautogui.click()
        pyautogui.moveTo(1302, 546, duration=.3)
        pyautogui.click()
        pyautogui.moveTo(2716, 1209, duration=.3)
        pyautogui.click()
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command will open microphone in Google Docs.
# -------------------------------------------------------------
    if 'microphone' in command:
        pyautogui.hotkey('ctrl', 'S')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command will open a new terminal, and tile it to the right.
# -------------------------------------------------------------
    elif 'terminal' in command:
        # subprocess.call(["terminator"])
        subprocess.call(['terminator', '-T', 'First'])
        pyautogui.moveTo(2201, 1001, duration=.1)
        pyautogui.click()
        pyautogui.hotkey('winleft', 'right')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command will open a website in browser.
# This is the general way to open ANY website.
# It uses the re (regular expressions) module.
# Learn this one.
# Rememder to use the fully qualified name.
# -------------------------------------------------------------
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# End Open Stuff

# Query Stuff

# Next command
# -------------------------------------------------------------
    elif 'look' in command:
        talktome.talkToMe("Searching Wikipedia . . . ")
        command = cleanj(command)
        # results = wikipedia.summary(command, sentences=3)
        results = wikipedia.summary(command)
        wikiurl = wikipedia.page(command)
        webbrowser.open_new_tab(wikiurl.url)
        print(results)
        try:
            talktome.talkToMe(results)
        except KeyboardInterrupt:
            pass
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Play your music
# Next command will choose random songs.
# Set the number of songs in Juliet.py.  For example: songs2play = 2
# -------------------------------------------------------------
    elif 'music' in command:
        if playcounter == 1:
            talktome.talkToMe("Choosing random song . . . ")
        with open('/home/bard/Code/Juliet/mymusiclist.txt') as f:
            if playcounter == 1:
                print("Total songs to play " + str(songs2play) + ".")
            mymusic = f.read().splitlines()
            random_index = randrange(len(mymusic))
            song = mymusic[random_index]
            print("Playing song number " + str(playcounter) + ".")
            print("Song file:")
            print(song)
            playthis = 'mpg123 -q ' + song
            p1 = subprocess.Popen(playthis, shell=True)
            try:
                # while True:
                while p1.poll() is None:
                    pass
                # p1.wait()
            except KeyboardInterrupt:
                # Ctrl-C was pressed (or user knew how to send SIGTERM to the python process)
                pass  # not doing anything here, just needed to get out of the loop
            # nicely ask the subprocess to stop
            p1.terminate()
            # read final output
            sleep(1)
            # check if still alive
            if p1.poll() is not None:
                print('process terminated')
                p1.kill()
            # end new code
            if playcounter < songs2play:
                playcounter = playcounter + 1
                assistant(command, playcounter, songs2play, runtest)
            # end if
            playcounter = 1
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# End Query Stuff

# Polite Stuff
# Next command responds to Hi or Hello.
# -------------------------------------------------------------
    elif 'hello' in command or 'hi' in command:
        talktome.talkToMe(
            'Welcome.  I am Julia, your virtual artificial intelligence assistant.')
        print('Welcome.  I am Julia, your virtual artificial intelligence assistant.')
        talktome.talkToMe('How may I help you?')
        print('How may I help you?')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# Next command responds to thanks.
# -------------------------------------------------------------
    elif 'thanks' in command or 'tanks' in command or 'thank you' in command:
        talktome.talkToMe('You are welcome')
        print('You are welcome')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command chit chat
# -------------------------------------------------------------
    elif 'how are you' in command or 'and you' in command or 'are you okay' in command:
        talktome.talkToMe('Fine thank you.')
        print('Fine thank you.')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# End Polite Stuff

# Just for fun, HAL Stuff not listed in commandlist or commandlist.html.
# -------------------------------------------------------------
    elif 'open the pod door' in command:
        talktome.talkToMe('I am sorry, Dave. I am afraid I can not do that.')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command HAL stuff
# -------------------------------------------------------------
    elif 'problem' in command:
        talktome.talkToMe('I think you know as well as I do')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command HAL stuff
# -------------------------------------------------------------
    elif 'talkin' in command:
        talktome.talkToMe('This mission is too important.')
        talktome.talkToMe(' I can not to allow you to jeopardize it.')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command HAL stuff
# -------------------------------------------------------------
    elif 'why do you say that' in command:
        talktome.talkToMe('I know that you want to disconnect me.')
        talktome.talkToMe('I can not allow that.')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# End HAL Stuff

# System Commands -- This saves time at the end of the day.
# -------------------------------------------------------------
    elif 'shutdown' in command:
        subprocess.call(["shutdown -h now"])
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command -- REBOOT!
# -------------------------------------------------------------

    elif 'reboot' in command:
        subprocess.call(["reboot"])
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command -- Stop Juliet completely.
# -------------------------------------------------------------
    elif 'stop' in command or 'stopped' in command or "listening" in command:
        talktome.talkToMe("Goodbye, Sir, powering off")
        print("Goodbye, Sir, powering off")
        quit()
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# End System Commands -- Hands-free clicking.

# Interface With Desktop -- Clicking, tiling windows, and maximize.
# -------------------------------------------------------------
    elif 'click' in command:
        pyautogui.click()
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command -- Right click is "other" because "right" tiles a window.
# -------------------------------------------------------------
    elif 'other' in command:
        pyautogui.rightClick()
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command -- Middle click.
# -------------------------------------------------------------
    elif 'middle' in command:
        pyautogui.middleClick()
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command -- Tile window to the right.
# -------------------------------------------------------------
    elif 'right' in command:
        pyautogui.moveTo(400, 400, duration=.1)
        pyautogui.click()
        pyautogui.hotkey('winleft', 'right')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command -- Tile window to the left.
# -------------------------------------------------------------
    elif 'left' in command:
        pyautogui.moveTo(2200, 1000, duration=.1)
        pyautogui.click()
        pyautogui.hotkey('winleft', 'left')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command -- Maximize window.
# This is used a lot so that pyautogui can find controls.
# -------------------------------------------------------------
    elif 'maximize' in command:
        pyautogui.click()
        pyautogui.hotkey('winleft', 'up')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command -- Minimize window (hide.)
# -------------------------------------------------------------
    elif 'minimize' in command:
        pyautogui.click()
        pyautogui.hotkey('winleft', 'h')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# End Interface With Desktop

# Help Section
# -------------------------------------------------------------
    elif 'help' in command:
        talktome.talkToMe("The wake word is Julia")
        talktome.talkToMe("You can also use Juliet, Julius, or Julie")
        talktome.talkToMe("Julie Julie works best, however")
        talktome.talkToMe("You can always say Julie Julie HELP.")
        talktome.talkToMe("Julia also runs the listed commands that follow")
        talktome.talkToMe("Also, you can always say Julie Julie list commands.")
        talktome.talkToMe("You can ask Julia to")
        with open("commandlist") as file:
            for line in file:
                talktome.talkToMe(line)
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Next command -- List commands uses the commandlist file
# If you add commands to juliebrain.py,
# also ad the command name to commandlist.
# -------------------------------------------------------------
    elif 'commands' in command:
        talktome.talkToMe("You can ask Julia to")
        with open("commandlist") as file:
            for line in file:
                # line = line.strip()
                talktome.talkToMe(line)
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# End Help Section

# Miscelaneous -- Because it's short and runs fast,
# this is a great command to test the system.
# -------------------------------------------------------------
    elif 'what\'s up' in command:
        talktome.talkToMe('Just doing my thing')
# -------------------------------------------------------------
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# End Miscelaneous Section

# END GIGANTIC ASSISTANT FUNCTION -- as of 4/24/20,
# there are 26 commands in this brain.
#############################################################
