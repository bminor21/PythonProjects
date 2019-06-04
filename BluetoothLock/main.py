import os
import platform
import sys

# Must be running on windows
if platform.system() != 'Windows':
    print('Must be running on Windows to execute')
    sys.exit(1)

# lock the computer
def lock():
    os.system('rundll32.exe user32.dll,LockWorkStation')

if __name__ == '__main__':
    lock()
