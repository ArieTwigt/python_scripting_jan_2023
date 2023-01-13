#%% Assignment 1

# define the story
my_story = '''

This is a story of a programmer.
He wrote a script.
It got an Indentation error.

- END -
'''


#%%
with open("my_story.txt", "w") as file:
    file.write(my_story)


#%% Assignment 2
with open("my_story.txt", "r") as file:
    story_lines = file.readlines()


#%% Assignment 3
story_str = "".join(story_lines)
story_str_upper = story_str.upper()


# %% Assignment 4
import os

current_files_folders = os.listdir()

folder_name = "stories"

if folder_name not in current_files_folders:
    os.mkdir(folder_name)


with open(f"{folder_name}/my_story.txt", "w") as file:
    file.write(story_str_upper)
# %%
