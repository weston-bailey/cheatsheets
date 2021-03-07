# Python Cheatsheet

enumerate 
zip
set

[gitbook notes](https://gawdiseattle.gitbook.io/wdi/python/python-intro)

## comments

```python
# this is a comment
'''
this is a 
multiiline comment
but do not do this
because its actually just a string
'''
```

## print function

```python
print('hello snakes') # output 'hello snakes'
```

## variables

use snake_case

its the_python_way

```python
my_variable = 5
my_other_variable = 'string'
```

## basic primatives

```python
# Nothingness (NoneType) always evaluates to false
false_variable = None

# Booleans are capitalized
is_true = True
is_false = False

# integers
integer = 2

# float
floating_point = 3.1415

# complex
complex_number = 1+2j
complex_number = 1+2j + 5 + 3j # evaluates to (6+5j)

# strings
my_string = 'yay im words'
my_string = "yay im words"
my_string = "yay i'm words" # single quute respected in double quotes
my_string = 'yay i\'m words' # escape inner single quote with \'
```

## arithmetic

```python
# addition 
print(2 + 2) # 4

# subtraction
print(2 - 2) # 0

# decimal division
print(4 / 3) # 1.333333

# forced integer division
print(4 // 3) # 1

# multiplication
print(2 * 3) # 6

# exponents 
print(2 ** 3) # 8

# modulo (return remainder of division)
print(17 % 5) # 2

# plus equals (add to self)
num = 2
num += 2
print(num) # 4
num += 2
print(num) # 6

# minus equals (subtract from self)
num = 2
num -= 2
print(num) # 0
num -= 2
print(num) # -2

# multiply equals 
num = 2
num *= 2
print(num) # 4

# divide equals
num = 11
num /= 2
print(num) # 5.5

# divide integer equals
num = 11
num //= 2
print(num) # 5

# exponent equals
num = 2
num **= 3
print(num) # 8

# modulo equals 
num = 17
num %= 5
print(num) # 2
```

## logical operators

two equals `==` evaluates equality
bang equals `!=` evaluates inequality

regular words are great!

`not` evaluates if something is not true
`or` evaluates one or the other thing being true
`and` evaluates both of two things being true

```python
# equality
print(1 == 1) # True
print(1 == 2) # False

# inequality
print(1 != 1) # False
print(1 != 2) # True

# not, or, and
truthy = True 
falsey = False
noney = None

print(truthy) # True
print(falsey) # False
print(noney)  # None

print(not truthy) # False
print(not falsey) # True
print(not noney)  # True

print(truthy or falsey) # True
print(falsey or falsey) # False
print(truthy or noney) # True

print(truthy and falsey) # False
print(truthy and truthy) # True
print(truthy and noney) # None
```





