#%% 
import sys
import math


#%%
diameter = float(sys.argv[1])
#diameter = float(input("Insert diameter: \n"))

# %%
print(f"The diameter was {diameter}")


radius = diameter / 2
size = math.pow(radius, 2) * math.pi

print(f"The size is {size}")