import os
import subprocess

# Pull any updates!
pullCommand = "git pull"
noUpdatesOutput = "Already up to date."

pullOutput = subprocess.check_output(pullCommand, shell=True, text=True)
firstLineOfPullOutput = pullOutput.split("\n")[0]

didUpdate = firstLineOfPullOutput != noUpdatesOutput

if didUpdate:
    print("Restarting Raspberry Pi in order to make sure changes are commited!")
    os.system("sudo reboot")
    exit()


print("Everything is up to date! Not entering main program!")
os.startfile("main.py")