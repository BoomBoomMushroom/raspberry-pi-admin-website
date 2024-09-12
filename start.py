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
    DEVNULL = subprocess.DEVNULL
    ngrokProcess = subprocess.Popen(["python", "start_ngrok.py"], stdout=DEVNULL, stdin=DEVNULL, stderr=DEVNULL)
    
    try:
        run()
    except:
        
        pass
    
    mainPython.kill()
    ngrokProcess.kill()

# MAKE SURE start.sh IS EXECUTABLE BY:
# chmod a+x start.sh

"""
# Make the start.sh a service inside of systemd
Steps:
Create a new service file for your script:

sudo nano /etc/systemd/system/start-admin-website.service
start-admin-website.service:
```
[Unit]
Description=Run the Admin Webserver at startup
After=network-online.target

[Service]
ExecStart=/home/admin/raspberry-pi-admin-website/start.sh
ExecStartPre=/bin/sleep 2
Restart=always

[Install]
WantedBy=multi-user.target
```

Save and exit the file.

Enable the service:
    sudo systemctl enable start-admin-website.service

You can start the service immediately (without rebooting) by running:
    sudo systemctl start start-admin-website.service

To check the status of the service:
    sudo systemctl status start-admin-website.service
"""