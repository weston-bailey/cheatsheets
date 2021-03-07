# this is a comment

'''
multiline comment (python ignores unnassainged string literals)
'''

# better practice for 
# mulitline comments
# are like this

# variables
# my_variable = 5
# print(my_variable)

# empty values are are a datatype None
# None does not equal false but does not evaluate as true

# my_bank_account = None

# if my_bank_account:
#   print('this is true')
# else:
#   print('false')

# booleans must be capitalized

# is_true = True
# is_false = False

# number datatypes
# integer: 23 whole number
# float: 23.02 floating point decimal
# complex: 2+3j

# python does floating point division with / 
# python does interger division //

# float division
# print(15 / 5)
# print(15 / 4.9)

# integer divsion
# print(15 // 4.9)

# complex numbers
complex = 1 + 2j + 7 + 3j

# print(complex)

# exponents
# square = 2 * 2
# print(square)
# exponent = 2 ** 1000
# print(exponent)

def gather_input():
  you = input("Enter your name: ")
  friend = input("Enter a friend's name: ")
  print("Hello, {}. {} says hi.".format(you, friend))

gather_input()
