# Python Strings

three qoutes lets you make multiline strings that respect line breaks

```python
print('''
line break
line break
line break
''')
```

format strings are great for interpolating variables into strings

```python

# f string

other_string = 'neato'

format_string = f'{other_string} curly bois format variables into strings'

# .format()

other_string = '{} other string {}'

print(other_string.format('woot', 'woot 2')) # woot other string woot 2
```

## string methods

```python
# split at supplied character and return a list of strings
string_test = "ace of spades".split(" ") # split at whitespace
print(string_test) # ['ace', 'of', 'spades']

# same result
string_test = "ace of spades".split()
print(string_test) # ['ace', 'of', 'spades']

# index returns the first found instance of a character in a string
string_test = "qqxzzz".index("z")
print(string_test) # 2

string_test = "qqxzzz".index("q")
print(string_test) # 0

# upper() and lower() to format strings to all upper case and lower case respectively
string_test = "Ace of Spades"
string_test.upper()
print(string_test) # ACE OF SPADES

string_test.lower()
print(string_test) # ace of spades

# replace() replaces all instrances of the first argument with the second argument
string_test = "then I went to the store I like".replace("I", "you")
print(string_test) # then you went to the store you like

# the in keyword will evaluate if a string is found in string
string_test = "eggs" in "green eggs and ham"
print(string_test) # True

string_test = "eggs" in "greeneggsandham"
print(string_test) # True

string_test = " eggs " in "greeneggsandham"
print(string_test) # False

# pass len() a string to return the stings length
string_test = len("Hawaii")
print(string_test) # 6
```
