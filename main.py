import configparser
import os

from colorama import init
init()

config = configparser.ConfigParser()

defaultKeybinds = {
    'Keybind1': 'key1',
    'Keybind2': 'key2'
}

def printgreen(value: str) -> None:
    print(f'\033[92m{value}\033[0m')

def printred(value: str) -> None:
    print(f'\033[91m{value}\033[0m')

def verifyConfig():
    if not os.path.isfile('config.cfg'):
        with open('config.cfg', 'w') as f:
            f.close()
    config.read('config.cfg')
    if 'Keybinds' not in config.sections():
        config.add_section('Keybinds')
        config['Keybinds'] = defaultKeybinds
        with open('config.cfg', 'w') as f:
            config.write(f)
    config.read('config.cfg')
    for key, value in defaultKeybinds.items():
        if key not in config['Keybinds']:
            config['Keybinds'][key] = value
    with open('config.cfg', 'w') as f:
        config.write(f)

verifyConfig()

printgreen('''   _______________       ______            __
  / ____/_  __/   |     /_  __/___  ____  / /____
 / / __  / / / /| |      / / / __ \/ __ \/ / ___/
/ /_/ / / / / ___ |     / / / /_/ / /_/ / (__  )
\____/ /_/ /_/  |_|    /_/  \____/\____/_/____/
                            By KaasToast''')