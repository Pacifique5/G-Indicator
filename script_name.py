import os
import datetime
import subprocess

# Define the number of days to commit
days_to_commit =5 # Change this to increase the number of days

# Create a text file to commit
file_name = "contributions.txt"

# Loop through the number of days and make commits
for i in range(days_to_commit):
    # Calculate the date for the commit
    date = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
    
    # Write to the file
    with open(file_name, "a") as file:
        file.write(f"Contribution on {date}\n")
    
    # Stage the changes
    subprocess.run(["git", "add", file_name])
    
    # Commit with a custom date
    subprocess.run(["git", "commit", "--date", f"{date} 12:00:00", "-m", f"Commit on {date}"])
    
    print(f"Commit made for {date}")

# Push the changes to GitHub
subprocess.run(["git", "push"])