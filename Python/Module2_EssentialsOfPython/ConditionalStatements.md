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
   :description: Topic: Conditional Statements, Difficulty: Easy, Category: Section
   :keywords: if, else, elif, inline if, switch statement, comparison operator, bool, truth, is operator
<!-- #endraw -->


# Conditional Statements

<div class="alert alert-warning">

**Note**: 

There are reading-comprehension exercises included throughout the text. These are meant to help you put your reading to practice. Solutions for the exercises are included at the bottom of this page.
</div>

<!-- #region -->
In this section, we will be introduced to the `if`, `else`, and `elif` statements. These allow you to specify that blocks of code are to be executed only if specified conditions are found to be true, or perhaps alternative code if the condition is found to be false. For example, the following code will square `x` if it is a negative number, and will cube `x` if it is a positive number:
```python
# a simple if-else block
if x < 0:
    x = x ** 2
else:
    x = x ** 3
```

Please refer to the "Basic Python Object Types" subsection to recall the basics of the "boolean" type, which represents True and False values. We will extend that discussion by introducing comparison operations and membership-checking, and then expanding on the utility of the built-in `bool` type. 
<!-- #endregion -->

<!-- #region -->
## Comparison Operations
Comparison statements will evaluate explicitly to either of the boolean-objects: `True` or `False`. There are eight comparison operations in Python:

| Operation | Meaning                 |
| --------- | ----------------------- |
| `<`       | strictly less than      |
| `<=`      | less than or equal      |
| `>`       | strictly greater than   |
| `>=`      | greater than or equal   |
| `==`      | equal                   |
| `!=`      | not equal               |
| `is`      | object identity         |
| `is not`  | negated object identity |

The first six of these operators are familiar from mathematics:

```python
>>> 2 < 3
True
```

Note that `=` and `==` have very different meanings. The former is the assignment operator, and the latter is the equality operator:

```python
>>> x = 3   # assign the value 3 to the variable `x`
>>> x == 3  # check if `x` and 3 have the same value
True
```

Python allows you to chain comparison operators to create "compound" comparisons:

```python
>>> 2 < 3 < 1  # performs (2 < 3) and (3 < 1)
False
```

Whereas `==` checks to see if two objects have the same value, the `is` operator checks to see if two objects are actually the *same* object. For example, creating two lists with the same contents produces two *distinct* lists, that have the same "value":

```python
# demonstrating `==` vs `is`
>>> x = [1, 2, 3]
>>> y = [1, 2, 3]

>>> x == y
True

# `x` and `y` reference equivalent, but distinct lists
>>> x is y
False
```

Thus the `is` operator is most commonly used to check if a variable references the `None` object, or either of the boolean objects:
```python
>>> x = None
>>> x is None
True

# (2 < 0) returns the object `False`
# thus this becomes: `False is False`
>>> (2 < 0) is False
True
```

Use `is not` to check if two objects are distinct:
```python
>>> 1 is not None
True
```
<!-- #endregion -->

<!-- #region -->
## `bool` and Truth Values of Non-Boolean Objects
Recall that the two boolean objects `True` and `False` formally belong to the `int` type in addition to `bool`,  and are associated with the values `1` and `0`, respectively:

```python
>>> isinstance(True, int)
True

>>> int(True)
1

>>> isinstance(False, int)
True

>>> int(False)
0

>>> 3*True - False
3

>>> True / False
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-4-f8487d9d0863> in <module>()
----> 1 True / False

ZeroDivisionError: division by zero
```

Likewise Python ascribes boolean values to non-boolean objects. For example,the number 0 is associated with `False` and non-zero numbers are associated with `True`. The boolean values of built-in objects can be evaluated with the built-in Python command `bool`:

```python
# Using `bool` to access the True/False
# value of non-boolean objects
>>> bool(0)
False
```

and non-zero Python integers are associated with `True`:

```python
# nonzero values evaluate to `True`
>>> bool(2)
True
```
The following built-in Python objects evaluate to `False` via `bool`:

- `False`
- `None`
- Zero of any numeric type: `0`, `0.0`, `0j`
- Any empty sequence, such as an empty string or list: `''`, `tuple()`, `[]`, `numpy.array([])`
- Empty dictionaries and sets

Thus non-zero numbers and non-empty sequences/collections evaluate to `True` via `bool`.

<div class="alert alert-info">

**Takeaway**: 

The `bool` function allows you to evaluate the boolean values ascribed to various non-boolean objects. For instance, `bool([])` returns `False` wherease `bool([1, 2])` returns `True`.
</div>
<!-- #endregion -->

<!-- #region -->
## `if`, `else`, and `elif`
We now introduce the simple, but powerful `if`, `else`, and `elif` conditional statements. This will allow us to create simple branches in our code. For instance, suppose you are writing code for a video game, and you want to update a character's status based on her/his number of health-points (an integer). The following code is representative of this:

```python
if num_health > 80:
    status = "good"
elif num_health > 50:
    status = "okay"
elif num_health > 0:
    status = "danger"
else:
    status = "dead"
```

Each `if`, `elif`, and `else` statement must end in a colon character, and the body of each of these statements is [delimited by whitespace](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Introduction.html#Python-Uses-Whitespace-to-Delimit-Scope).

The following pseudo-code demonstrates the general template for conditional statements:

```
if <expression_1>:
    the code within this indented block is executed if..
    - bool(<expression_1>) is True
elif <expression_2>:
    the code within this indented block is executed if..
     - bool(<expression_1>) was False 
     - bool(<expression_2>) is True
...
...
elif <expression_n>:
    the code within this indented block is executed if..
      - bool(<expression_1>) was False
      - bool(<expression_2>) was False
      ...
      ...
      - bool(<expression_n-1>) was False
      - bool(<expression_n>) is True
else:
    the code within this indented block is executed only if 
    all preceding expressions were False

```

In practice this can look like:

```python
x = [1, 2]

if 3 < len(x):
    # bool(3 < 2) returns False, this code 
    # block is skipped
    print("`x` has more than three items in it")
elif len(x) == 2:
    # bool(len(x) == 2) returns True
    # this code block is executed
    print("`x` has two items in it")
elif len(x) == 1:
    # this statement is never reached
    print("`x` has one items in it")
else:
    # this statement is never reached
    print("`x` is an empty list")

"`x` has two items in it"
```

In its simplest form, a conditional statement requires only an `if` clause. `else` and `elif` clauses can only follow an `if` clause.

```python
# A conditional statement consisting of 
# an "if"-clause, only.

x = -1

if x < 0:
    x = x ** 2
# x is now 1
```

Similarly, conditional statements can have an `if` and an `else` without an `elif`:

```python
# A conditional statement consisting of
# an "if"-clause and an "else"
x = 4

if x > 2:
    x = -2
else:
    x = x + 1
# x is now -2
```

Conditional statements can also have an `if` and an `elif` without an `else`:

```python
# A conditional statement consisting of
# an "if"-clause and an "elif"
x = 'abc'

if len(x) < 9:
    x = x * 3
elif len(x) > 40:
    x = 'cba'
# x is now 'abcabcabc'
```

Note that only one code block within a single if-elif-else statement can be executed: either the "if-block" is executed, or an "elif-block" is executed, or the "else-block" is executed. Consecutive if-statements, however, are completely independent of one another, and thus their code blocks can be executed in sequence, if their respective conditional statements resolve to `True`.

```python
# consecutive if-statements are independent
x = 5
y = 0

if x < 10:
    y += 1 

if x < 20:
    y += 1
    
# y is now 2
```
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info">

**Reading Comprehension: Conditional statements**

1\. Assume `my_list` is a list. Given the following code:
```python
first_item = None

if my_list:
    first_item = my_list[0]
```

What will happen if `my_list` is `[]`? Will `IndexError` be raised? What will `first_item` be?

2\. Assume variable `my_file` is a string storing a filename, where a period denotes the end of the filename and the beginning of the file-type. Write code that extracts only the filename.

`my_file` will have at most one period in it. Accommodate cases where `my_file` does *not* include a file-type. 

That is: 

- `"code.py"` $\rightarrow$ `"code"`
- `"doc2.pdf"` $\rightarrow$ `"doc2"`
- `"hello_world"` $\rightarrow$ `"hello_world"` 

</div>
<!-- #endregion -->

<!-- #region -->
### Inline if-else statements
Python supports a syntax for writing a restricted version of if-else statements in a single line. The following code:

```python
num = 2

if num >= 0:
    sign = "positive"
else:
    sign = "negative"
```

can be written in a single line as:

```python
sign = "positive" if num >=0 else "negative"
```

This is suggestive of the general underlying syntax for inline if-else statements:

<div class="alert alert-info">

**The inline if-else statement**: 

The expression `A if <condition> else B` returns `A` if `bool(<condition>)` evaluates to `True`, otherwise this expression will return `B`.
</div>

This syntax is highly restricted compared to the full "if-elif-else" expressions - no "elif" statement is permitted by this inline syntax, nor are multi-line code blocks within the if/else clauses.

Inline if-else statements can be used anywhere, not just on the right side of an assignment statement, and can be quite convenient:
```python
# using inline if-else statements in different scenarios

>>> x = 2

# will store 1 if `x` is non-negative
# will store 0 if `x` is negative
>>> my_list = [1 if x >= 0 else 0]
>>> my_list
[1]

>>> "a" if x == 1 else "b"
'b'
```
We will see this syntax shine when we learn about comprehension statements. That being said, this syntax should be used judiciously. For example, inline if-else statements ought not be used in arithmetic expressions, for therein lies madness:

```python
# don't ever do this...ever!
2 - 3 if x < 1 else 1 + 6*2 if x >= 0 else 9
```
<!-- #endregion -->

<!-- #region -->
## Short-Circuiting Logical Expressions
Armed with our newfound understanding of conditional statements, we briefly return to our discussion of Python's logic expressions to discuss "short-circuiting". In Python, a logical expression is evaluated from left to right and will return its boolean value as soon as it is unambiguously determined, *leaving any remaining portions of the expression unevaluated*. That is, the expression may be *short-circuited*. 

For example, consider the fact that an `and` operation will only return `True` if both of its arguments evaluate to `True`. Thus the expression `False and <anything>` is guaranteed to return `False`; furthermore, when executed, this expression will return `False` *without having evaluated* `bool(<anything>)`.

To demonstrate this behavior, consider the following example:

```python
# demonstrating short-circuited logic expressions   
>>> False and 1/0  # evaluating `1/0` would raise an error 
False
```
According to our discussion, the pattern `False and` short-circuits this expression without it ever evaluating `bool(1/0)`. Reversing the ordering of the arguments makes this clear.

```python
# expressions are evaluated from left to right
>>> 1/0 and False
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-1-3471672109ee> in <module>()
----> 1 1/0 and False

ZeroDivisionError: division by zero
```

In practice, short-circuiting can be leveraged in order to condense one's code. Suppose a section of our code is processing a variable `x`, which may be either a [number](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Number-Types) or a [string](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Strings). Suppose further that we want to process `x` in a special way if it is an all-uppercased string. The code

```python
# this will raise an error if `x` is not a string
if x.isupper():
    # do something with the uppercased string
```
is problematic because `isupper` can only be called once we are sure that `x` is a string; this code will raise an error if `x` is a number. We could instead write

```python
# a valid but messy way to filter out non-string objects
if isinstance(x, str):
    if x.isupper():
        # do something with the uppercased string
```

but the more elegant and concise way of handling the nestled checking is to leverage our ability to short-circuit logic expressions.

```python
# utilizing short-circuiting to concisely perform all necessary checks
if isinstance(x, str) and x.isupper():
    # do something with the uppercased string
```

See, that if `x` is not a string, that `isinstance(x, str)` will return `False`; thus `isinstance(x, str) and x.isupper()` will short-circuit and return `False` without ever evaluating `bool(x.isupper())`. This is the preferable way to handle this sort of checking. This code is more concise and readable than the equivalent nested if-statements.
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info">

**Reading Comprehension: short-circuited expressions**

Consider the preceding example of short-circuiting, where we want to catch the case where `x` is an uppercased string. What is the "bug" in the following code? Why does this fail to utilize short-circuiting correctly? 

```python
# what is wrong with me?
if x.isupper() and isinstance(x, str):
    # do something with the uppercased string
```

</div>
<!-- #endregion -->

## Links to Official Documentation

- [bool](https://docs.python.org/3/library/functions.html#bool)
- [Truth testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)
- ['if' statements](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)


## Reading Comprehension Exercise Solutions:

<!-- #region -->
**Conditional statements**

1\. If `my_list` is `[]`, then `bool(my_list)` will return `False`, and the code block will be skipped. Thus `first_item` will be `None`.

2\. First, check to see if `.` is even contained in `my_file`. If it is, find its index-position, and slice the string up to that index. Otherwise, `my_file` is already the file name.
```python

my_file = "code.pdf"

if "." in my_file:
    dot_index = my_file.index(".")
    filename = my_file[:dot_index]
else:
    filename = my_file
```
<!-- #endregion -->

<!-- #region -->
**Short-circuited expressions**

The code
```python
# what is wrong with me?
if x.isupper() and isinstance(x, str):
    # do something with the uppercased string
```

fails to account for the fact that expressions are always evaluated from left to right. That is, `bool(x.isupper())` will always be evaluated first in this instance and will raise an error if `x` is not a string. Thus the following `isinstance(x, str)` statement is useless.
<!-- #endregion -->
