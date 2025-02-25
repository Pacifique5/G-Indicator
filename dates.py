import subprocess

# Define the list of dates you want to make commits on (use the format YYYY-MM-DD)
dates_to_commit = [
    # "2025-02-01",
    # "2025-02-05",
    # "2025-02-10",
    "2024-04-17"
]

# Create a text file to commit
file_name = "contributions.txt"

# Loop through the dates and make commits
for date in dates_to_commit:
    # Write to the file
    with open(file_name, "a") as file:
        file.write(f"Contribution on {date}\n")
    
    # Stage the changes
    subprocess.run(["git", "add", file_name])
    
    # Commit with the specified date
    subprocess.run(["git", "commit", "--date", f"{date} 12:00:00", "-m", f"Commit on {date}"])
    
    print(f"Commit made for {date}")

# Push the changes to GitHub
subprocess.run(["git", "push"])
