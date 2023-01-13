def change_name(name):
    '''
    Function that removes the vowels from a name
    
    '''

    vowels = 'aeouiy'

    new_name = ""
    
    for letter in name:
        if letter.lower() not in vowels:
            new_name += letter

    return new_name

