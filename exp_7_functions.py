#%% define function
def greet():
    print("Hello")

# %%
greet()

# %%
def greet_name(name):
    print(f"Hello {name}")

#%%
greet_name("Arie")

# %% define a function for pythagoras
import math
from typing import Tuple


def pythagoras(a: float, b: float, rounding: int=1) -> Tuple[float, float]:
    '''
    Function to apply Pythagoras theorem:

    Parameters:
    * a (required):
    * b (required):

    returns:
    * c, c_squared
    '''

    # check for the right types
    accepted_calculation_types = [int, float]

    if a not in accepted_calculation_types:
        raise TypeError(f"'a' shoud be of type int or float, got {type(a)}")

    if b not in accepted_calculation_types:
        raise TypeError(f"'b' shoud be of type int or float, got {type(b)}")

    c_sqrd = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(c_sqrd)
    c_rounded = round(c, rounding)
    return c_rounded, c_sqrd
    

# %%
result_1, result_2 = pythagoras(5, "Arie", 5)

# %%
c_sqrd = "Arie"
# %%

# %%
