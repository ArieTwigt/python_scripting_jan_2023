#%% Assignments 
from our_functions.calculation_functions import calc_contents
from our_functions.conversion_functions import uppercase_names



# test if the functions work
#%% calc_contents
result = calc_contents(4,5,6)
print(result)


#%% uppercase names
names_list = ['arie', 'jim', 'bob', 'ann']
new_names_list = uppercase_names(names_list)
print(new_names_list)


#%%