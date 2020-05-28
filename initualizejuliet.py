import os

##############################################################
######Check Model. 
def CheckMyModel():
    if not os.path.exists("model-en"):
        print ("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases and unpack as 'model-en' in the current folder.")
        exit(1)
##############################################################
######End Check Model.
