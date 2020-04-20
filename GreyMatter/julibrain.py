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
from SpeakAndHear import talktome
from GreyMatter import julibrain
###############################################################################################
################################################################################################
#####myVars
#def myVars():
#    myDir = os.getcwd()
#    global playcounter 
#    playcounter = 0
#    wakeWord = "juli" 
################################################################################################
###############################################################################################
####Check if a process is already running
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
###############################################################################################
####End Check if a process is already running


###############################################################################################
# This is Juliet's brain.
# All her commands and logic are called here.
###############################################################################################


######## BEGIN GIGANTIC ASSISTANT FUNCTION
def assistant(command, playcounter,totalsongstoplay):
######## Big If Statement for Executing Commands

######## Open Stuff
    if 'open reddit' in command:
        #reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        #if reg_ex:
        #    subreddit = reg_ex.group(1)
        #    url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
        talktome.talkToMe('reddit is opening, shit head!')
# next command
    if 'open youtube' in command:
        url = 'https://www.youtube.com/'
        webbrowser.open(url)
        print('Done!')
        talktome.talkToMe('youtube is opening, shit head!')
# next command
    if 'dictation' in command:
        url = 'https://docs.google.com/document/u/0/'
        webbrowser.open(url)
        print('Done!')
        talktome.talkToMe('Opening a new document, Sir.')
        # Maximize the window
        pyautogui.hotkey('winleft', 'up')
        # I have a 4k display.  You may need to find 
        # your own point.  I used 
        # xdotool getmouselocation --shell
        # to find the location where to click
        # change duration if your internet is slow.
        pyautogui.moveTo(777, 777, duration=.3)
        pyautogui.click()
# next command
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
# next command
    if 'microphone' in command:
        pyautogui.hotkey('ctrl', 'S')
# next command
    elif 'terminal' in command:
        #subprocess.call(["terminator"])
        subprocess.call(['terminator','-T', 'First'])
        pyautogui.moveTo(2201, 1001, duration=.1)
        pyautogui.click()
        pyautogui.hotkey('winleft', 'right')
# next command
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass
######## End Open Stuff
######## Query Stuff
    elif 'wikipedia' in command:
        talktome.talkToMe("Searching Wikipedia . . . ")
        command = command.replace("julia", "")
        command = command.replace("julius", "")
        command = command.replace("wikipedia", "")
        try:
            results = wikipedia.summary(command)
            wikiurl = wikipedia.page(command)
            webbrowser.open_new_tab(wikiurl.url)
            print(results)
            talktome.talkToMe(results)
        except:
            print("Disambiguation error") 
            talktome.talkToMe("Disambiguation error") 
# next command
    elif 'look up' in command:
        talktome.talkToMe("Searching Wikipedia . . . ")
        command = command.replace("julia", "")
        command = command.replace("julius", "")
        command = command.replace("look up", "")
        results = wikipedia.summary(command, sentences = 3)
        wikiurl = wikipedia.page(command)
        print(wikiurl.url)
        webbrowser.open_new_tab(wikiurl.url)
        print(results)
        talktome.talkToMe(results)
# next command
    elif 'music' in command:
        if playcounter == 1:
            talktome.talkToMe("Choosing random song . . . ")
        with open('/home/bard/Code/Otto3/mymusiclist.txt') as f:
            if playcounter = 1:
                print("Total songs to play " + str(totalsongstoplay) + ".")
            mymusic = f.read().splitlines()
            random_index = randrange(len(mymusic))
            song = mymusic[random_index]
            print("Playing song number " + str(playcounter) + ".")
            print("Song file:")
            print(song)
            playthis = 'mpg123 -q ' + song
            subprocess.call(playthis, shell=True)
            if playcounter < totalsongstoplay:
                playcounter = playcounter + 1
                assistant(command, playcounter, totalsongstoplay)
            else:
                playcounter=1
# next command
######## End Query Stuff

######## Polite Stuff
    elif 'hello' in command or 'hi' in command:
        talktome.talkToMe('Welcome.  I am Julia, your virtual artificial intelligence assistant.')
        print('Welcome.  I am Julia, your virtual artificial intelligence assistant.')
        talktome.talkToMe('How may I help you?')
        print('How may I help you?')
    
# next command
    elif 'thanks' in command or 'tanks' in command or 'thank you' in command:
        talktome.talkToMe('You are welcome')
        print('You are welcome')

# next command
    #elif 'julia' in command:
    #    talkToMe('Yes Sir? What can I do for you sir?')
    #    print('Yes Sir? What can I do for you sir?')

# next command
    elif 'how are you' in command or 'and you' in command or 'are you okay' in command:
        talktome.talkToMe('Fine thank you.')
        print('Fine thank you.')

######## End Polite Stuff

######## HAL Stuff
    elif 'open the pod door' in command:
        talktome.talkToMe('I am sorry, Dave. I am afraid I can not do that.')
    
# next command
    elif 'problem' in command:
        talktome.talkToMe('I think you know as well as I do')



# next command
    elif 'talkin' in command:
        talktome.talkToMe('This mission is too important.')
        talktome.talkToMe(' I can not to allow you to jeopardize it.')
    
# next command
    elif 'why do you say that' in command:
        talktome.talkToMe('I know that you want to disconnect me.')
        talktome.talkToMe('I can not allow that.')

######## End HAL Stuff

######## System Commands

    elif 'shutdown' in command:
        subprocess.call(["shutdown -h now"])

# next command

    elif 'reboot' in command:
        subprocess.call(["reboot"])

# next command

    elif 'stop listening' in command or 'stopped listening' in command:
        talktome.talkToMe("Goodbye, Sir, powering off")
        print("Goodbye, Sir, powering off")
        quit()

######## End System Commands

######## Interface With Desktop

    elif 'click' in command:
        pyautogui.click()

# next command
    elif 'other' in command:
        pyautogui.rightClick()

# next command
    elif 'middle' in command:
        pyautogui.middleClick()

# next command
    elif 'right' in command:
        pyautogui.moveTo(400, 400, duration=.1)
        pyautogui.click()
        pyautogui.hotkey('winleft', 'right')

# next command
    elif 'left' in command:
        pyautogui.moveTo(2200, 1000, duration=.1)
        pyautogui.click()
        pyautogui.hotkey('winleft', 'left')

# next command

    elif 'maximize' in command:
        pyautogui.click()
        pyautogui.hotkey('winleft', 'up')

# next command
    elif 'minimize' in command:
        pyautogui.click()
        pyautogui.hotkey('winleft', 'h')

######## End Interface With Desktop

######## Help Section
    elif 'help' in command:
        #talkToMe("There are three different wake words")
        talktome.talkToMe("The wake word is Julia")
        talktome.talkToMe("You can also use Juliet, Julius, or Julie")
        talktome.talkToMe("You can always say JULIA HELP.")
        talktome.talkToMe("Julia also runs the listed commands that follow")
        talktome.talkToMe("Also, you can always say JULIA list commands.")
        talktome.talkToMe("You can ask Julia to")
        with open("commandlist") as file:
            for line in file:
                #line = line.strip()
                talktome.talkToMe(line)
# next command
    elif 'commands' in command:
        talktome.talkToMe("You can ask Julia to")
        with open("commandlist") as file:
            for line in file:
                #line = line.strip()
                talktome.talkToMe(line)

######## End Help SectionEND

######## Miscelaneous
    elif 'what\'s up' in command:
        talktome.talkToMe('Just doing my thing')

######## End Miscelaneous Section

######## END GIGANTIC ASSISTANT FUNCTION
###############################################################################################
