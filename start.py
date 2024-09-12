import os
import subprocess
import time


def closeScriptAndLaunchAnother(newScript="start.py"):
    print(f"Closing & Launching {newScript}")
    time.sleep(1)
    subprocess.Popen(["python", newScript])
    exit()

# Pull any updates!
pullCommand = "git pull"
#os.system(pullCommand)

noUpdatesOutput = "Already up to date."

try:
    pullOutput = subprocess.check_output(pullCommand, shell=True, text=True)
except:
    pullOutput = noUpdatesOutput + "\n"

firstLineOfPullOutput = pullOutput.split("\n")[0]

didUpdate = firstLineOfPullOutput != noUpdatesOutput

if didUpdate:
    print("Not up to date, restarting")
    os.system(pullCommand)
    #print("Restarting Raspberry Pi in order to make sure changes are applied!")
    #os.system("sudo reboot")
    #exit()
    closeScriptAndLaunchAnother("start.py")
    

print("Everything is up to date! Now entering main program!")
#os.system("python main.py")
closeScriptAndLaunchAnother("main.py")