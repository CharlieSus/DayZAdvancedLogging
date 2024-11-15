# AdvancedLogging
A python script to allow for advanced logging in DayZ

Introducing AdvancedLogging, a python based script to allow for advanced logging of DayZ logs, that attaches text files to discord webhooks.
This script will automatically monitor a specified folder path for the newest file, and monitor said file to upload the newest line in the file as a message to discord.


HOW TO SETUP

First, you need to install the requests library if you haven't already:
"pip install requests"

After downloading the AdvancedLogging.py script, there is some lines you need to change.
First changes you need to make are under "log_directories"
![Screenshot_489](https://github.com/user-attachments/assets/766e8aa7-dedd-4cee-a625-5e5392091cbd)

This is where you will put the file paths to your log directories. It should look like the following example below.
![Screenshot_490](https://github.com/user-attachments/assets/bc37ac0a-b0a0-4ef9-b1c3-cad58a1b9346)
