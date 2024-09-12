import subprocess
import threading
import time

def closeScriptAndLaunchAnother(newScript="start.py"):
    print(f"Closing & Launching {newScript}")
    time.sleep(1)
    subprocess.Popen(["python", newScript])
    exit()

def getOutputOfCommand(command):
    return subprocess.check_output(command, shell=True, text=True)

def checkForUpdates():
    fetch = getOutputOfCommand("git fetch")
    status = getOutputOfCommand("git status")
    
    #print(status)
    print("Your branch is behind" in status, "Your branch is up to date" in status)
    
    if "Your branch is behind" in status:
        print(f"We are behind on commits!")
        closeScriptAndLaunchAnother("start.py")
        #exit()

    threading.Timer(1, checkForUpdates).start()

checkForUpdates()

print("Hello, World! Main.py here!")
# to admin@piserver1