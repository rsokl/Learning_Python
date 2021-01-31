---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.9.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #raw raw_mimetype="text/restructuredtext" -->
.. meta::
   :description: Topic: Basics of Python Objects, Difficulty: Easy, Category: Section
   :keywords: integers, booleans, floats, floating point precision, lists, strings, fundamentals
<!-- #endraw -->

<!-- #region -->
# Basic Object Types

<div class="alert alert-warning">

**Note**: 

There are reading-comprehension exercises included throughout the text. These are meant to help you put your reading to practice. Solutions for the exercises are included at the bottom of this page.
</div>

You will see the term "object" be used frequently throughout this text. In Python, the term "object" is quite the catch-all; including numbers, strings of characters, lists, functions - a Python object is essentially anything that you can assign to a variable. That being said, there are different *types* of objects: Python treats integers as a different *type* of object than a string, for instance. 

The different object types have manifestly different purposes and thus have different built-in functions available to them. Here, we will review some of the basic types that are built into Python, as a natural entry point to writing code. We will cover:

- numbers (integers, floating-point numbers, and complex numbers)
- booleans
- the "null" type
- strings
- lists

The built-in function `isinstance` will allow us to check if an object is of a given type. You can also use the built-in `type` function to check an object's type. For example, the following code checks if an object is an integer:

```python
# assign the variable `x` to the integer 1
>>> x = 1  

# checking the type of `x`
>>> type(x)
int

# verifying that `x` is an integer-type object
>>> isinstance(x, int)
True
```

In a later module, you will learn "object-oriented" programming, which will allow you to create your own, customized objects!
<!-- #endregion -->

<!-- #region -->
## Number Types
Python has three basic types of numbers: integers, "floating-point" numbers, and complex numbers. Familiar mathematical symbols can be used to perform arithmetic on all of these numbers (comparison operators like "greater than" are not defined for complex numbers):

| Operation  | Description |
| ------------- |:-------------:|
| `x + y` | Sum of two numbers |   
| `x - y` | Difference of two numbers |   
| `x * y` | Product of two numbers |   
| `x / y` | Quotient of two numbers |   
| `x // y` | Quotient of two numbers, returned as an integer | 
| `x % y` | `x` "modulo": `y`: The remainder of `x / y` for positive `x`, `y` |
| `x ** y` | `x` raised to the power `y` |
| `-x` | A negated number |
| `abs(x)` | The absolute value of a number |
| `x == y` | Check if two numbers have the same value |
| `x != y` | Check if two numbers have different values |
| `x > y` | Check if `x` is greater than `y` |
| `x >= y` | Check if `x` is greater than or equal to `y` |
| `x < y` | Check if `x` is less than `y` |
| `x <= y` | Check if `x` is less than or equal to `y` |

These operations obey the familiar order of operations from your mathematics class, with parentheses available for association:

```python
# multiplication takes precedence over addition
>>> 1 + 2 * 3
7

# grouping operations with parentheses
>>> (1 + 2) * 3
9

# finding the remainder of division between two positive numbers
>>> 11 % 5
1

# checking an inequality
>>> (2 ** 3) < (2 ** 4)
True
```

It should be noted that in many other programming languages, including the out-dated Python 2, dividing two integers would always return an integer - even if mathematically the result should be a fraction. In Python 3, *the quotient of two integers will always return a floating-point number* (i.e. a number that includes a decimal point):

```python
# In many other languages, 3 / 2 returns the integer 1.
# In Python 3, division always returns a floating-point number:
>>> 3 / 2
1.5

>>> 4 / 2
2.0
```

The `//` operator is known as the "floor-divide" operator: it performs division between two numbers and returns the result as an integer by discarding any decimal-places for that number (thus returning the "floor" of that number). This can be used to perform the integer-division traditionally used in other programming languages:

```python
# floor-division
>>> 1 // 3  # 0.3333.. -> 0
0
>>> 3 // 2  # 1.5 -> 1
1
```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Understanding the modulo operator**

The modulo operator, `%`, is not commonly seen in mathematics textbooks. It is, however, a very useful operation to have at our disposal. `x % y` (said as x "mod" y in programmer's jargon) returns the *remainder* of `x / y`, when `x` and `y are non-negative numbers. For example: 

- $\frac{3}{2} = 1 + \frac{1}{2}$. 2 "goes into" 3 one time, leaving a remainder of 1. Thus `3 % 2` returns `1`
- $\frac{9}{3} = 3$. 3 "goes into" 9 three times, and leaves no remainder. Thus `9 % 3` returns `0`

Given this description of the "mod" operator, simplify the following by hand, and then use the IPython console to check your work:

1. `1 % 5`
2. `2 % 5`
3. `22 % 1`
4. `22 % 2`
5. `22 % 3`
6. `22 % 4`
7. `22 % 5`
6. `22 % 6`

Now, given any integer, `n`, what are the possible values that `n % 2` can return? See if you can come up with a simple rule for explaining the behavior of `n % 2`.

</div>

<!-- #region -->
### Python's math module
The standard library's math module provides us with many more mathematical functions, like logarithms and trigonometric functions. A complete listing of them [can be found in the official Python documentation](https://docs.python.org/3/library/math.html#number-theoretic-and-representation-functions). This module must be imported into your code in order to use its functions:

```python
# using the `math` module to use 
# additional mathematical functions
>>> import math
>>> math.sqrt(4.)
2.0

# base-10 log
>>> math.log10(10.)
1.0

# 4! = 4*3*2*1
>>> math.factorial(4)
24
```
<!-- #endregion -->

<!-- #region -->
### Integers
As in traditional mathematics, an integer is any "whole" number: $\dots, -3, -2, -1, 0, 1, 2, 3, \dots$. 

Integers belong to the built-in type `int`, which can be used to convert objects to integers:

```python
>>> type(-3)
int

# `1.3` is not an integer-type object
>>> isinstance(1.3, int)
False

# converting a string to an integer
>>> int("10")
10

# converting a floating-point number to an integer
>>> int(1.3)
1
```

You can create as large an integer as you'd like; Python will allocate as much memory as needed (and ultimately, as is available) to store an integer's exact value:

```python
# you can make an integer as large as you'd like
>>> large_int = 281938481039848500192847576920
```

Integers have some built-in functions available to them, which are detailed in the [official documentation](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-integer-types). The utility of these will likely be quite obscure to new programmers. Just note that they are here for now.
<!-- #endregion -->

<!-- #region -->
### Floating-Point Numbers
A "floating-point" number is a number with a decimal point. Referred to as a "float" for short, this can be used to represent any number, up to a limited number of digits.

These objects belong to the built-in type `float`, which can be used to convert objects to floats:

```python
# examples of "floating-point" numbers
>>> 100. ** 0.5
10.0

>>> 1 / 3
0.3333333333333333

>>> 1 / 2
0.5

>>> type(-2.1)
float

# the integer 10 is not a float-type object
>>> isinstance(10, float)
False

# including a decimal makes the number a float
>>> isinstance(10., float)
True

# converting a string to a floating-point number
>>> float("10.456")
10.456

# converting an integer to a floating-point number
>>> float(-22)
-22.0
```

Floats have a couple of built-in functions available to them, as detailed in the [official documentation](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-float).
<!-- #endregion -->

<!-- #region -->
#### Scientific Notation
A float can also be created using familiar scientific notation. The character `e` is used to represent $\times 10$, and the proceeding number is the exponent. Here are some examples of traditional scientific notation, and their corresponding representation in Python:

$1.38 \times 10^{-4} \rightarrow$ `1.38e-04`

$-4.2 \times 10^{10} \rightarrow$ `-4.2e10`

Python will automatically display a float that possesses many digits in scientific notation:
```python
# python will display many-digit numbers using 
# scientific notation
>>> 0.0000001  # seven leading-zeros
1e-07
```
<!-- #endregion -->

<!-- #region -->
#### Understanding Numerical Precision
Whereas a Python integer can be made to be as large as you'd like, a floating-point number is *limited in the number of digits it can store*. That is, your computer will only use a set amount of memory - 8 bytes (64 bits) on most machines - to store the value of a floating-point number. 

In effect, this means that a float can only be represented with a *numerical precision* of approximately 16 decimal places, when that number is written in scientific notation. The computer will not be able to reliably represent a number's digits beyond those accounted for by the allotted 8 bytes. For instance, the following Python integer is defined with 100 digits, but when this number is converted to a  float, it only retains 15 decimal places in scientific notation:  
```python
# Demonstrating the finite-precision of a float.

# An integer with 100 digits - Python will use as
# much memory as needed to store an integer
>>> int("1"*100)  # creates a string with 100 1s and makes it an int
1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

# Converted to a float, it retains only 
# 16 decimal places, when written in scientific
# notation. This is the precision permitted by 
# 8 bytes of memory.
>>> float("1"*100)  # creates a string with 100 1s and makes it a float
1.111111111111111e+99
```
The computer cannot keep track of those last 84 decimal places because doing so would require more than 8 bytes of memory to store the entire value of that float. If you had been diligently counting stars in the sky (perhaps across many universes, this number far exceeds the estimated number of stars in our universe), you would have just lost track of over $1\times10^{83}$ of them simply by converting your integer count to a float! 

As such, attempting to modify a floating point number in decimal places beyond its numerical precision does not have any effect:

```python
# changing a float beyond its precision has no effect 
>>> 1. + 1e-16
1.0
```

Even in light of this discussion on float precision, you may be shocked and dismayed to see the following outcome of float arithmetic:

```python
# the finite-precision of floats 
# result in non-obvious behavior
>>> 0.1 + 0.1 + 0.1 - 0.3 == 0.
False

# the effects of having finite numerical precision
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
```
This is not a quirk of Python; this is a [well-understood](https://docs.python.org/3/tutorial/floatingpoint.html) aspect of dealing with floating-point numbers with limited numerical precision. To accommodate this, don't check if two floats are "equal". Rather, you should check if they are "close enough in value".
Let me emphasize this:

 **You should never check to see if two floats are exactly equal in value. Instead, you should only check that two floats are approximately equal to one another**. 

The `math` module has a very nice function for this; `math.isclose` will check if the relative difference between two numbers is less than $1 \times 10^{-9}$. You can change this tolerance value along with the type of tolerance-checking used by the function; see its documentation [here](https://docs.python.org/3/library/math.html#math.isclose). Because in the previous example we compare values that are close to 0, we will check if their absolute difference is sufficiently small:

```python
# checking if two float values are "almost equal"
>>> import math

# check: 
# | (0.1 + 0.1 + 0.1 - 0.3) - 0 | < 1x10^{-9}
>>> math.isclose((0.1 + 0.1 + 0.1 - 0.3), 0., abs_tol=1e-9)
True
```
If you do not heed this lesson, it is inevitable that you will end up with serious, hard-to-find bugs in your code. Lastly,
when doing numerical work in Python (and any other programming language), you must understand that the finite numerical precision of floating-point numbers is a source of error, akin to error associated with imprecision with a measuring device, and should be accounted for in your analysis (if error analysis is warranted).

Python's [decimal module](https://docs.python.org/3.0/library/decimal.html) can be used to define higher (or lower) precision numbers than permitted by the standard 8-byte floats. Furthermore, all arithmetic involving decimal numbers from this module is guaranteed to be *exact*, meaning that `0.1 + 0.1 + 0.1 - 0.3` would be exactly `0.`. There is also a built-in [fractions module](https://docs.python.org/3/library/fractions.html#module-fractions), which provides tools for working with exact representations of rational numbers. Although we will not be using them here, it is very important to keep in mind that these modules exist and that floating point numbers are not the only way around the number line in Python. 
<!-- #endregion -->

<!-- #region -->
### Complex Numbers
In mathematics, a "complex number" is a number with the form $a + bi$, where $a$ and $b$ are real-valued numbers, and $i$ is defined to be the number that satisfies the relationship $i^2 = -1$. Because no real-valued number satisfies this relationship, $i$ is called the "imaginary number". 

Weirdo electrical engineers use the symbol $j$ in place of $i$, which is why Python displays the complex number $2 + 3i$ as `2+3j` (this is actually because $i$ typically denotes current; we like electrical engineers too).

Along with the `a + bj` syntax,  built-in type `complex` can be used to create complex-type numbers: 

```python
# creating complex numbers
>>> 2 + 3j
(2+3j)

>>> complex(2, 3)
(2+3j)

>>> complex(0, 1)**2
(-1+0j)

>>> type(2+3j)
complex

>>> isinstance(2-4j, complex)
True
```

Note that `j` is not, by itself, reserved as a special placeholder for $i$. Rather, `j` must be preceded immediately with a numerical literal (i.e. you cannot use a variable) in order for the Python interpreter to treat it as a complex number.

```python
# `j` by itself is treated like any other character
>>> j
NameError: name 'j' is not defined

# `1j` is interpreted as the imaginary number
>>> (1j) ** 2
(-1+0j)
```

You can access `a` and `b` from `a + bj`, the real and imaginary parts of the complex number, respectively.
```python
# Accessing the real and imaginary parts of
# a complex number.
>>> x = complex(1.2, -3.4)
>>> x.real
1.2
>>> x.imag
-3.4
```

The `cmath` ("complex math") module provides a collection of mathematical functions defined for complex numbers. For a complete listing of these functions, refer to the [official documentation](https://docs.python.org/3/library/cmath.html#module-cmath).
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info">

**Reading Comprehension: Working with numbers in Python**

1\. In Python, performing an arithmetic operation, such as addition or multiplication, on two integers will return an integer, and performing an operation on two floats will return a float:
```python
>>> 2 * 3
6

>>> 2.0 * 3.0
6.0
```

For which operation, among `+ - * / **`, does this *not* hold?
<!-- #endregion -->

2\. What type of number will be returned if you perform a mathematical operation using an integer and a floating-point number? Does this hold for all the arithmetic operations? Determine this by trial and error.

3\. Given the function $f(x) = e^{|x - 2|}$, make use of the `math` module to compute $f(-0.2)$.

4\. Using Python's syntax for scientific notation, write an expression that verifies that one trillion divided by one billion is equal to one thousand
</div>

<!-- #region -->
### Augmented Assignment Statements
Python provides a nice "shortcut" for updating a variable via an arithmetic operation. For example, suppose you want to increase the value of `x` by 1. Currently, we would update `x` as follows:
```python
# incrementing `x` by 1
>>> x = 5
>>> x = x + 1
>>> x 
6
```

We can make use of a special assignment operation `+=` to perform this update in an abbreviated way.
```python
# using `+=` to increment `x` by 1
>>> x = 5
>>> x += 1  # equivalent to: `x = x + 1`
>>> x
6
```

`+=` is a type of *augmented assignment statement*. In general, an augmented assignment performs a mathematical operation on a variable, and then updates that variable using the result. Augmented assignment statements are available for all of the arithmetic operations. Assuming `x` and `n` are both types of numbers, the following summarizes the available arithmetic augmented assignment statements that we can perform on `x`, using `n`:

- `x += n` $\rightarrow$ `x = x + n`
- `x -= n` $\rightarrow$ `x = x - n`
- `x *= n` $\rightarrow$ `x = x * n`
- `x /= n` $\rightarrow$ `x = x / n`
- `x //= n` $\rightarrow$ `x = x // n`
- `x **= n` $\rightarrow$ `x = x ** n`
<!-- #endregion -->

<!-- #region -->
### Improving The Readability of Numbers
Python version 3.6 introduced the ability to include underscores between the digits of a number as a visual delimiter. This character can be used to improve the readability of long numbers in your code. For example the number `662607004` can be rewritten as `662_607_004`, using `_` to delimit digits separated by orders of one thousand. Leading, trailing, or multiple underscores in a row are not allowed; otherwise this character can be included anywhere within a numerical literal.

```python
# examples of using `_` as a visual delimiter in numbers
>>> 1_000_000  # this is nice!
1000000

# this is gross but is permitted
>>> 2_3_4.5_6_7  
234.567

# underscores work with all variety of numerical literals
>>> 10_000j  
10000j
```

<div class="alert alert-warning">

**Compatibility Warning**

The permitted use of the underscore character, `_`, in numerical literals was introduced in Python 3.6. Thus utilizing this syntax in your code will render it incompatible with Python 3.5 and earlier. 

</div>
<!-- #endregion -->

<!-- #region -->
## The Boolean Type
There are two boolean-type objects: `True` and `False`; they belong to the built-in type `bool`. We have already seen that the `isinstance` function either returns `True` or `False`, as a given object either is or isn't an instance of a specific type. 

```python
# the two boolean-objects: `True` and `False`
>>> type(True)
bool

# `False` is a boolean-type object
>>> isinstance(False, bool)
True
```
`True` and `False` must be specified with capital letters in Python. These should not be confused with strings; note that there are no quotation marks used here.

### Logic Operators
Python provides familiar operators for performing basic boolean logic: 

| Logic Operation | Symbolic Operator            
| --------------- | ------------------- |
| `and`           | `&`                 | 
| `or`            | <code>&#124;</code> |          
<!-- #endregion -->

<!-- #region -->
```python
# demonstrating boolean-logic operators
>>> True or False
True

>>> True and False
False

>>> not False 
True
```

Operator symbols are available in place of the reserved words `and` and `or`:
```python
# demonstrating the symbolic logic operators
>>> False | True  # equivalent to: `False or True`
True

>>> False & True  # equivalent to: `False and True`
False
```
That being said, it is generally more "Pythonic" (i.e. in-vogue with Python users) to favor the use of the word-operators over the symbolic ones. 

Multiple logic operators can be used in a single line and parentheses can be used to group expressions:
```python
>>> (True or False) and True
True
```

Comparison statements used in basic mathematics naturally return boolean objects.
```python
>>> 2 < 3
True

>>> 10.5 < 0
False

>>> (2 < 4) and not (4 != -1)
False
```

The `bool` type has additional utilities, which will be discussed in the "Conditional Statements" section.
<!-- #endregion -->

<!-- #region -->
### Boolean Objects are Integers
The two boolean objects `True` and `False` formally belong to the `int` type in addition to `bool`,  and are associated with the values `1` and `0`, respectively:

```python
>>> isinstance(True, int)
True

>>> int(True)
1

>>> isinstance(False, int)
True

>>> int(False)
0
```

As such, they can be used in mathematical expressions interchangeably with `1` and `0`  
```python
>>> 3*True - False  # equivalent to: 3*1 + 0 
3

>>> True / False  # equivalent to: 1 / 0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-4-f8487d9d0863> in <module>()
----> 1 True / False

ZeroDivisionError: division by zero
```

The purpose of having `True` and `False` double as integers is beyond the scope of this section. It is simply useful to be aware of these facts so that this behavior is not completely alien to you as you begin to write code in Python.
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Boolean expressions**

1\. Assuming `x` is a an integer-type, write a comparison statement that will return `True` if `x` is an even number, and `False` otherwise. (Hint: recall the purpose of the `%` operator)

2\. Assuming `x` and `y` are both real-valued numbers (i.e. not complex numbers), write a line of code that will return `False` if: `x` and `y` are within 0.9 of one another, and `x` is a positive number. (Hint: try writing the expression that will return `True` for this condition, and then negate it)

3\. Write an expression that returns `True` if `x` is a boolean-type object or a float-type object.

</div>

<!-- #region -->
## The None-Type
There is a simple type, `NoneType` that has exactly one object: `None`. `None` is used to represent "null"... nothing.
```python
# `None` is the *only* object belonging to NoneType
>>> type(None)
NoneType
```
As such, instead of checking if an object belongs to NoneType, you should simply check if the object is `None`. Python reserves `is` as an operation that checks if two objects are identical. This is different than `==`, which checks if two objects are associated with the same value or state:
```python
# Check if an object "is" None, instead
# of checking if it is of NoneType
>>> x = 22

>>> x is None
False

>>> x is not None
True

>>> y = None

>>> y is None
True
```
`None` appears frequently, and is often used as a placeholder in code. Here is a simple example where `None` could be useful; don't worry that this code may not make perfect sense to you yet:

```python
# Demonstrating the use of `None` as a placeholder

# In this code, we want to get the first
# item in a list that is greater than 10, and notify
# the user if there is no such number

large_num = None

for number in [1, 2, 3, 4]:
    if number > 10:
        large_num = number
        break

if large_num is None:
    print("The list did not contain any number larger than 10")

```
<!-- #endregion -->

<!-- #region -->
## Strings
### Introducing the string type
The string type is used to store written characters. A string can be formed using:

- single quotes: `'Hello world'`
- double quotes: `"Hello world"`
- triple quotes: `"""Hello world"""` or `'''Hello world'''` 

```python
# Strings contain written characters, even those
# not found in the english alphabet!
>>> "hello, 你好, Olá, 123"
'hello, 你好, Olá, 123'
```
By default, Python 3 uses [UTF-8 unicode](https://docs.python.org/3/howto/unicode.html#unicode-howto) to represent this wide variety of characters. Don't worry about this detail beyond making note of it, for now.

Strings belong to the built-in `str` type, which can be used to convert non-string objects into strings.
```python
# the type `str`
>>> type("hello")
str

>>> isinstance("83", str)
True

# Using the type `str` to convert non-string objects
# into strings.
>>> str(10.34)
'10.34'

>>> str(True)
'True'
```
Once a string is formed, it cannot be changed (without creating an entirely new string). Thus a given string object cannot be "mutated" - a string is an *immutable* object.

As the string stores a *sequence* of characters, Python provides a means for accessing individual characters and subsequences of characters from a string:
```python
>>> sentence = "The cat in the hat."
>>> sentence[0]
'T'
>>> sentence[0:3]
'The'
```
Strings are not the only sequence-type in Python; lists and tuples are examples of sequences as well. We will reserve a separate section to learn about the common interface that Python has for all of its types that are sequential in nature, including the "indexing" and "slicing" demonstrated here.

### String essentials
We will only scratch the surface with strings, touching on some essentials. Please refer to the [official Python tutorial](https://docs.python.org/3/tutorial/introduction.html#strings) for a more extensive, but still informal, overview of strings.

In a string, `\n` is treated as a single character. It denotes a new-line in a string, and will be rendered thusly when the string is printed. Similarly, `\t` will render as a tab-character.

```python
# using `\n` to create a newline
>>> print("hi...\n...bye")
hi...
...bye
```

Using triple quotes allows you to write a block-string, meaning that you can include text on multiple lines, and it is all still treated as one string:

```python
# using triple-quotes to write a multi-line string
>>> x = """ I am a string.
I am part of the same string.
    me... too!"""

>>> x 
' I am a string.\nI am part of the same string.\n    me... too!'
 
```

Python's strings have a large number of fantastic, built-in functions available to them. It is *very important* that you familiarize yourself with these functions by looking over [the official documentation](https://docs.python.org/3/library/stdtypes.html#string-methods). To demonstrate a few of these:
```python
# demonstrating a few of the built-in functions for strings
>>> "hello".capitalize()
'Hello'

# join a list of strings, using "..."
>>> "...".join(["item1", "item2", "item3"])
'item1...item2...item3'

# split a string wherever ", " occurs
>>> 'item1, item2, item3'.split(", ")
['item1', 'item2', 'item3']

# does this string end with ".py"?
>>> "script.py".endswith(".py")
True

# does this string start with "sc"?
>>> "script.py".startswith("sc")
True

# insert objects into a string, in its 
# "formatting" fields {}
>>> "x: {}, y: {}, z: {}".format(3.2, 8.4, -1.0)
'x: 3.2, y: 8.4, z: -1.0'

# Are the characters in the string
# numerical digits?
>>> "7".isdigit()
True

```

### Formatting strings
Python provides multiple syntaxes for formatting strings; these permit us to do things like programmatically inject the values of variables into strings, align fields using whitespace, and control the number of decimal places with which numbers are displayed in a string. This section is designed to simply expose the reader to the different varieties of string-formatting. 

[pyformat.info](https://pyformat.info) is the best resource to consult to see an exhaustive (but still intuitive) treatment of string-formatting in Python. You can also refer to the official documentation [here](https://docs.python.org/3/library/string.html#format-examples).

In Python 3, you can leverage the `format` method towards this end:

```python
# using `format` to replace placeholders with values
>>> "{name} is {age} years old".format(name="Bruce", age=80)
'Bruce is 80 years old'

# padding a string with leading-spaces so that it has at least 8 characters
>>> "{item:>8}".format(item="stew")
'   stew'
```
Note that you may encounter the use of the cryptic `%` operator to format strings to the same effect:

```python
# using `%` to  format strings (avoid this)
>>> name = "Selina"
>>> "My name is %s" % name
'My name is Selina'
```
this is a relic of Python 2; it is recommend that you avoid this formatting syntax.

If you are using Python 3.6 or beyond, then you have the luxury of being able to use f-strings, which provide a supremely convenient means for formatting strings. Here is an example of an f-string in action:

```python
# an example of an 'f-string'
>>> batman = 12
>>> catwoman = 10
>>> f"Batman has {batman} apples. Catwoman has {catwoman} apples. Together, they have {batman + catwoman} apples"
'Batman has 12 apples. Catwoman has 10 apples. Together, they have 22 apples'
```

See that an f-string has a special syntax; an f-string is denoted by preceding the opening quotation mark with the lowercase f character:
```python
# this is a typical empty string
>>> ""
''

# this is an empty f-string
>>> f""
''
```

An f-string is special because it permits us to write Python code *within* a string; any expression within curly brackets, `{}`, will be executed as Python code, and the resulting value will be converted to a string and inserted into the f-string at that position.

```python
>>> x = 7.9
>>> f"x is a {type(x)}-number. Its value is {x}. The statement 'x is greater than 5' is {x > 5}"
"x is a <class 'float'>-number. Its value is 7.9. The statement 'x is greater than 5' is True"
```

As seen in the preceding examples, this permits us to elegantly include variables in our strings and even do things like call functions within the string construction syntax.

<div class="alert alert-warning">

**f-string Compatibility**: 

The 'f-string' syntax was introduced in Python 3.6. It is not available in earlier versions of Python.
</div>

### Official documentation for strings
It is highly recommended that you take time to read over all of the functions that are built-in to a string.

- [Built-in functions for strings](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Formatting strings](https://docs.python.org/3/library/string.html#format-examples)
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Strings**

To answer some of the following questions, you will need to peruse the documentation for the built-in functions of strings. It may take a bit of experimentation to understand the documentation's use of square-brackets to indicate optional inputs for a function.

1\. Use a function that will take the string `"cat"`, and returns the string `"   cat    "` (which has a length of 11, including the letters c, a, t). Now, change the way you call the function so that it returns `"----cat----"` instead. 

2\. Replace the first three periods of this string with a space-character: `"I.am.aware.that.spaces.are.a.thing"`


3\. Remove the whitespace from both ends of: `"  basket    "` 


4\. Create a string that will print as (the second line begins with a tab-character):
```
Hello
	over there
```

5\. Convert the integer `12` to the string `"12"`.

6\. Only kids 13 and up are allowed to see Wayne's World. Given the variables `name` (a string) and `age` (an integer), use an f-string that will display: "NAME is old enough to watch the movie: BOOL", where NAME is to be replaced with the kid's name, and BOOL should be `True` if the kid is at least 13 years old, and `False` otherwise.

</div>

<!-- #region -->
## Lists
A `list` is a type of Python object that allows us to store a sequence of other objects. One of its major utilities is that it provides us with means for updating the contents of a list later on. 

A list object is created using square-brackets, and its contents are separated by commas: `[item1, item2, ..., itemN]`. Its contents need not be of the same type of object.

```python
# a list-type object stores a sequence of other objects
>>> [3.5, None, 3.5, True, "hello"]
[3.5, None, 3.5, True, 'hello']

>>> type([1, 2, 3])
list

>>> isinstance([1, 2], list)
True 

# constructing an empty list
>>> []
[]

# constructing a list with only one member
>>> ["hello"]
["hello"]
```

You can also include variables, equations, and other Python expressions in the list constructor; Python will simplify these expressions and construct the list with the resulting objects.
```python
# the list constructor will simplify expressions 
# and store their resulting objects
>>> x = "hello"
>>> [2 < 3, x.capitalize(), 5**2, [1, 2]]
[True, 'Hello', 25, [1, 2]]
```

The built-in `list` type can be used to convert other types of sequences (and more generally, any *iterable* object, which we will discuss later) into a list:
```python
# `list` forms a list out of the contents of other sequences
>>> list("apple")
['a', 'p', 'p', 'l', 'e']
```
### Lists are sequences
Like a string, the ordering of a list's contents matters, meaning that a list is sequential in nature.
```python
# A list's ordering matters
>>> [1, "a", True] == [1, True, "a"]
False
```

Thus a list supports the same mechanism for accessing its contents, via indexing and slicing, as does a string. Indexing and slicing will be covered in detail in the next section.
```python
# Accessing the contents of a list with indexing and slicing
>>> x = [2, 4, 6, 8, 10]

# `x` contains five items
>>> len(x)
5

# access the 0th item in the list via "indexing"
>>> x[0]
2

# access a subsequence of the list via "slicing"
>>> x[1:3]
[4, 6]
```

### Lists can be "mutated"
We will encounter other types of containers in Python, what makes the list stand out is that the *contents of a list can be changed after the list has already been constructed*. Thus a list is an example of a *mutable* object.
```python
# changing a list after it has been constructed
>>> x = [2, 4, 6, 8, 10]
>>> y = [2, 4, 6, 8, 10] 

# "set" the string 'apple' into position 1 of `x` 
>>> x[1] = "apple"
>>> x
[2, 'apple', 6, 8, 10]

# replace a subsequence of `y`
>>> y[1:4] = [-3, -4, -5]
>>> y
[2, -3, -4, -5, 10]
```

The built-in list-functions "append" and "extend" allow us to add one item and multiple items to the end of a list, respectively:
```python
>>> x = [2, 4, 6, 8, 10]

# use `append` to add a single object to the end of a list
>>> x.append("moo")
>>> x
[2, 4, 6, 8, 10, 'moo']

# use `extend` to add a sequence of items to the end of a list
>>> x.extend([True, False, None])
>>> x
[2, 4, 6, 8, 10, 'moo', True, False, None]
```

The "pop" and "remove" functions allow us to remove an item from a list based on its position in the list, or by specifying the item itself, respectively.
```python
>>> x = ["a", "b", "c", "d"]

# pop the position-1 item out from a list
# `pop` will return the item that gets removed.
>>> x.pop(1) 
'b'

>>> x
['a', 'c', 'd']

# remove the object "d" from the list
>>> x.remove("d")
>>> x
['a', 'c']
```

### Official documentation for lists
It is highly recommended that you take time to read over all of the functions that are built-in to a list. These are all designed to allow us to either inspect or mutate the contents of a list.

- [Built-in functions for a list](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Lists**

To answer some of the following questions, you will need to peruse the documentation for the built-in functions of lists.

1\. Create a list whose sole entry is the `None` object.

2\. Assign to the variable `k` a list that contains an integer, a boolean, and a string, in that order. Then, add two more entries to the end of the list: a float and a complex number.  

3\. Alphabetize the list of names: `["Jane", "Adam", "Ryan", "Bob", "Zordon", "Jack", "Jackenzie"]`. 

</div>

<!-- #region -->
## Summary
The term "object" is a catch-all in Python, meaning anything that we can assign to a variable. Objects behave differently from one another according to what "type" a given object is. 

We reviewed several fundamental object types in Python:

- `int`, `float`, `complex`: the numerical types
- `bool`: the boolean type. `True` and `False` are the only boolean-type objects
- `NoneType`: the "null" type; `None` is *the only object that belongs to this type*
- `str`: the string type
- `list`: the list type

The built-in function `type` permits us to check the type of any object:
```python
>>> type(3.2)
float

>>> type(True)
bool
```

The built-in function `isinstance` should be used to check if an object is of a specific type:
```python
>>> x = 2 + 3
>>> isinstance(x, int)
True
```
The only exception to this is if you want to check if an object is of the type `NoneType`, since this is only possible if the object is  `None`; thus it is "cleaner" to directly check this:
```python
>>> x = None
>>> x is None
True
```

Objects of different types have different built-in functions available to them:
```python
>>> x = "I am a farmer.. moo"
>>> x.upper()
'I AM A FARMER.. MOO'

>>> y = 0.5
>>> y.as_integer_ratio()
(1, 2)

>>> z = [1, 2]
>>> z.append(3)
>>> z
[1, 2, 3]
```

You should leverage the official documentation, for which links were provided throughout this section, whenever you are wondering how to best do a specific task with a given type of object.

As a final reminder, we saw that that an integer in Python is able to hold a value with arbitrarily-many digits. A floating-point number, on the other hand, is restricted in the number of "significant" digits it can hold. Thus, where it is perfectly fine to check if two integers are exactly equal:
```python
# checking if two integers are equal is great!
>>> 2 + 2 == 4
True
```
you should never rely on two floats being exactly equal. Instead, check if they are close in value:
```python
# checking if two floats are equal is lame!
>>> 0.1 + 0.1 + 0.1 - 0.3 == 0.
False

>>> abs((0.1 + 0.1 + 0.1 - 0.3) - 0.) < 1e-12
True
```

It is very important to remember this issue of the limited numerical precision of a floating point number.
<!-- #endregion -->

## Links to Official Documentation

- [Integers](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-integer-types)
- [Floating point numbers](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-float)
- [The standard library's math module](https://docs.python.org/3/library/math.html#number-theoretic-and-representation-functions)
- [The standard library's complex-valued math module](https://docs.python.org/3/library/cmath.html#module-cmath)
- [Strings](https://docs.python.org/3/library/stdtypes.html#string-methods)
   - [String tutorial](https://docs.python.org/3/tutorial/introduction.html#strings)
   - [Formatting strings](https://docs.python.org/3.4/library/string.html#format-examples)
- [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)


## Reading Comprehension Exercise Solutions:


**Understanding the modulo operator: Solution**

If `n` is an even integer, then 2 will divide into it evenly, and thus there is no remainder. If `n` is odd, then `n / 2` must have a remainder of 1. Thus:

- `n % 2 ` = 0 if `n` is an even number
- `n % 2 ` = 1 if `n` is an odd number

<!-- #region -->
**Working with numbers in Python: Solution**

1\. The division operator, `/`, will return a floating-point number even if it is operating on two integer-type numbers.

2\. For all of the arithmetic operations, `+ - * / **`, operating on a floating-point number and an integer will return a floating-point number:
```python
>>> 2 * 3.0
6.0

>>> -1.0 + 2
1.0
```

3\. Given the function $f(x) = e^{|x - 2|}$, make use of the `math` module to compute $f(-0.2)$.
```python
>>> from math import exp
>>> x = -0.2
>>> exp(abs(x - 2))
9.025013499434122
```

4\. Using Python's syntax for scientific notation, write an expression that verifies that one trillion divided by one billion is equal to one thousand.

> As cautioned above, we should avoid checking to see if two floating point numbers are exactly equal, and instead simply ensure that they are close in value. Keep in mind that a number written Python's using scientific syntax will produce a float. 

```python
>>> from math import isclose
>>> isclose(1e12 / 1e9, 1e3)
True
```
<!-- #endregion -->

<!-- #region -->
**Boolean expressions: Solutions**
```python
# 1. Write an a comparison-statement that will return 
#    True if x is an even number
x%2 == 0
```

```python
# 2. Write a line of code that will return False if: 
#    x and y are within 0.9 of one another, and x is a positive number. 
not (abs(x - y) < 0.9 and 0 < x)
# alternatively,
abs(x - y) > 0.9 or 0 > x
```

```python
# 3. Write an expression that returns True if 
#    x is a boolean-type object or a float-type object
isinstance(x, bool) or isinstance(x, float)
```
<!-- #endregion -->

<!-- #region -->
**Strings: Solutions**

```python
# 1.  Use a function that will take the string "cat" 
#     and returns the string "   cat    "
>>> "cat".center(11)
'    cat    '

>>> "cat".center(11, "-")
'----cat----'
```

```python
# 2. Replace the first three periods of this string with 
#    a space-character: 
>>> "I.am.aware.that.spaces.are.a.thing".replace(".", " ", 3)
'I am aware that.spaces.are.a.thing'
```

```python
# 3. Remove the whitespace from both ends 
#    of: "  basket    "
>>> "  basket    ".strip()
'basket'
```

```python
# 4.
>>> print("Hello\n\tover there")
Hello
	over there
```

```python
# 5. Convert the integer 12 to the string "12"
>>> str(12)
'12'
```

Only kids 13 and up are allowed to see Wayne's World. Given the variables `name` (a string) and `age` (an integer), use an f-string that will display: "NAME is old enough to watch the movie: BOOL", where NAME is to be replaced with the kid's name, and BOOL should be `True` if the kid is at least 13 years old, and `False` otherwise. Use the example `name = "Alfred"`, `age = 10`.

```python
# 6. Use an f-string that will display: 
# "NAME is old enough to watch the movie: BOOL", 
# where NAME is to be replaced with the kid's name, 
# and BOOL should be `True` if the kid is at least 
# 13 years old, and `False` otherwise.
>>> name = "Alfred"
>>> age = 10
>>> f"{name} is old enough to watch the movie: {age >= 13}"
'Alfred is old enough to watch the movie: False'
```

<!-- #endregion -->

<!-- #region -->
**Lists: Solutions**

```python
# Create a list whose sole entry is the None object.
>>> [None]
[None]
```

```python
# 2. Assign the variable k to a list that contains an 
#    integer, a boolean, and a string, in that order. 
#    Then, add two more entries to the end of the 
#    list - a float and a complex number.
>>> k = [4, False, "moo"]
>>> k.extend([3.14, complex(9, -2)])
>>> k
[4, False, 'moo', 3.14, (9-2j)]
```

```python
# 3. Alphabetize the list of names:
>>> names = ["Jane", "Adam", "Ryan", "Bob", "Zordon", "Jack", "Jackenzie"]

# The documentation for `sort` says that the sorting happens "in-place". This
# means that the original list is replaced by the sorted list. The alternative
# would be that `sort` returns a new, sorted list, without changing the list
# assigned to `names`.
>>> names.sort()
>>> names
['Adam', 'Bob', 'Jack', 'Jackenzie', 'Jane', 'Ryan', 'Zordon']
```
<!-- #endregion -->
