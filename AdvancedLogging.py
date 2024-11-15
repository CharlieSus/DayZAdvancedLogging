import os
import time
import requests
import threading

# List of directories where log files are stored
log_directories = [
    r"\your\file\path1", # add file path here
    r"\your\file\path2",# add file path here

    # add more above this text, using same formatting as above
]

# Dictionary to store the webhook URLs for each directory (mapping the directory to a webhook)
log_webhooks = {
    r"\your\file\path1": "\your\discord\webhook\url",
    r"\your\file\path2": "\your\discord\webhook\url",

    # add more above this text, using same formatting as above
}

# Function to send a message to Discord
def send_to_discord(message, webhook_url):
    try:
        payload = {"content": message}
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print(f"Message sent to Discord: {message}")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending message to Discord: {e}")

# Function to check if the directory is accessible
def check_directory_access(directory):
    if os.access(directory, os.R_OK):
        print(f"Directory is accessible: {directory}")
        return True
    else:
        print(f"Directory is NOT accessible: {directory}")
        return False

# Function to read new lines in the log file and send them to Discord
def read_and_send_log_file(file_path, webhook_url):
    try:
        with open(file_path, "r") as file:
            # Move to the end of the file
            file.seek(0, os.SEEK_END)
            
            while True:
                new_line = file.readline()
                if new_line:
                    send_to_discord(new_line.strip(), webhook_url)
                else:
                    time.sleep(1)  # Sleep for 1 second before checking for new content
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

# Function to get the most recently modified log file in a directory
def get_latest_log_file(directory):
    try:
        print(f"Scanning directory: {directory}")
        
        if not os.path.exists(directory):
            print(f"Directory does not exist: {directory}")
            return None
        
        log_files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        if not log_files:
            print(f"No log files found in {directory}")
            return None
        
        latest_file = max(log_files, key=os.path.getmtime)
        print(f"Latest log file in {directory}: {latest_file}")
        return latest_file
    except Exception as e:
        print(f"Error scanning directory {directory}: {e}")
        return None

# Function to monitor a specific directory in its own thread
def monitor_directory(directory, webhook_url):
    try:
        if not check_directory_access(directory):
            print(f"Skipping directory {directory} because it's not accessible.")
            return
        
        print(f"Monitoring directory: {directory}")
        
        while True:
            latest_log_file = get_latest_log_file(directory)
            
            if latest_log_file:
                print(f"Monitoring log file: {latest_log_file}")
                read_and_send_log_file(latest_log_file, webhook_url)
            else:
                print(f"No log files found in {directory}")
            
            time.sleep(5)  # Check for new files every 5 seconds
    except Exception as e:
        print(f"Error in monitoring directory {directory}: {e}")

# Function to start monitoring all directories in separate threads
def monitor_logs():
    try:
        threads = []
        
        for directory in log_directories:
            webhook_url = log_webhooks.get(directory)
            if webhook_url:
                thread = threading.Thread(target=monitor_directory, args=(directory, webhook_url))
                threads.append(thread)
                thread.start()  # Start the thread
        
        for thread in threads:
            thread.join()
            
    except Exception as e:
        print(f"Error in monitoring logs: {e}")

if __name__ == "__main__":
    try:
        monitor_logs()
    except Exception as e:
        print(f"Error in main execution: {e}")
