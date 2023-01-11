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

# %% 3b. better reproducable, note that this will not work if 'tulip' occurs multiple times, might also raise an error
combined_flower_list = flower_list_1 + flower_list_2

idx_tulip = combined_flower_list.index('tulip')
combined_flower_list[idx_tulip] = 'daisy'
combined_flower_list

# %% 3c. (advanced, later) for more occassions of 'tulip', this is called a 'list comprehension'
combined_flower_list = flower_list_1 + flower_list_2

['daisy' if x == 'tulip' else x for x in combined_flower_list]


####


#%% Assignment 1
first_name = "Erling"
last_name  = "Haaland"

full_name = first_name + " " + last_name
full_name_new = f"{first_name} {last_name} Jr."
full_name_new

#%% Assignment 2
full_name_list = full_name_new.split(" ")
first_letter = full_name_list[0][0]
f"{first_letter}. {full_name_list[1]} {full_name_list[2]}"



#%% Assignment 3
flower_list_1 = ['rose', 'tulip', 'lily']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2
print(combined_flower_list)


# %% replace
combined_flower_list[1] = 'daisy'
combined_flower_list

# %% Assignment 3b. If daisy is on a possible different place
flower_list_1 = ['rose', 'lily', 'tulip']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2
print(combined_flower_list)


idx_tulip = combined_flower_list.index('tulip')
combined_flower_list[idx_tulip] = 'daisy'
combined_flower_list

# %% Assignment 3c.

flower_list_1 = ['tulip', 'rose', 'lily', 'tulip']
flower_list_2 = ['dandelion', 'gerbera', 'tulip']

combined_flower_list = flower_list_1 + flower_list_2


#%%
tulip_indices = []

for idx, value in enumerate(combined_flower_list):
    print(value)
    if value == 'tulip':
        tulip_indices.append(idx)

#%%
tulip_indices
# %%
