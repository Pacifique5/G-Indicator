import subprocess

# ✅ New random dates (excluding previous ones)
dates_to_commit = [
    "2024-01-03", "2024-01-18", "2024-02-05", "2024-03-11", "2024-03-26",
    "2024-04-03", "2024-05-16", "2024-05-28", "2024-06-10", "2024-07-06",
    "2024-07-28", "2024-08-08", "2024-08-18", "2024-09-08", "2024-09-19",
    "2024-10-05", "2024-10-13", "2024-11-06", "2024-12-03", "2024-12-15"
]

num_commits = 15  # Adjust this for darker green (higher = darker)
file_name = "fique.txt"

for date_to_commit in dates_to_commit:
    for i in range(num_commits):
        with open(file_name, "a") as file:
            file.write(f"Contribution {i+1} on {date_to_commit}\n")

        subprocess.run(["git", "add", file_name])

        subprocess.run(
            ["git", "commit", "--date", f"{date_to_commit} 12:00:00", "-m", f"Commit {i+1} on {date_to_commit}"],
            env={"GIT_COMMITTER_DATE": f"{date_to_commit} 12:00:00"}
        )

        print(f"✅ Commit {i+1} on {date_to_commit}")

# Push to GitHub
subprocess.run(["git", "push", "origin", "master"])
