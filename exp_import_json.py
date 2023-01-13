#%%
import json


#%%
with open("config.json", "r") as file:
    config_str = file.read()

# %%
config_str['brands']

# %%
config_dict = json.loads(config_str)
# %%
