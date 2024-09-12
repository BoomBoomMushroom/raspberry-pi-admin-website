import os
import subprocess
import sys

try:
    # Pull any updates!
    pullCommand = "git pull"
    noUpdatesOutput = "Already up to date."

    pullOutput = subprocess.check_output(pullCommand, shell=True, text=True)
    firstLineOfPullOutput = pullOutput.split("\n")[0]

    didUpdate = firstLineOfPullOutput != noUpdatesOutput

    if didUpdate:
        print("Updated code!")
        #print("Restarting Raspberry Pi in order to make sure changes are applied!")
except:
    pass

print("Everything is up to date! Now entering main program!")
os.system("python main.py")