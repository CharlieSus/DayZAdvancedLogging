# AdvancedLogging
A python script to allow for advanced logging in DayZ

Introducing AdvancedLogging, a python based script to allow for advanced logging of DayZ logs, that attaches text files to discord webhooks.
This script will automatically monitor a specified folder path for the newest file, and monitor said file to upload the newest line in the file as a message to discord.


HOW TO SETUP

First, you need to install the requests library if you haven't already:
"pip install requests"

After downloading the AdvancedLogging.py script, there is some lines you need to change.
First changes you need to make are under "log_directories"
