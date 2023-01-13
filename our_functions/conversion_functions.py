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