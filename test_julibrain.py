import unittest
from GreyMatter import julibrain
from SpeakAndHear import talktome

test = True

class TestBrain(unittest.TestCase):
    def test_open_reddit(self):
        test_error = julibrain.assistant('open reddit', 1, 2, test)
        print(self.assertEquals(test_error, 10))

        