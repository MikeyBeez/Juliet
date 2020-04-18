#!/home/bard/miniconda3/envs/Otto/bin/python3
###############################################################################################
######## IMPORT PYTHON3 MODULES
import pyaudio
from gtts import gTTS
import pyautogui
import subprocess
import os
import webbrowser
from time import localtime, strftime
import DateTime
import re
import requests
import wikipedia
from random import randrange
import psutil
import sys
from vosk import Model, KaldiRecognizer
###############################################################################################
###############################################################################################
#
#   Welcome to Juliet -- your virtual assistant
#
#   You can say "Julia Help" to get started
#
###############################################################################################
###############################################################################################

def myVars():
    myDir = os.getcwd()
    global playcounter 
    playcounter = 0
    wakeWord = "juli" 

###############################################################################################
#####Check Model 
def CheckModel():
    if not os.path.exists("model-en"):
        print ("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases and unpack as 'model-en' in the current folder.")
        exit(1)
###############################################################################################
#####End Check Model 

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
######## TTS TEXT TO SPEECH FUNCTION 

# This gets used all over to speak text aloud.
# It also prints to the console for people with bad memories.

def talkToMe(mytext):
    # "speaks audio passed as argument"
    print(mytext)
    # can handle multiline text.
    #for line in mytext.splitlines():
        # uses the google text to speech module to synthesize text
    text_to_speech = gTTS(text=mytext, lang='en-uk')
        # saves syntesized speech to audio.mp3
        # this file gets written, played. and overwritten
        # over and over again.
    text_to_speech.save('audio.mp3')
        # the sox modules wrapper is mpg123.
        # This is called by the operating system imported os module.
    os.system('mpg123 -q audio.mp3')
###############################################################################################
######## END TTS TEXT TO SPEECH FUNCTION 

###############################################################################################
######## STT SPEECH TO TEXT FUNCTION THAT RETURNS THE VARIABLE: command
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

###############################################################################################
######## BEGIN GIGANTIC ASSISTANT FUNCTION
def assistant(command, playcounter):
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
        talkToMe('reddit is opening, shit head!')
# next command
    if 'open youtube' in command:
        url = 'https://www.youtube.com/'
        webbrowser.open(url)
        print('Done!')
        talkToMe('youtube is opening, shit head!')
# next command
    if 'dictation' in command:
        url = 'https://docs.google.com/document/u/0/'
        webbrowser.open(url)
        print('Done!')
        talkToMe('Opening a new document, Sir.')
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
        talkToMe("Searching Wikipedia . . . ")
        command = command.replace("julia", "")
        command = command.replace("julius", "")
        command = command.replace("wikipedia", "")
        try:
            results = wikipedia.summary(command)
            wikiurl = wikipedia.page(command)
            webbrowser.open_new_tab(wikiurl.url)
            print(results)
            talkToMe(results)
        except:
            print("Disambiguation error") 
            talkToMe("Disambiguation error") 
# next command
    elif 'look up' in command:
        talkToMe("Searching Wikipedia . . . ")
        command = command.replace("julia", "")
        command = command.replace("julius", "")
        command = command.replace("look up", "")
        results = wikipedia.summary(command, sentences = 3)
        wikiurl = wikipedia.page(command)
        print(wikiurl.url)
        webbrowser.open_new_tab(wikiurl.url)
        print(results)
        talkToMe(results)
# next command
    elif 'music' in command:
        if playcounter == 0:
            talkToMe("Choosing random song . . . ")
        with open('/home/bard/Code/Otto3/mymusiclist.txt') as f:
            mymusic = f.read().splitlines()
            random_index = randrange(len(mymusic))
            song = mymusic[random_index]
            print(song)
            playthis = 'mpg123 -q ' + song
            subprocess.call(playthis, shell=True)
            #subprocess.Popen(playthis, shell=True)
            #proc = Popen([playthis], shell=True, stdin=None, stderr=None, close_fds=True)
            #if checkIfProcessRunning('projectM-pulseaudio'):
            #    print('Yes a projectM process was running')
            #else:
            #    print('No projectM process was running')
            #    pmcommand = 'projectM-pulseaudio 2>/dev/null'
            #    subprocess.call(pmcommand, shell=True)
            #    pyautogui.moveTo(301, 300, duration=.1)
            #    pyautogui.click()
            #    pyautogui.hotkey('winleft', 'up')
            #    pyautogui.click()
            #    pyautogui.hotkey('winleft', 'left')
            if playcounter <= 2:
                playcounter = playcounter + 1
                print(playcounter)
                assistant(command, playcounter)
            else:
                playcounter=0
# next command
######## End Query Stuff

######## Polite Stuff
    elif 'hello' in command or 'hi' in command:
        talkToMe('Welcome.  I am Julia, your virtual artificial intelligence assistant.')
        print('Welcome.  I am Julia, your virtual artificial intelligence assistant.')
        talkToMe('How may I help you?')
        print('How may I help you?')
    
# next command
    elif 'thanks' in command or 'tanks' in command or 'thank you' in command:
        talkToMe('You are welcome')
        print('You are welcome')

# next command
    #elif 'julia' in command:
    #    talkToMe('Yes Sir? What can I do for you sir?')
    #    print('Yes Sir? What can I do for you sir?')

# next command
    elif 'how are you' in command or 'and you' in command or 'are you okay' in command:
        talkToMe('Fine thank you.')
        print('Fine thank you.')

######## End Polite Stuff

######## HAL Stuff
    elif 'open the pod door' in command:
        talkToMe('I am sorry, Dave. I am afraid I can not do that.')
    
# next command
    elif 'problem' in command:
        talkToMe('I think you know as well as I do')

# next command
    elif 'talkin' in command:
        talkToMe('This mission is too important.')
        talkToMe(' I can not to allow you to jeopardize it.')
    
# next command
    elif 'why do you say that' in command:
        talkToMe('I know that you want to disconnect me.')
        talkToMe('I can not allow that.')

######## End HAL Stuff

######## System Commands

    elif 'shutdown' in command:
        subprocess.call(["shutdown -h now"])

# next command

    elif 'reboot' in command:
        subprocess.call(["reboot"])

# next command

    elif 'stop listening' in command:
        talkToMe("Goodbye, Sir, powering off")
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
        talkToMe("There are two different wake words")
        talkToMe("They are Julia, and Alice")
        talkToMe("Julia runs the listed commands that follow")
        talkToMe("You can always say JULIA HELP.")
        talkToMe("Also, you can always say JULIA list commands.")
        talkToMe("Alice is a chatbot")
        talkToMe("You can talk to Alice about anything")
        talkToMe("But she's dumber than rocks.")
        talkToMe("You can ask Julia to")

        with open("commandlist") as file:
            for line in file:
                #line = line.strip()
                talkToMe(line)
# next command
    elif 'commands' in command:
        talkToMe("You can ask Julia to")
        with open("commandlist") as file:
            for line in file:
                #line = line.strip()
                talkToMe(line)

######## End Help SectionEND

######## Miscelaneous
    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')

######## End Miscelaneous Section

######## END GIGANTIC ASSISTANT FUNCTION
###############################################################################################

######## START MAIN PROGRAM
def main():
    myVars()
    CheckModel()
    #aimylStuff()
    #print('If you are on Ubuntu, ignore the following ALSA errors')
    #print('pyaudio was compiled on a different linux')
    #print('If you can not bear them, you will need to recompile pyaudio.')
    #loop to continue executing multiple commands
    #Uncomment the following line for noobs
    #talkToMe("To get started, You can say julia help.")
    print("To get started, You can say 'Julia help.'")
    print("To get started, You can say 'Julia help.'")
    print("To get started, You can say 'Julia help.'")
    #talkToMe("Hello, Sir.  How can I be of assistance?")
    print("Hello, Sir.  How can I be of assistance?")

    while True:
        output = myCommand()[3:]
        if 'juli' in output:
            print('The Julia responds:\n')
            assistant(output, playcounter)
            print(output)

        elif '""' in output:
            pass
#            print('Alice says:')
#            response = brainkernel.respond(output)
#            talkToMe(response)
#            print(response)
#
#  I removed the following help function and the wake word "help"
#  It was starting accidentially, triggered by normal conversation.
#  Now you must say "julia help" to get this functionality.
#
#            elif 'help' in output:
#                talkToMe("There are three different wake words")
#                talkToMe("They are Help, Julia, and Alice")
#                talkToMe("Julia runs the listed commands that follow")
#                talkToMe("Also, you can always say JULIA list commands.")
#                talkToMe("Alice is a chatbot")
#                talkToMe("You can talk to Alice about anything")
#                talkToMe("But she's dumber than rocks.")
#                talkToMe("Say ALICE, what's the capital of England?")
#                talkToMe("To repeat this and get the list of commands,")
#                talkToMe("say, JULIA HELP")
#                talkToMe("Remember, the list is for the JULIA wake word.")

######## END MAIN FUNCTION
######## CALL MAIN FUNCTION
main()
###############################################################################################
