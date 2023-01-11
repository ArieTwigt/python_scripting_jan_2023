#%%
import os

#%%
os.getcwd()


#%%
current_files_folders = os.listdir()

# %%
file_name = "created_from_python"
if file_name not in current_files_folders:
    print("Creating")
    os.mkdir("created_from_python")
else:
    print("Folder already exists")

# %%
os.remove("my_script.py")
# %%
