#%%

#%%
with open("my_file.txt", 'w') as file:
    file.write("This comes from Python")
    

print("Proceed with code")

# %% read file
with open("my_file.txt", 'r') as file:
    file_content = file.read()

print(f"Contents of the file: {file_content}")


#%% 
with open("my_file.txt", 'w') as file:
    file.writelines("This comes from Python\n")
    file.writelines("This also comes from Python\n")
    file.writelines("And this also comes from Python\n")

# %% use the same file.read
with open("my_file.txt", 'r') as file:
    file_content = file.read()



# %%
with open("my_file.txt", 'r') as file:
    file_content_list = file.readlines()
    
# %%
