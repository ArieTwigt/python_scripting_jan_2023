import math


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


def calc_pythagoras(a: float, b: float) -> float:
    '''
    Applies Pythagoras theorem
    
    '''
    c_sqrd = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(c_sqrd)
    return c