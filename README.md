# AdvancedLogging
A python script to allow for advanced logging in DayZ

Introducing AdvancedLogging, a python based script to allow for advanced logging of DayZ logs, that attaches text files to discord webhooks.
This script will automatically monitor a specified folder path for the newest file, and monitor said file to upload the newest line in the file as a message to discord.


HOW TO SETUP

First, you need to install the requests library if you haven't already:
"pip install requests"

After downloading the AdvancedLogging.py script, there is some lines you need to change.
First changes you need to make are under "log_directories"

![Screenshot_492](https://github.com/user-attachments/assets/d8722a62-7eba-4cc3-a1fe-3608cef28af6)


This is where you will put the file paths to your log directories. It should look like the following example below.

![Screenshot_490](https://github.com/user-attachments/assets/bc37ac0a-b0a0-4ef9-b1c3-cad58a1b9346)


Next, you will edit the "log_webhooks" section. This function will assign a webhook to said file paths.

![Screenshot_491](https://github.com/user-attachments/assets/8c9bcc7b-976d-48dd-80c0-a3ef1e98d2c6)

Example screenshot is shown below:

![Screenshot_493](https://github.com/user-attachments/assets/7c2c9b62-e6a6-4c4c-af94-f8f92b702524)
