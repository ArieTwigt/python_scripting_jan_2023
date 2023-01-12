#%%
'''
[] : Lists
() : Tuples
{} : dictionaries
    -> Key-value pairs
        --> Similar to JSON-data
'''

#%%
person_dict = {}

#%%
person_dict = dict()

#%% declare
person_dict = {"name": "Arie",
               "age": 40,
               "hobbies": ['football', 'cycling', 'reading'],
               "spouse": {
                "name": 'mary', 
                "age": 38
               }}

# %% impirative
person_dict_2 = {}
person_dict_2['name'] = 'Jim'
person_dict_2['age'] = 40
person_dict_2['name'] = 'Arnold'
person_dict_2

# %% methods, attributes
person_dict.get('pet', 'Not there')


#%%
person_dict.keys()
# %%
person_dict['spouse']['age']

# %%
person_dict['hobbies'][1]

# %%
type(person_dict['hobbies']) 

# %%
