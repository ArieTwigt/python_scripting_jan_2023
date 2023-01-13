import math


def calc_circle(diameter) -> float:
    '''
    A function that returns the size of a circle

    Parameters:
    * diameter
    
    '''

    radius = diameter / 2
    size = math.pow(radius, 2) * math.pi
    return size


def calc_pythagoras(a, b):
    '''
    Calculation of Pythagoras

    Parameters

    * a
    * b
    
    '''
    c_sqrd = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(c_sqrd)
    return c


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