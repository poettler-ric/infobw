# course: Informatik 1 BW
# topics: variables, datatypes, strings + formatting, using funtions
#         and code conventions
# author: Richard Pöttler (richard.poettler@student.tugraz.at)

# A program consists of input, processing and output
# Examples:
# https://github.com/poettler-ric/scripts/blob/master/mkpasswd.py
# https://github.com/poettler-ric/scripts/blob/master/wallhaven.py

# Simple statements
print("hello world")
print("second line")
4 + 5
print(4 + 5)

# Variables have a name, address and value (datatype?)
name = "Dilbert"
age = 25
print("Hello, my name is %s and I am %d years old." % (name, age))

height = 10
width = 5
depth = 5
volume = height * width * depth
print("The volume is %d m3" % volume)

# multiple assignments in one line are possible
x, y = 1, 2
print("x=%s y=%s" % (x, y))
# swapping values in python is easy
x, y = y, x
print("x=%s y=%s" % (x, y))


# Datatypes
# Why: to determine how to handle the stored values and what operations
# are allowed
# https://docs.python.org/2/library/stdtypes.html

# bools
a = True
b = False

print("a: %s type: %s" % (a, type(a)))
print("b: %s type: %s" % (b, type(b)))

# not True -> False
# not False -> True
#
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False
#
# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False

print("not a: %s" % (not a))
print("not b: %s" % (not b))
print("a and True %s" % (a and True))
print("a and False %s" % (a and False))
print("b and True %s" % (b and True))
print("b and False %s" % (b and False))
print("a or True %s" % (a or True))
print("a or False %s" % (a or False))
print("b or True %s" % (b or True))
print("b or False %s" % (b or False))

# Further: https://docs.python.org/2/library/stdtypes.html#truth-value-testing
print("0 == False -> %s" % (0 == False))

# Numbers: int, long, float, complex
i = 10 # integer
j = 10l # long
k = 10.1 #float
# type() returns the type of an expression
print("i: %s type: %s" % (i, type(i)))
print("j: %s type: %s" % (j, type(j)))
print("k: %s type: %s" % (k, type(k)))

# type casts convert one expression to another datatype
# explicit type cast
print("casted i -> long: %s type: %s" % (long(i), type(long(i))))
print("casted i -> float: %s type: %s" % (float(i), type(float(i))))
print("casted k -> int: %s type: %s" % (int(k), type(int(k))))
# implicit type cast (operand with the 'narrower' type is widened to that of the other)
l = i / j
print("k: %s type: %s" % (l, type(l)))
print("5 / 2 = %s type: %s" % (5/2, type(5/2)))
print("5 / 2.0 = %s type: %s" % (5/2.0, type(5/2.0)))


# Operators
# + - * ** / % ()
print("(4 + 3) * 6 / 7 - 10 = %s" % ((4 + 3) * 6 / 7 - 10))
print("2^3 = %s" % 2**3)
print("negate: %s" % -i)
print("modulo (remainder of 17 / 5): %s" % (17 % 5))
# Shorthands:
# += -= *= /=
c = 5
c += 2 # c = c + 2
print("c = %s" % c)

# Comparison
# == != < > <= >=
print("i == 10 -> %s" % (i == 10))
print("i != 5 -> %s" % (i != 5))
print("i < 15 -> %s" % (i < 15))
print("i > 5 -> %s" % (i > 5))
print("i <= 10 -> %s" % (i <= 10))
print("i >= 10 -> %s" % (i >= 10))


# Strings
# Strings are list of characters
# A character is a letter
string1 = "hello"
string2 = "world"
print(string1 + " " + string2)
print("=" * 20)
# https://docs.python.org/2/library/stdtypes.html#string-methods
print(string1.capitalize() + " " + string2.capitalize())
print("upper".upper() + "LOWER".lower())
print(string1.startswith("hel"))
print(string1.endswith("lo"))
print(string1.find("ll")) # retunrs index or -1 if not found

# string formatting
# https://docs.python.org/2/library/stdtypes.html#string-formatting-operations
string_with_one_variable = "i=%s" % i
print(string_with_one_variable)
string_with_multiple_variables = "i=%s j=%s k=%s" %(i, j, k)
print(string_with_multiple_variables)
# formatting numbers:
print("d: %d" % 10.02)
print("f: %f" % 10.02)
print("g: %g" % 10.02)
print("   1234567890")
print("f: %10f" % 10.02)
print("f: %10.1f" % 10.02)
print("f: %10.3f" % 10.02)


# Functions
# https://docs.python.org/2/library/functions.html#built-in-funcs
# get documentation easily - e.g. help(print)
print("absolute: %s" % abs(-i))
print("min: %s" % min(8, 4, 2, 10, 9))
print("max: %s" % max(8, 4, 2, 10, 9))


# Code conventions
# https://www.python.org/dev/peps/pep-0008/
# lines at maximum only 80 characters long

# Variables - distinguish words with '_'
long_variable_name = 0
# Constants
GRAVITY = 9.80665

# Line splitting
variable1 = 1
variable2 = 2
variable3 = 3
another_long_variable_name = variable1 + variable2 \
                             / variable3
