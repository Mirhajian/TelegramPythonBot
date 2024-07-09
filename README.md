
# Telegram Python Bot

Developed by Abolfazl Mirhajian



## Dependencies
**1. python-telegram-bot:** Library for interacting with the Telegram Bot API. Install with pip:

    • pip install python-telegram-bot

**2. All the dependencies:**

    • pip install python-telegram-bot anyio certifi h11 httpcore httpx idna sniffio "python-telegram-bot[job-queue]"




## Setup
**1. Create the bot and copy the token:** create a bot from @botFather and get the token to run the bot.

Inside main.py change the token: 

    ...
    • TOKEN = ‘YOUR_TOKEN’
    ...

**2. Run the bot:**

    • cd telegramPythonBot
    • python main.py


## Features
Introduces the bot and lists available commands.

    • /start

Commands for generating invite links, fetching bot photo, setting group profile photos, and contacting admins respectively.

    /1, /2, /3, /4 



## Virtual Env(Environment)
**1. Running the env:**

On MacOS/Linux:
    
    source myenv/bin/activate

On Windows “PowerShell”: 
    
    myenv/bin/Activate.ps1

**2. Deactivating(exiting) the myenv:**

    deactivate


## Structure
The project directory is organized as follows:
```
telegramPythonBot/
├── admin_handler.py
├── invite_link_handler.py
├── main.py
├── photo_handler.py
├── start_handler.py
├── basic/
│   └── originProject.py
├── __pycache__/
└── myenv/
    ├── Include/
    ├── Lib/
    └── bin/
        ├── activate        # activating venv for linux and osx operating systems.
        └── Activate.ps1    # activating venv for windows via powershell"
```