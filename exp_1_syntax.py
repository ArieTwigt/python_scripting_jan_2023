# %%
my_name = "Arie"

# %%
print(my_name)

# %%
my_age = 30

#%%
my_length = 1.93

# %% verify types
type(my_name)

# %%
type(my_length)

# %% 
'''
Everything is an Object:

- Methods --> Callable ()
- Attributes


'''


#%%
my_name.replace("r", "p")

# %%
my_age.upper()

# %% 
'''
Structure and Brackets

Lists: []
Dictionaries: {}
Tuples: ()


'''


#%%
names_list = ['Arie', 'Jim', 'James']


#%%
print(names_list)

#%%
names_list.append('George')

# %%
mixed_list = ['Arie', 4000, True, names_list]
# %%
mixed_list

#%% '+'
4 + 4
# %%
my_name + my_name
# %%
names_list + names_list


# %% Dictionaries, Key-Value: JSON
person_dict = {'name': 'Arie', 
               'age': 30}

#%%
person_dict['name']

# %% Tuples --> Is a Immutable 'List'
names_tuple = ('Arie', 'Jim', 'James')

# %% data selection
names_list[0]

# %%
names_tuple[0]

# %%
names_list.append('Philip')
names_list

# %%
names_list[0] = "Bob"
names_list

# %%
names_tuple[0] = "Bob"


# %% formatting
"Hi my name is " + my_name + "and I am " + str(my_age) + "old"


# %% f-string for formatting
f"Hi my name is {my_name} and I am {my_age} old"


