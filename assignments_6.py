#%% Assignment 1
names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

vowels = 'aeoiu'

for name in names_list:
    print(f"old name: {name}")
    for letter in name:
        if letter in vowels:
            name = name.replace(letter, "")
    print(f"new name: {name}")
    print("="*10)
    

# %% Assignment 2
from datetime import date, timedelta

today_date = date.today()

num_days = 10

weekend_days = ['Saturday', 'Sunday']

for num_day in range(10):
    num_day += 1
    next_date = today_date + timedelta(days=num_day)
    next_date_weekday = next_date.strftime("%A")
    if next_date_weekday in weekend_days:
        print(f"🍻 {next_date_weekday}")
    else:
        print(f"💻 {next_date_weekday}")

# %%
