# imports
import sys
import platform
import time
from datetime import datetime as dt

hostFile = None
redirectIP = '127.0.0.1'
website_list=['www.facebook.com']

if platform.system() == 'Windows':
    hostFile = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Darwin": #MacOS
    hostFile = "/etc/hosts"

def isDuringWorkHours():
    start = dt( dt.now().year, dt.now().month, dt.now().day, 8)
    end = dt(dt.now().year, dt.now().month, dt.now().day, 16)
    currentTime = dt.now()

    if start < currentTime and currentTime < end:
        return True
    return False

def blockWebsites():
    with open(hostFile, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirectIP + " " + website + "\n")

def removeBlockedWebsites():
    with open(hostFile, 'r+') as file:
        content = file.read()
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()

def main():
    while True:
        if isDuringWorkHours():
            print("Blocking websites")
            blockWebsites()
        else:
            print("After hours...")
            removeBlockedWebsites()
    time.sleep(5)

if __name__ == '__main__':
    if hostFile is None:
        print('Cannot determine hostfile')
        sys.exit(1)
    main()
