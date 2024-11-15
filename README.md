# AdvancedLogging
A python script to allow for advanced logging in DayZ. You MUST have python installed already, I will not be doing a walkthrough on how to do that.
I will also not be providing a walkthrough on how to do Discord WebHooks, as you should already know how to do that if you are going to use this.
**THIS WILL ONLY WORK ON TEXT FILES. IT WILL NOT BE ABLE TO PULL FROM OTHER FILE TYPES.**

Introducing AdvancedLogging, a python based script to allow for advanced logging of DayZ logs, that attaches text files to discord webhooks.
This script will automatically monitor a specified folder path for the newest file, and monitor said file to upload the newest line in the file as a message to discord.


# HOW TO SETUP

After downloading the AdvancedLogging.py script, there is some lines you need to change.
First changes you need to make are under "log_directories"

![Screenshot_492](https://github.com/user-attachments/assets/d8722a62-7eba-4cc3-a1fe-3608cef28af6)


This is where you will put the file paths to your log directories. It should look like the following example below.

![Screenshot_490](https://github.com/user-attachments/assets/bc37ac0a-b0a0-4ef9-b1c3-cad58a1b9346)


Next, you will edit the "log_webhooks" section. This function will assign a webhook to said file paths.

![Screenshot_491](https://github.com/user-attachments/assets/8c9bcc7b-976d-48dd-80c0-a3ef1e98d2c6)

Example screenshot is shown below:

![Screenshot_493](https://github.com/user-attachments/assets/7c2c9b62-e6a6-4c4c-af94-f8f92b702524)


After you make those changes, you will need to save the file as a .py file type. Remember where you saved this, as you will need the file for the next step.

# HOW TO CHANGE THE .py FILE TO A .exe FILE

Open an elevated command prompt window, and run the following command:
```pip install auto-py-to-exe```

After that installs, run the following command:
```python -m auto_py_to_exe```

You should get a window that pops up looking like this:

![Screenshot_494](https://github.com/user-attachments/assets/33239adc-137e-4458-98f3-5cfbb1a3b3d3)

Browse for the newly created AdvancedLogging.py file, and after you select it, click on "Convert .py to .exe"
The file will create itself, and open up a window where the file has been created. 

At this time, you can either manually open it, and the logging will start, or you can set up the .exe to automatically launch when you turn on the computer.

You should get a command window that pops up, and it will search for the newest log file in the folder you specified.
This command window will notify you if logging is successful, by stating that it is monitoring the newest log file.

![Screenshot_486](https://github.com/user-attachments/assets/e08d79d3-fc69-4251-9f4e-2a9d857699af)


If you have set everything up properly, the script will automatically send a discord message to the proper webhook, to the channel that the webhook is linked to.
The script will automatically pull the newest line in the text file, and send it as a message in Discord.

![Screenshot_483](https://github.com/user-attachments/assets/58c4b9ba-9e02-4a62-a07f-a14bbfc985c9)


























