import subprocess
import time
import ctypes
import sys
import os

def main():
    if ctypes.windll.shell32.IsUserAnAdmin():
        os.system("pause")
        subprocess.run(["netsh", "interface", "set", "interface", "\"Ethernet\"", "disable"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Disconnected ethernet. Sleeping for 15 seconds.")
        time.sleep(15)
        subprocess.run(["netsh", "interface", "set", "interface", "\"Ethernet\"", "enable"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == "__main__":
    main()