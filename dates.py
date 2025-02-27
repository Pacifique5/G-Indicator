import subprocess

# Define the date you want to make multiple commits on
date_to_commit = "2024-04-17"
num_commits = 50  # Adjust this number to increase the darkness of the green

# Create a text file to commit
file_name = "fique.txt"

# Loop through the number of commits for the selected date
for i in range(num_commits):
    # Write to the file with a unique line for each commit
    with open(file_name, "a") as file:
        file.write(f"Contribution {i+1} on {date_to_commit}\n")
    
    # Stage the changes
    subprocess.run(["git", "add", file_name])
    
    # Commit with the specified date
    subprocess.run(["git", "commit", "--date", f"{date_to_commit} 12:00:00", "-m", f"Commit {i+1} on {date_to_commit}"], 
                   env={"GIT_COMMITTER_DATE": f"{date_to_commit} 12:00:00"})
    
    print(f"Commit {i+1} made for {date_to_commit}")

# Push the changes to GitHub
subprocess.run(["git", "push"])