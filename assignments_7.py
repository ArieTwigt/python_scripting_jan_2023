#%% Assignment 1
from handy_functions.calculation_functions import calc_contents
from handy_functions.conversion_functions import uppercase_names


#%%
result = calc_contents(3,4,5)
print(result)

# %% Assignment 2
names_list = ['Jim', 4, 'Marc', 'Danny', 'Peter']


#%%
uppercase_names(names_list, auto_convert=True)


# %%
name = "Arie"
if type(name) == str:
    print("This is a string")


# %%
[name.upper() if type(name) == str else name for name in names_list]


# %%
