import subprocess
import sys
import os
os.system('cls') # Clears the console screen
import time

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'


print(fg.BLUE + "------------------YouTube Downloader---------------\n")
print(style.RESET_ALL)



current_Folder_Location = os.getcwd()
list = []

getinput = input(fg.GREEN + " What song do you want to download? " + fg.RESET)


time.sleep(1)
print(fg.BLUE + " Searching....\n" + fg.RESET)
print(fg.YELLOW)
time.sleep(1)
print("    3")
time.sleep(1)
print("    2")
time.sleep(1)
print("    1\n")
time.sleep(1)
print(fg.RESET)
print(fg.BLUE + "Getting file download\n" + fg.RESET)


getfile = subprocess.run(['spotdl', f'{getinput}'])
time.sleep(1)
print(fg.YELLOW + f'{getinput}' + " - " + " Downloaded to " + f'{current_Folder_Location}' + "\n" + fg.RESET)


            
            
            
            
print(fg.GREEN + "--- DONE! ---")
print("-------------")
print("-------------" + fg.RESET)

time.sleep(3)
print(fg.BLUE + "\nExiting" + fg.RESET)


time.sleep(1)
sys.exit()

