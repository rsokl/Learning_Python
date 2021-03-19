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
   :description: Topic: Functions and Function Signatures, Difficulty: Medium, Category: Section
   :keywords: functions, *args, **kwargs, signature, default parameter, docstring, return, vowel count, syntax, basics
<!-- #endraw -->

<!-- #region -->
# Basics of Functions
<div class="alert alert-warning">

**Note**: 

There are reading-comprehension exercises included throughout the text. These are meant to help you put your reading to practice. Solutions for the exercises are included at the bottom of this page.
</div>

Defining a function allows you to encapsulate a segment of code, specifying the information that enters and leaves the code. You can make use of this "code-capsule" repeatedly and in many different contexts. For example, suppose you want to count how many vowels are in a string. The following defines a function that accomplishes this:

```python
def count_vowels(in_string):
    """ Returns the number of vowels contained in `in_string`"""
    num_vowels = 0
    vowels = "aeiouAEIOU"
    
    for char in in_string:
        if char in vowels:
            num_vowels += 1  # equivalent to num_vowels = num_vowels + 1
    return num_vowels
```

Executing this code will define the *function* `count_vowels`. This function expects to be passed one object, represented by `in_string`, as an *input argument*, and it will *return* the number of vowels stored in that object. Invoking `count_vowels`, passing it an input object, is referred to as *calling* the function:

```python
>>> count_vowels("Hi my name is Ryan")
5
```

The great thing about this is that it can be used over and over!

```python
>>> count_vowels("Apple")
2

>>> count_vowels("envelope")
4
```

In this section, we will learn about the syntax for defining and calling functions in Python
<!-- #endregion -->

<div class="alert alert-info">

**Definition**: 

A Python **function** is an object that encapsulates code. *Calling* the function will execute the encapsulated code and *return* an object. A function can be defined so that it accepts *arguments*, which are objects that are to be passed to the encapsulated code.  
</div>


## The `def` Statement
Similar to `if`, `else`, and `for`, the `def` statement is reserved by the Python language to signify the definition of functions (and a few other things that we'll cover later). The following is the general syntax for defining a Python function:

```
def <function name>(<function signature>):
    """ documentation string """
    <encapsulated code>
    return <object>
```

- `<function name>` can be any valid variable name, and *must* be followed by parentheses and then a colon.
- `<function signature>` specifies the input arguments to the function, and may be left blank if the function does not accept any arguments (the parentheses must still be included, but will not encapsulate anything).
- The documentation string (commonly referred to as a "docstring") may span multiple lines, and should indicate what the function's purpose is. It is optional.
- `<encapsulated code>` can consist of general Python code, and is demarcated by being indented relative to the `def` statement.
- `return` if reached by the encapsulated code, triggers the function to return the specified object and end its own execution immediately.
 
The `return` statement is also reserved by Python. It denotes the end of a function; if reached, a `return` statement immediately concludes the execution of the function and returns the specified object. 

Note that, like an if-statement and a for-loop, the `def` statment must end in a colon and the body of the function is [delimited by whitespace](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Introduction.html#Python-Uses-Whitespace-to-Delimit-Scope):

<!-- #region -->
```python
# wrong indentation
def bad_func1():
x = 1
    return x + 2
```
***
```python
# wrong indentation
def bad_func2():
    x = 1
return x + 2
```
***
```python
# missing colon
def bad_func3()
    x = 1
    return x + 2
```
***
```python
# missing parenthesis
def bad_func4:
    x = 1
    return x + 2
```

***
```python
# this is ok
def ok_func():
    x = 1
    return x + 2
```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Writing a Basic Function**

Write a function named `count_even`. It should accept one input argument, named `numbers`, which will be an iterable containing integers. Have the function return the number of even-valued integers contained in the list. Include a reasonable docstring.

</div>

<!-- #region -->
## The `return` Statement
In general, any Python object can follow a function's `return` statement. Furthermore, an **empty** `return` statement can be specified, or the **return** statement of a function can be omitted altogether. In both of these cases, *the function will return the* `None` *object*.

```python
# this function returns `None`
# an "empty" return statement
def f():
    x = 1
    return
```

```python
# this function returns `None`
# return statement is omitted
def f():
    x = 1
```
<!-- #endregion -->

<!-- #region -->
All Python functions return *something*. Even the built-in `print` function returns `None` after it prints to standard-output! 

```python
# the `print` function returns `None`
>>> x = print("hi")
hi

>>> x is None
True
```
<div class="alert alert-warning">

**Warning!** 

Take care to not *mistakenly* omit a return statement or leave it blank. You will still be able to call your function, but it will return `None` no matter what!
</div>

A function also need not have any additional code beyond its return statement. For example, we can make use of `sum` and a generator comprehension (see the previous section of this module) to shorten our `count_vowels` function:

```python
# the returned object of a function can be specified straight-away
def count_vowels(in_string): 
    """ Returns the number of vowels contained in `in_string`"""
    return sum(1 for char in in_string if char in "aeiouAEIOU")
```
<!-- #endregion -->

<!-- #region -->
### Multiple `return` Statements
You can specify more than one `return` statement within a function. This can be useful for handling edge-cases or optimizations in your code. Suppose you want your function to compute $e^{x}$, using a [Taylor series](https://en.wikipedia.org/wiki/Taylor_series#Exponential_function) approximation. The function should immediately return `1.0` in the case that $x = 0$:

```python
def compute_exp(x):
    """ Use a Taylor Series to compute e^x """
    if x == 0:
        return 1.0

    from math import factorial
    return sum(x**n / factorial(n) for n in range(100))
```

If `x==0` is `True`, then the first `return` statement is reached. `1.0` will be returned and the function will be "exited" immediately, without ever reaching the code following it.
<!-- #endregion -->

As stated above, a `return` statement will trigger a function to end its execution immediately when reached, even when subsequent code follows it. *It is impossible for multiple `return` statements to be visited within a single function call*. Thus if you want to return multiple items, then your function must return a single container of those items, like a list or a tuple.

<!-- #region -->
```python
# Returning multiple items from a function
def bad_f(x):
    """ return x**2 and x**3"""
    return x**2 
    # this code can never be reached!
    return x**3

def good_f(x):
    """ return x**2 and x**3"""
    return (x**2, x**3)
```
```python
>>> bad_f(2)
4

>>> good_f(2)
(4, 8)
```
<!-- #endregion -->

<!-- #region -->
## Inline Functions
Functions can be defined in-line, as a single return statement:

```python
def add_2(x):
    return x + 2
```

can be rewritten as:

```python
def add_2(x): return x + 2
```

This should be used sparingly, for exceedingly simple functions that can be easily understood without docstrings.
<!-- #endregion -->

<!-- #region -->
## Arguments
A sequence of comma-separated variable names can be specified in the function signature to indicated *positional* arguments for the function. For example, the following specifies `x`, `lower`, and `upper` as input arguments to a function, `is_bounded`:

```python
def is_bounded(x, lower, upper):
    return lower <= x <= upper
```

This function can then be passed its arguments in several way:

### Specifying Arguments by Position
The objects passed to `is_bounded` will be assigned to its input variables based on their positions. That is, `is_bounded(3, 2, 4)` will assign `x=3`, `lower=2`, and `upper=4`, in accordance with the positional ordering of the function's input arguments:

```python
# evaluate: 2 <= 3 <= 4
# specifying inputs based on position
>>> is_bounded(3, 2, 4)
True
```

Feeding a function too few or too many arguments will raise a `TypeError`
```python
# too few inputs: raises error
is_bounded(3)

# too many inputs: raises error
is_bounded(1, 2, 3, 4)
```

### Specifying Arguments by Name
You can provide explicit names when specifying the inputs to a function, in which case ordering does not matter. This is very nice for writing clear and flexible code:
```python
# evaluate: 2 <= 3 <= 4
# specify inputs using explicit input names
>>> is_bounded(lower=2, x=3, upper=4)
True
```

You can mix-and-match positional and named input by using position-based inputs first:

```python
# evaluate: 2 <= 3 <= 4
# `x` is specified based on position
# `lower` and `upper` are specified by name
>>> is_bounded(3, upper=4, lower=2)
True
```

Note that if you provide a named input, all the inputs following it must also be named:

```python
# positional arguments cannot follow named arguments
>>> is_bounded(3, lower=2, 4)
SyntaxError: positional argument follows keyword argument
```
<!-- #endregion -->

<!-- #region -->
### Default-Valued Arguments
You can specify default values for input arguments to a function. Their default values are utilized if a user does not specify these inputs when calling the function. Recall our `count_vowels` function. Suppose we want the ability to include "y" as a vowel. We know, however, that people will typically want to exclude "y" from their vowels, so we can exclude "y" by default:

```python
def count_vowels(in_string, include_y=False): 
    """ Returns the number of vowels contained in `in_string`"""
    vowels = "aeiouAEIOU"
    if include_y:
        vowels += "yY"  # add "y" to vowels  
    return sum(1 for char in in_string if char in vowels)
```

Now, if only `in_string` is specified when calling `count_vowels`, `include_y` will be passed the value `False` by default:

```python
# using the default value: exclude y from vowels
>>> count_vowels("Happy")
1
```

This default value can be overridden:
```python
# overriding the default value: include y as a vowel
>>> count_vowels("Happy", True)
2

# you can still specify inputs by name
>>> count_vowels(include_y=True, in_string="Happy")
2
```

Default-valued input arguments must come after all positional input arguments in the function signature:
```python
# this is ok
def f(x, y, z, count=1, upper=2):
    return None
```

```python
# this will raise a syntax error
def f(x, y, count=1, upper=2, z):
    return None
```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Functions and Arguments**

Write a function, `max_or_min`, which accepts two positional arguments, `x` and `y` (which will hold numerical values), and a `mode` variable that has the default value `"max"`. 

The function should return `min(x, y)` or `max(x, y)` according to the `mode`. Have the function return `None` if `mode` is neither `"max"` nor `"min"`. 

Include a descriptive doc-string.

</div>

<!-- #region -->
### Accommodating an Arbitrary Number of Positional Arguments
Python provides us with a syntax for defining a function, which can be called with an arbitrary number of positional arguments. This is signaled by the syntax `def f(*<var_name>)`.

```python
# The * symbol indicates that an arbitrary number of
# arguments can be passed to `args`, when calling `f`.
def f(*args):
    #  All arguments passed to `f` will be "packed" into a 
    #  tuple that is assigned to the variable `args`.
    # `f()`  will assign `args = tuple()`
    # `f(x, y, ...)` will assign `args = (x, y, ...)`
    return args
```

Because Python cannot foresee how many arguments will be passed to `f`, all of the objects that are passed to it will be *packed into a tuple*, which is then assigned to the variable `args`:

```python
# pass zero arguments to `f`
>>> f()            
()

# pass one argument to `f`
>>> f(1)           
(1,)

# pass three arguments to `f`
>>> f((0, 1), True, "cow")  
((0, 1), True, "cow")
```

This syntax can be combined with positional arguments and default arguments. Any variables specified after a packed variable *must be called by name*:
```python
def f(x, *seq, y):
    print("x is: ", x)
    print("seq is: ", seq)
    print("y is: ", y)
    return None
```
```python
>>> f(1, 2, 3, 4, y=5)  # `y` must be specified by name
```
```
x   is:  1
seq is:  (2, 3, 4)
y   is:  5
```
```python
>>> f("cat", y="dog")  # no additional positional arguments are passed
```
```
x   is:  "cat"
seq is:  ()
y   is:  "dog"
```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Arbitrary Arguments**

Write a function named `mean`, which accepts and arbitrary number of numerical arguments, and computes the mean of all of the values passed to the function. Thus `mean(1, 2, 3)` should return $\frac{1 + 2 + 3}{3} = 2.0$ 

This function should return `0.` if no arguments are passed to it. Be sure to test your function, and include a docstring.

</div>

<!-- #region -->
We see that `*` indicates the *packing of an arbitrary number of arguments into a tuple*, when used in the signature of a function definition. Simultaneously, `*` signals the *unpacking of an iterable* to pass each of its members as a positional argument to a function, when used in the context of calling a function:

```python
# Using `*` when calling a function, to unpack an 
# iterable. Passing its members as distinct arguments 
# to the function

def f(x, y, z):
    return x + y + z

>>> f(1, 2, 3)
6

# `*` means: unpack the contents of [1, 2, 3]
# passing each item as x, y, and z,
# respectively
>>> f(*[1, 2, 3])  # equivalent to: f(1, 2, 3)
6
```
<!-- #endregion -->

In the following example, we use `*` to: 

   1. Define a function to accept an arbitrary
      number of arguments, which get packed into a tuple.
   2. Call the function, passing it  an arbitrary 
      number of arguments, by unpacking an iterable.

<!-- #region -->
```python
def number_of_args(*args):
    return len(args)
```
```python
>>> number_of_args(None, None, None, None)
4

>>> some_list = [1, 2, 3, 4, 5]

# passing the list itself as the sole argument
>>> number_of_args(some_list)
1

# unpacking the 5 members of the list, 
# passing each one as an argument to the function
>>> number_of_args(*some_list)
5
```
<!-- #endregion -->

<!-- #region -->
### Accommodating an Arbitrary Number of Keyword Arguments
We can also define a function that is able to accept an arbitrary number of *keyword* arguments, using the syntax: `def f(**<var_name>)` 

Note that a single asterisk, `*`, was used to denote an arbitrary number of *positional* arguments, whereas `**` signals the acceptance of an arbitrary number of *keyword* arguments. 

```python
# The ** symbol indicates that an arbitrary number of
# keyword arguments can be passed to `args`, when calling `f`.
def f(**args):
    #  All keyword arguments passed to `f` will be "packed" into a 
    #  dictionary that is assigned to the variable `args`.
    # `f()`  will assign `args = {}` (an empty dictionary)
    # `f(x=1, y=2, ...)` will assign `args = {"x":1, "y":2, ...}`
    return args
```

Because Python cannot foresee how many arguments will be passed to `f`, all of the keyword arguments that are passed to it will be packed into a *dictionary*, where a given keyword is set as a key (cast as a string) that maps to the corresponding value. This dictionary is then assigned to the variable `args`. Dictionaries will be discussed in detail in a [later section](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_II_Dictionaries.html).

```python
>>> f()            # pass zero arguments to `f`
{}

>>> f(x=1)           # pass one argument to `f`
{'x': 1}

>>> f(x=(0, 1), val=True, moo="cow")  # pass three arguments to `f`
{'moo': 'cow', 'val': True, 'x': (0, 1)}
```

This syntax can be combined with positional arguments and default arguments. No additional arguments may come after a `**` entry in a function-definition signature:
```python
def f(x, y=2, **kwargs):
    print("x is: ", x)
    print("y is: ", y)
    print("kwargs is: ", kwargs)
    return None
```
```python
# passing arbitrary keyword arguments to `f`
>>> f(1, y=9, z=3, k="hi")
```
```
x is:  1
y is:  9
kwargs is:  {'z': 3, 'k': 'hi'}
```
```python
# no additional keyword arguments are passed
>>> f("cat", y="dog")  
```
```
x is:  cat
y is:  dog
kwargs is:  {}
```

The following function accepts an arbitrary number of positional arguments *and* an arbitrary number of keyword arguments:

```python
# accepting arbitrary positional and keyword arguments
def f(*x, **y):
    # all positional arguments get packed into the tuple `x`
    # all keyword arguments get packed into the dictionary `y` 
    print(x)  
    print(y)
    return None

>>> f(1, 2, 3, hi=-1, bye=-2, sigh=-3)
```
```
(1, 2, 3)
{'hi': -1, 'bye': -2, 'sigh': -3}
```
<!-- #endregion -->

<!-- #region -->
We see that `**` indicates the *packing of an arbitrary number of keyword arguments into a dictionary*, when used in the signature of a function definition. Simultaneously, `**` signals the *unpacking of a dictionary* to pass each of its key-value pairs as a keyword argument to a function, when used in the context of calling a function:

```python
# Using `**` when calling a function, to unpack a 
# dictionary, passing its members as keyword arguments 
# to the function
def f(x, y, z):
    return 0*x + 1*y + 2*z

>>> f(z=10, x=9, y=1)
21

>>> args = {"x": 9, "y": 1, "z": 10}
>>> f(**args)  # equivalent to: f(x=9, y=1, z=10)
21
```
<!-- #endregion -->

In the following example, we use `**` to: 

   1. Define a function to accept an arbitrary
      number of keyword arguments, which get packed into a dictionary.
   2. Call the function, passing it  an arbitrary 
      number of keyword arguments, by unpacking a dictionary.

<!-- #region -->
```python
def print_kwargs(**args):
    print(args)
```
```python
>>> print_kwargs(a=1, b=2, c=3, d=4)
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

>>> some_dict = {"hi":1, "bye":2}

# unpacking the key-value pairs of the dictionary
# as keyword arguments and values, to the function
>>> print_kwargs(a=2, umbrella=True, **some_dict)
{'a': 2, 'umbrella': True, 'hi': 1, 'bye': 2}
```
<!-- #endregion -->

<!-- #region -->
## Functions are Objects
Once defined, a function behaves like any other Python object, like a list or string or integer. You can assign a variable to a function-object:
```python
>>> var = count_vowels  # `var` now references the function `count_vowels`
>>> var("Hello")        # you can now "call" `var`
2
```

You can store functions in a list:
```python
my_list = [count_vowels, print]

for func in my_list:
    func("hello")
    
# iteration 0: calls `count_vowels("hello")` 
# iteration 1: calls `print("hello")`
```

You can also call functions anywhere, and their return-value will be returned in-place:
```python
if count_vowels("pillow") > 1:
    print("that's a lot of vowels!")
```

And, of course, this works within comprehension expressions as well:
```python
>>> sum(count_vowels(word, include_y=True) for word in ["hi", "bye", "guy", "sigh"])
6
```

"Printing" a function isn't very revealing. It simply tells you the memory address where the function-object is stored:
```python
>>> print(count_vowels)
<function count_vowels at 0x000002A32898C6A8>
```
<!-- #endregion -->

## Links to Official Documentation

- [Definition of 'function'](https://docs.python.org/3/library/stdtypes.html#functions)
- [Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Default argument values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)
- [Keyword arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
- [Specifying arbitrary arguments](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
- [Unpacking arguments](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)
- [Documentation strings](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)
- [Function annotations](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)

<!-- #region -->
## Reading Comprehension Exercise Solutions:

**Writing a Basic Function: Solution**

```python
def count_even(numbers):
    """ Counts the number of even integers in an iterable"""
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += 1
    return total
```
or, using a generator comprehension:

```python
def count_even(numbers):
    """ Counts the number of even integers in an iterable"""
    return sum(1 for num in numbers if num % 2 == 0)
```

**Functions and Arguments: Solution**

```python
def max_or_min(x, y, mode="max"):
    """ Return either `max(x,y)` or `min(x,y)`,
        according to the `mode` argument.
        
        Parameters
        ----------
        x : Number
   
        y : Number
   
        mode : str
           Either 'max' or 'min'
        
        Returns
        -------
        The max or min of the two values. `None` is
        returned if an invalid mode was specified."""
    if mode == "max":
        return max(x, y)
    elif mode == "min":
        return min(x, y)
    else:
        return None
```

Note that you can actually have your function raise an "exception" (an error) in the case that `mode` wasn't passed a proper value. In fact, that is likely the more appropriate behavior for this function. 

Such a solution would look like:
```python
def max_or_min(x, y, mode="max"):
    if mode == "max":
        return max(x, y)
    elif mode == "min":
        return min(x, y)
    else:
        raise Exception("`mode` was passed an invalid value: {}".format(mode))
```

**Arbitrary Arguments: Solution**

```python
def mean(*seq):
    """ Returns the mean of the function's arguments """
    if len(seq) == 0:
        return 0
    
    total = 0 
    for num in seq:
        total += num
    return total / len(seq)
```

or, being a bit more fancy :

- using the fact that `bool(seq)` is `False` if `seq` is empty
- using the inline if-else syntax

```python
def mean(*seq):
    """ Returns the mean of the function's arguments """
    return sum(seq) / len(seq) if seq else 0
```
<!-- #endregion -->
