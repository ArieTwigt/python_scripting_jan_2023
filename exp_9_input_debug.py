from handy_functions.calculation_functions import calc_pythagoras

a_value = float(input("Provide a value for a (10):\n") or 10)
b_value = float(input("Provide a value for b (10):\n") or 10)


result = calc_pythagoras(a_value, b_value)
print(result)