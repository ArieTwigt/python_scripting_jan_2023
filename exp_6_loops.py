#%% iterable
names_list = ['Arie', 'Jim', 'James', 'Bob']

# basic loop with 'i' as iterator
for i in names_list:
    print(i)

# %%
my_name = "Arie"

# basic loop, with more descriptive iterator
for letter in my_name:
    print(letter)

#%% break, continue
# break, stops the entire loop
# continue, stops the current iteration
required_amount = 1000
currently_donated = 0
min_amount = 100
max_amount = 500

donations_list = [400, 25, 200, 200, 600, 50, 600, 100, 100]

for idx, donation in enumerate(donations_list, start=1):
    print(f"Current donation: {idx}")
    if donation < min_amount:
        print(f"Donation {donation} lower than the minimum")
        print("="*10)
        continue
    if donation > max_amount:
        print(f"Donation {donation} higher than the maximum")
        print("="*10)
        continue
    if currently_donated >= required_amount:
        print(f"Amount already reached")
        break
    print(f"Current_amount: {currently_donated}")
    print(f"Next donation is: {donation}")
    currently_donated += donation
    print(f"Current_amount: {currently_donated}")
    print("="*10)


print("This is the rest of the code")


# %%
for idx, value in enumerate(donations_list):
    print(idx)
    print("-")
    print(value)

# %% Nested loop
names_list = ['Arie', 'Jim', 'James', 'Bob']

for name in names_list:
    print(f"Current name {name}")
    for letter in name:
        print(letter)
    print("="*10)

#%% list comprehensions
ages_list = [21, 34, 25, 19, 15, 50, 13]

new_ages_list = []

for age in ages_list:
    new_ages_list.append(age * 2)

new_ages_list    

#%% list comprehension
new_ages_list = [age * 2 for age in ages_list]


# %% filter
adult_ages = []

for age in ages_list:
    if age > 18:
        adult_ages.append(age)

adult_ages

# %% filter

[age for age in ages_list if age > 18]

# %% 
age_category = []

for age in ages_list:
    if age > 18:
        age_category.append('adult')
    else:
        age_category.append('infant')

age_category

# %%
['adult' if age > 18 else 'infant' for age in ages_list]

# %%
[('adult', 'infant')[age < 18] for age in ages_list]


#%%
person_dict = {"name": "Jim",
               "age": 20,
               "hobbies": ['skiing', 'cycling', 'reading'],
               "favourite food": "Sushi"}


for key, value in person_dict.items():
    if type(value) == list:
        print(f"His {key} are:")
        for x in value:
            print(f"- {x}")
        print("="*10)
        continue
    print(f"His {key} is {value}")
    print("="*10)

# %%
for x in person_dict.items():
    print(x)
# %%
