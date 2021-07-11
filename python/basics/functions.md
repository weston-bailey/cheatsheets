# Python Functions

default arguments most come after arguments without a default:

```python
def foo(x,y=5):
  return x + y

foo(3) # returns 8
```

variable length arguments *args:



return value annotations with and arrow ->

```python
def annotated(x, y) -> int:
  return x + y
```

argument annotation

```python
def annotated(x: int, y: int) -> int:
  return x + y

def verbose_annotated(x: 'int, the first value to be added', y: 'int, the second value to be added') -> int:
  return x + y
```

order of function arguments:

```python
def orderly(x: 'arg with no defualt', y: 'arg with defualt' = 3, *args, **kwargs):
  return x, y, args, kwargs
```
