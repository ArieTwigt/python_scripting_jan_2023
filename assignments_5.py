#%% Assignment 1
my_name = "Arianne"

if "a" in my_name.lower():
    print("✅ Your names contains an 'a'")
else:
    print("❌Your name does not contain an 'a'")



#%% Assignment 2a

vowels = 'aeoiu'
my_name = "Arie"

if my_name[0].lower() in vowels:
    print("Starts with a vowel")
    my_name_new = my_name.replace(my_name[0], "B")
    print(my_name_new)
else:
    print("Does not start with a vowel")
    my_name_new = my_name.replace(my_name[0], "A")
    print(my_name_new)


#%% Assignment 2b --> Elaborate, with random and string, if letter appears more than 1 time in the name
import string
import random

all_letters = string.ascii_lowercase
vowels = 'aeoui'
non_vowels = "".join([letter for letter in all_letters if letter not in vowels])


#%%
if my_name[0].lower() in vowels:
    print("Your names starts with a vowel")
    first_letter = my_name[0]
    random_non_vowel = random.choice(non_vowels).upper()
    my_name_new = my_name.replace(first_letter, random_non_vowel, 1)
else:
    print("Your names does not start with a vowel")
    first_letter = my_name[0]
    random_vowel = random.choice(vowels).upper()
    my_name_new = my_name.replace(first_letter, random_vowel, 1)

print(my_name_new)




