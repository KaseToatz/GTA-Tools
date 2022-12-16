from subprocess import run, PIPE
from ctypes import windll
from time import sleep
from sys import executable, argv
from os import system

def main():
    if windll.shell32.IsUserAnAdmin():
        system("pause")
        run(["netsh", "interface", "set", "interface", "\"Ethernet\"", "disable"], stdout=PIPE, stderr=PIPE)
        print("Disconnected ethernet. Sleeping for 15 seconds.")
        sleep(15)
        run(["netsh", "interface", "set", "interface", "\"Ethernet\"", "enable"], stdout=PIPE, stderr=PIPE)
    else:
        windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv), None, 1)

if __name__ == "__main__":
    main()