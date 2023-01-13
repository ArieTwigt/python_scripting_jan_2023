import os

if not os.path.exists("our_folder"):
    print(f"Folder does not exist yet, creating...")
    os.mkdir("our_folder")

print("This is from the __init__ ")

