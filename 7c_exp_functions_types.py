#%%
def my_func(x, check_type):

    print(f"This is of type {type}")

    if type(x) == check_type:
        print("Yes")
    else:
        print("Something else")

#%%
my_func(4, int)
# %%
assert(type(4) == int)
# %%
