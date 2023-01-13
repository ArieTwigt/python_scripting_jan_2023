#%% Assignment 1
def calc_contents(length: float, 
                  width: float, 
                  height:float) -> float:
    '''
    Calculates the contents of a box

    Parameters:

    * length
    * width
    * height

    Return:

    * content 
    '''

    contents = length * width * height
    return contents


#%%
result = calc_contents(3,4,5)
print(result)

# %% Assignment 2
names_list = ['Jim', 4, 'Marc', 'Danny', 'Peter']


def uppercase_names(input_list: list, auto_convert=False, keep_type=False) -> list:
    '''
    Uppercases every value in a list
    
    '''

    # check
    for idx, name in enumerate(input_list):
        if type(name) != str:
            if auto_convert:
                print(f"Autoconverting {name}")
                input_list[idx] = str(name)
            else: 
                raise TypeError(f"{name} is of type {type(name)}")

    list_uppercased = [name.upper() for name in input_list]

    return list_uppercased

#%%
uppercase_names(names_list, auto_convert=True)





# %%
name = "Arie"
if type(name) == str:
    print("This is a string")


# %%
[name.upper() if type(name) == str else name for name in names_list]


# %%
