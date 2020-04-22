import unittest
import subprocess
from GreyMatter import julibrain
from SpeakAndHear import talktome


class TestBrain(unittest.TestCase):
    def test_open_reddit(self):
        test = True
        testurl = julibrain.assistant('open reddit', 1, 2, test)
        #subprocess.call(['pip', 'list', '|', 'grep', 'webbrowser'])
        self.assertEqual(testurl, 'https://www.reddit.com/')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
    def test_open_youtube(self):
        test = True
        testurl = julibrain.assistant('open youtube', 1, 2, test)
        #subprocess.call(['pip', 'list', '|', 'grep', 'webbrowser'])
        self.assertEqual(testurl, 'https://www.youtube.com/')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    
    def dictation(self):
        test = True
        testurl = julibrain.assistant('dict', 1, 2, test)
        self.assertEqual(testurl, 'https://docs.google.com/document/u/0/')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^