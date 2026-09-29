# para x imprime The number x is[number]. utilizando varios formatos: , + f- string {} % str.format()
x = 5
# 1. using print with multiples argumentos
print('The number x is', str (x) + '.')

# 2. using string concatenation with +
print('The number x is' + str(x) + '.')

# 3. using %-formatting
print('The number x is %i.' %(x))

# 4. using str.fotmat()
print('The number x is {}.'.format(x))

# 5. using an f-string
print(f'The number x is {x}.')