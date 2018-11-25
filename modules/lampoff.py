#You can import any required modules here
import subprocess
#This can be anything you want
moduleName = "lampoff"

#All of the words must be heard in order for this module to be executed
commandWords = ["lamp", "off"]

def execute(command):
    subprocess.call(['lightswitch.sh', 'off'])
    print("Light is turned off now")
