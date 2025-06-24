# This demonstrate the use of import modules and packages
# This imports the calculator module to give access to the elements within
import calculator  

# This is used to import a specific function that resides within the calculator module.
# from calculator import calc_add

print(calculator.calc_add(5, 3))
print(calculator.calc_div(5, 3))
print(calculator.calc_mult(5, 3))
print(calculator.calc_subt(5, 3))
