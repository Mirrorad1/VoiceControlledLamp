#You can import any required modules here
import subprocess
#This can be anything you want
moduleName = "lampon"

#All of the words must be heard in order for this module to be executed
commandWords = ["lamp", "on"]

def execute(command):
    subprocess.call(['lightswitch.sh', 'on'])
    print("Light is turned on now")
