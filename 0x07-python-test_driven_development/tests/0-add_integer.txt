Test cases for 0-add_integer module
===================================

The 0-add_integer module takes two integers or floats as arguments and returns their sum

Usage
=====

Importing function from the module:
    >>> add_integer = __import__('0-add_integer').add_integer

Adding two positive integers (a = 1 and b = 1)
    >>> add_integer(1, 1)
    2

Adding one positive and one negative integer (a = 10 and b = -4)
    >>> add_integer(10, -4)
    6

Adding two negative integers (a = -10 and b = -4)
    >>> add_integer(-10, -4)
    -14

Adding two integers with the second being the same as the default value of b (a = 2 and b = 98)
    >>> add_integer(2)
    100

Adding a positive float and a positive integer (a = 2.5 and b = 5)
    >>> add_integer(2.5, 5)
    7

Adding a float and an integer where the integer is equal to the default value of b (a = 2.5 and b = 98)
    >>> add_integer(2.5)
    100

Adding a positive float and a negative integer (a = 10.5 and b = -2)
	    >>> add_integer(10.5, -2)
	    8

Adding two negative floats (a = -10.5 and b = -2)
	    >>> add_integer(-10.5, -2)
	    -12

Adding an integer number and a string (a = 4 and b = "School")
    >>> add_integer(4, "School")
    Traceback (most recent call last):
	      ...
    TypeError: b must be an integer

Passing no argument to the function
    >>> add_integer(None)
    Traceback (most recent call last):
	      ...
    TypeError: a must be an integer

Adding a letter and a number (a = 'c' and b = 1)
    >>> add_integer('c', 1)
    Traceback (most recent call last):
              ...
    TypeError: a must be an integer

Adding two letters (a = 'c' and b = 'm')
    >>> add_integer('c', 'm')
    Traceback (most recent call last):
              ...
    TypeError: a must be an integer

Adding a tuple
    >>> add_integer((1, 1))
    Traceback (most recent call last):
              ...
    TypeError: a must be an integer

Adding a number and a list
    >>> add_integer(123, [])
    Traceback (most recent call last):
	      ...
    TypeError: b must be an integer

Passing a only one string
    >>> add_integer("Hello")
    Traceback (most recent call last):
	      ...
    TypeError: a must be an integer

Adding two float numbers (a = 1.2 and b = 4.2)
    >>> add_integer(1.2, 4.2)
    5

Case Overflow:

    >>> add_integer(float('inf'), 0)
    Traceback (most recent call last):
    	      ...
    OverflowError: cannot convert float infinity to integer

Case Overflow 2:

    >>> add_integer(float('inf'), float('-inf'))
    Traceback (most recent call last):
    	      ...
    OverflowError: cannot convert float infinity to integer

Case NaN 1:

    >>> add_integer(0, float('nan'))
    Traceback (most recent call last):
    	      ...
    ValueError: cannot convert float NaN to integer

Case NaN 2:

    >>> add_integer(float('nan'))
    Traceback (most recent call last):
    	      ...
    ValueError: cannot convert float NaN to integer
