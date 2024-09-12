import os
import subprocess
import time
import start_ngrok

pullCommand = "git pull"

def installRequirements():
    os.system("pip install -r requirements.txt")

def updateCode():
    # Pull any updates!
    #os.system(pullCommand)

    noUpdatesOutput = "Already up to date."

    try:
        pullOutput = subprocess.check_output(pullCommand, shell=True, text=True)
    except:
        pullOutput = noUpdatesOutput + "\n"

    firstLineOfPullOutput = pullOutput.split("\n")[0]

    didUpdate = firstLineOfPullOutput != noUpdatesOutput

    return didUpdate

mainPython = None

def run():
    global mainPython
    
    while True:
        #print("Everything is up to date! Now entering main program!")
        time.sleep(1)
        
        mainPython = subprocess.Popen(["python", "main.py"])
        while True:
            # Poll the current status of Main.py. If dead, restart it
            mainStatus = mainPython.poll()

            if mainStatus == None:
                #print(f"Main.py is running, and is alive! Poll Status: {mainStatus}")
                pass
            else:
                mainPython.kill()
                #print(f"Main.py is dead, restarting... Poll Status: {mainStatus}")
                break

            
            # Check if we need to update our code. If so, kill main.py and restart
            didUpdate = updateCode()
            if didUpdate:
                print("Not up to date, restarting")
                os.system(pullCommand)
                mainPython.kill()

                time.sleep(3)
                installRequirements()
                break

            # Run this staus check and update check loop every 2 seconds
            time.sleep(2)


if __name__ == "__main__":
    #start_ngrok.start()
    ngrokProcess = subprocess.Popen(["python", "start_ngrok.py"])
    
    try:
        run()
    except:
        
        pass
    
    mainPython.kill()
    ngrokProcess.kill()