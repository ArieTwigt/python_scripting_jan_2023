#%%
5 > 4

# %%
if 4 == 5:
    print("It is true")
    print("Go on") 
elif 4 < 5:
    print("Not as much, but smaller")
else:
    print("It was something else")
   
print("Proceed with code")



# %%
my_age = 23

if my_age < 21:
    print("You cannot drink")
else:
    print("🍻 Cheers")

# %%
members_list = ['Arie', 'James', 'Arnold']
my_name = 'Bob'


if my_name not in members_list:
    print("You are not a member, yet")
    members_list.append(my_name)
    print("You are a member now")
    print(f"Members {members_list}")
else:
    print("You are a member, welcome")


# %%
if my_age > 21 and (my_name == 'Bob' or 'Jim') :
    print("This is true")

# %% one-liner statements
age_class = 'adult' if my_age >= 21 else 'infant'

# %%
my_name = "Arie"

my_name.lower() 

# %% 
# check if the 'o' or 'a' appears in my_name
my_name = 'Bob'
matches = ['o', 'a']
if any(letter in my_name.lower() for letter in matches):
    print("Present")

# more pythonic



# %%
