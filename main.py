import subprocess
import threading
import time

def closeScriptAndLaunchAnother(newScript="start.py"):
    print(f"Closing & Launching {newScript}")
    time.sleep(1)
    subprocess.Popen(["python", newScript])
    exit()


def checkForUpdates():
    commitDiffCommand = "git rev-list --count --left-right @{u}...HEAD"
    pullOutput = subprocess.check_output(commitDiffCommand, shell=True, text=True)
    commitsBehind = int(pullOutput.split("\t")[0])
    
    print(f"Checking if we are behind... {pullOutput}")
    
    if commitsBehind > 0:
        print(f"We are {commitsBehind} commits behind!")
        closeScriptAndLaunchAnother("start.py")
        #exit()

    threading.Timer(1, checkForUpdates).start()

checkForUpdates()

print("Hello, World! Main.py here!")