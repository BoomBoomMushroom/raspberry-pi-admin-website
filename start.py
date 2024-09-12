import os

# Get working directory and print it
dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"Working path: {dir_path}")

# Pull any updates!
os.system("git pull")