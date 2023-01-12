#%%
import requests
import sys
import pandas as pd
import os
from tqdm import tqdm
from datetime import datetime

# %%
selected_brand_list = sys.argv[1:]

if len(selected_brand_list) == 0:
    input_brands_brand = input("Provide lists with brands (e.g. AUDI TESLA) \n").upper()
    selected_brand_list = input_brands_brand.split(" ")


for selected_brand in tqdm(selected_brand_list):

    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand}"
    
    #%%
    response = requests.get(endpoint)
    
    # %%
    if response.status_code != 200:
        print(f"Error for {selected_brand}")
        continue
    
    
    # %%
    cars_list = response.json()
    
    
    # %%
    cars_df = pd.DataFrame(cars_list)
    
    #%% check if the 'export' folder exists
    if not os.path.exists('export'):
        os.mkdir('export')
    
    #%%
    folder_name = selected_brand
    
    export_folder = f"export/{folder_name}"
    os.makedirs(export_folder, exist_ok=True)
    
    # %%
    current_date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{selected_brand}_{current_date_time}.csv"

    cars_df.to_csv(f"{export_folder}/{file_name}", 
                   sep=";", 
                   index=False)
    # %%
    