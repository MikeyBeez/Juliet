#############################################################
# TTS TEXT TO SPEECH FUNCTION

# This gets used all over to speak text aloud.
# It also prints to the console for people with bad memories.

from gtts import gTTS
import os


def talkToMe(mytext):
    # "speaks audio passed as argument"
    print(mytext)
    # can handle multiline text.
    # for line in mytext.splitlines():
    # uses the google text to speech module to synthesize text
    text_to_speech = gTTS(text=mytext, lang='en-uk')
    # saves syntesized speech to audio.mp3
    # this file gets written, played. and overwritten
    # over and over again.
    text_to_speech.save('audio.mp3')
    # the sox modules wrapper is mpg123.
    # This is called by the operating system imported os module.
    os.system('mpg123 -q audio.mp3')
#############################################################
# END TTS TEXT TO SPEECH FUNCTION
