#%%
import json

#%%
config_dict = {'brands': ['tesla', 'audi', 'bmw'],
               'filename': 'car_export.csv'}


    
# %%
config_dict
# %%
config_dict['brands']


#%%
config_str = json.dumps(config_dict)

# %%
with open("config.json", "w") as file:
    file.write(config_str)
# %%
