#%% Assignment 1.
from datetime import date

#%% for now hard code the birthday
next_birthday = date(2023, 4, 1)
date_today = date.today()

# subtract the days -> Results in a timedelta
days_difference = next_birthday - date_today
days_until_birthday = days_difference.days
print(days_until_birthday)

#%% Assignment 2.
import math

diameter = 10
radius = diameter / 2
surface = math.pow(radius, 2) * math.pi
print(surface)

#%% Assignmnent 3
import os

current_files_folders = os.listdir()
print(current_files_folders)

# %%
try:
    os.mkdir("our_functions")
except FileExistsError:
    print("File already exists")
# %%
