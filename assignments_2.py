#%% define the variables
first_name = "Erling"
last_name = "Haaland"
full_name = first_name + " " + last_name
full_name = f"{first_name} {last_name}"
full_name

# %% Assignment 1a. 
full_name_new = full_name + " " + ".Jr"
full_name_new


# %% Assignment 1b.
full_name_new = f"{full_name} .Jr"
full_name_new


# %% Assignment 2a. 
first_letter = first_name[0]
full_name_abbrv = f"{first_letter}. {last_name} .Jr"
full_name_abbrv

# %% 2b. -> better reproducable
name_split = full_name_new.split(" ")
name_split

# %%
full_name_abbrv = f"{name_split[0][0]}. {name_split[1]} {name_split[2]}"
full_name_abbrv

# %% Assignment 3
flower_list_1 = ['rose', 'tulip', 'lily']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2


# %% 3a. hard-coded
combined_flower_list[1] = "daisy"
combined_flower_list

# %% 3b. better reproducable
combined_flower_list = flower_list_1 + flower_list_2

idx_tulip = combined_flower_list.index('tulip')
combined_flower_list[idx_tulip] = 'daisy'
combined_flower_list

# %% 3c. (advanced, later) for more occassions of 'tulip'
combined_flower_list = flower_list_1 + flower_list_2

['daisy' if x == 'tulip' else x for x in combined_flower_list]

# %%
