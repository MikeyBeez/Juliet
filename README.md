# Juliet
At the moment, I am beginning to port this over from Otto3.  I use a female voice; so calling her Otto makes no sense.  It's also an opportunity to refactor my code, and cleanup the installation process. Thast means this repo is not ready for prime time.

Virtual Assistant with STT and TTS

Juliet answers to any name starting Juli.  So you can say "Juli Help," or "Julie Help," or "Juliet Help," or "Julius Help."

Juliet requires quite a few packages and programs to run.  I've built Juliet on Ubuntu 18.04.  I have a modern Logitek Webcam and integrated microphone, but any microphone should work.  The pyaudio program is used to access the microphone.  I recommend doing everything inside a virtual environment.  I use miniconda.  BTW, I am programming this at home.  I don't have a team, and I don't have a lab with multiple systems with different linuxes and different hardware.  I have a lot of programs and modules installed.  I don't know how my particular system is effecting this program as a unique environment.  Therefore, I'd be very interested in hearing about your experiences.  You can create a Github issue in this repository to leave your experiences.  

Juliet requires git and python3. I use miniconda to create a virtual environment. On my own system, I create a directory.  You should fork my repository,  Then clone your fork. 
  6
  5 sudo apt install git
  4
  3 mikdir ~/Code
  2 cd ~/Code
  1 git clone <Insert your url of the forked repository here>  # it should look something like this:  https://github.com/MikeyBeez/Juliet.git
18  cd Juliet
# I make a conda environment from the included yaml file.  There are probably more modules here than you need.  In any case, create a virtual environment any way you want, with virtualenv, Venv, Anaconda, or Miniconda.  I used Miniconda because it doesn't mess up Lambda Lab's Lambda Stack. 
  1 conda env create --file=Juliet.yaml
  # I need to cleanup this yaml file.  It has all my site packages too.
  The frustrating part is that I will need to set this up from scratch in a virtual machine before it's ready for the wild.  Then I can prune this down to the minimum.   

