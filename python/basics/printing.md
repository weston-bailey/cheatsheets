# Printing in Python

basic printing is pretty basic

just invoke the `print` method

```python
print('good job! Im gonna print')
```

by default, the print function ends with a newline, but the end parameter can be used to specify a different ending character:

```python
# useful not starting a new line
print('empty qoutes', end=' ') # adds one space
print('nothing', end='') # no space after printing 
# useful for progress meters
print('carriage return', end='\r')
# horizontal tab
print('tab', end='\t')
# vertical tab (start at newline in same place)
print('tab', end='\v')
# formfeed basically has the same effect as vertical tab
print('formfeed', end='\f')
```

