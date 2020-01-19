---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.0rc1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #raw raw_mimetype="text/restructuredtext" -->
.. meta::
   :description: Topic: Basics of Python Objects, Difficulty: Easy, Category: Section
   :keywords: exceptions, errors, bugs, debug, fix
<!-- #endraw -->

<!-- #region -->
# Errors

Unfortunately, not all code is perfect. As you write more complicated programs, you will doubtless run into some errors that you will need to figure out how to fix. Although debugging skills will come with practice, it can be helpful to understand errors, what causes them, and how to fix them. The different types of errors can be broken down into three categories: syntax errors, exceptions, and logic errors.


<!-- #endregion -->

<!-- #region -->
## Syntax Errors

Syntax errors are by far the easiest errors to debug, and they will be the most common errors while you are learning to program. Syntax errors are raised when the Python interpreter is unable to understand your code due to a typo or some misplaced syntax. When a syntax error occurs, the interpreter will stop running. It will also display the `SyntaxError` code, and will often give a line number or explanation.

Most syntax errors are benign and easily detectable, such as mispelling a name or forgetting a piece of punctuation. Occasionally you will encounter a tricky syntax error where you cannot find your mistake in the line. When this happens, remember to look out for punctuation mistakes, especially in parentheses. Misplaced parentheses can be difficult to detect, but are relatively simple to fix once detected.

Many modern IDEs will automatically detect syntax errors, and will sometimes automatically place punctuation and indentations. As such, syntax errors are becoming more easily avoidable, but it is still important to know how to spot and fix them. 

<!-- #endregion -->

<!-- #region -->
## Exceptions
An exception occurs when a piece of code is valid and understood by the interpreter, but for some reason the interpreter is unable to execute the action. Exceptions can occur when a function is passed an incompatible type of input, when the program is asked to something it cannot, and in many other circumstances. Python has many types of built-in exceptions that can be raised, but here are several that you are likely to encounter and their causes:

| Exception  | Causes |
| ------------- |:-------------:|
| `IndexError` | Attempting to index or slice into a list with an index outside of the list's range |   
| `KeyError` | Attempting to access a dictionary value with a key that is not in the dictionary |   
| `NameError` | Referencing a variable or function that is not yet defined |   
| `TypeError` | Passing an object of an invalid type into a function or operation |   
| `ValueError` | Passing an object of an appropriate type but invalid value to a function or operation |
| `ZeroDivisionError` | Attempting to divide by zero. Can also be raised when a function is passed a value that would force it to divide by zero |

These six exceptions are the most common exceptions you will face, as they cover many possible issues. There exist many more specific exceptions for complicated errors, but they are much rarer and tend to only appear in very specific cases. Let's look at a piece of code that will raise an exception.

```python
# attempting to take the square root of a negative number
>>> from math import sqrt
>>> math.sqrt(-1)
ValueError: math domain error

```

The math library cannot take the square root of a negative number. Because the number passed as an argument is technically the correct type, but is not compatible with the function, a `ValueError` is raised. Whenever you encounter one of these exceptions, be sure that you understand why the encounter is raised before you try to fix it.

It is also possible to raise exceptions on purpose with the `raise` statement. If you are writing a function that is designed only for certain inputs, it can be worthwhile to verify that inputs will be valid. As an example, let's create our own square root function.

```python
def squareRoot(x):
  if x < 0:
    raise ValueError('Cannot take the square root of a negative number.')
  return x**0.5
  
>>> print(squareRoot(-1))
ValueError: Cannot take the square root of a negative number.
```

When the invalid value is passed, our function raises a ValueError rather than allowing the function to run with the value, possibly causing a worse or more confusing error. Clearly, in this case it was much better to raise an exception than to allow the program to continue! The `assert` statement can also be used to raise errors in the format `assert [boolean statement], 'error message'`, but it tends to be less informative and less powerful than simply using `raise`.

It is also possible to create custom exceptions using classes, which will be discussed further in Module 4.
<!-- #endregion -->


<!-- #region -->
## Logic Errors

Logic errors occur when your code will run in the interpreter, but does not behave as expected. Whenever you write a function that works but outputs something incorrect, you have committed a logic error. Logic errors are very easy to commit and can be incredibly difficult to solve. It's impossible to completely avoid logic errors, but if you take care while programming and debugging, they can often be avoided or fixed.

Before writing a complex program, it is often smart to write psuedocode beforehand to ensure that your algorithm makes sense and will do what you want it to. It is important to understand how your program will work before you write it. After writing the program, it can be helpful to take another walk through how the program works, and make sure that every step makes sense. Some programmers keep rubber ducks at their desks and try to explain their code to the duck when they hit a bug. Sometimes, simply walking through your code slowly and describing everything can help you see an error that you otherwise may have missed.

Breaking your code down into functions can help with readability, usability, and debugging, especially as the scale of your project grows. It is much easier to find the error in ten functions, each with fifty lines, than it is to find the error in one block of code that is five hundred lines long. Testing out different parts of your code independently to verify that they work is essential to debugging. 

To find particularly elusive bugs, many IDEs come with debugging software that allows you to step through your program slowly and monitor the internal processes. Debuggers can be overkill for simpler bugs, but they can be invaluable tools when you cannot find a bug on your own.

If all else fails, it's best to simply move on and return to the program after some time has passed. A bug that may seem impossible to fix may become much easier after a good night's sleep or a meal.

<!-- #endregion -->

<!-- #region -->
## Summary

It is inevitable that you will have to deal with errors, so understanding what they are and how to fix them can be invaluable.

- Syntax errors occur when your code cannot be read by the Python interpreter
- Exceptions occur when your code is readable, but cannot be run correctly
- Logic errors occur when your code runs, but does not behave as expected


<!-- #endregion -->

## Link to Official Documentation

- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)