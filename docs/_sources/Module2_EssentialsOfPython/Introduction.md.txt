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
   :description: Topic: introduction to control flow, Difficulty: Easy, Category: Section
   :keywords: overview, summary, if, else, function, for-loop, if, else, control flow
<!-- #endraw -->

<!-- #region -->
# Introducing Control Flow
Very simply put, to "control flow" in your code is to affect the order in which the 
code in your program is executed. Up until this point in the course, you have seen (and hopefully written) code that 
executes linearly; for example:

```python
# simple code without any "control flow"
# i.e. no branches in logic, loops, or
# code encapsulation
x = 6
y = 23
print("x + y = ", x + y)
print("x - y = ", x - y)
```

But what if you want your code to do something different when `x` is an even number? What if you want to do an additional computation for every number that falls between `x` and `y`? By the end of this module, you should understand how to write programs that can accommodate these, and many other, branches in logic.

Control flow tools will vastly expand your ability to write useful code. They are the quintessential building blocks for modern programming languages, and are effectively the same across Python, C, C++, Java, and many others (barring syntactic differences).

As a sneak peek, let's write a function that counts how many numbers between m and n are divisible by 3

```python
def cnt_div_by_3(m, n):
    """ Counts how many numbers in the interval [m, n] are divisible by 3. """
    count = 0
    for num in range(m, n + 1):
        if num % 3 == 0:  # recall: x % y  gives the remainder of x / y 
            count += 1
        else:
            pass # this `else-pass` statement is not really necessary 
                 # it is included for the sake of clarity in this introduction 
    return count
```
(note: there are much more efficient ways of computing this - can you think of any?)

This code contains several critical "control flow" features:

- The `def cnt_div_by_3(m, n):` statement signals the definition of a function: a modular block of code, which can be utilized elsewhere in your code.
- The line `for num in range(m, n + 1):` signifies a "for-loop" which instructs the code to iterate over a sequence of numbers, executing a common block of code for each iteration.
- `if num % 3 == 0:` and `else` instruct pieces of codes to be executed conditionally - only if a specified condition is met.

In the following sections, you will be formally introduced to if-elif-else blocks, for-loops & iterables, and functions, all so that you can implement effective "control flow" in your code.

Before embarking on these sections, we must take a moment to study Python's syntax for delimiting scope for these various control flow constructs.

## Python Uses Whitespace to Delimit Scope

While the concepts of function definitions, loops, and conditional statements are shared across the majority of modern programming languages, the languages often differ in their syntax for delimiting the *bodies* of these constructs. For example, where C++ uses "curly braces" as delimiters, e.g.:

```cpp
// example showing that C++ uses curly braces to delimit scope
int x = 1;

if (x > 10)
    {
    // we are inside the if-block, as delimited by the curly-brackets
    x = x + 1;
    }
// we are outside of the if-block
x = x + 3;
```

Python **uses whitespace (i.e. indentation) to delimit scope**:

```python
# example showing that Python uses whitespace to delimit scope
x = 1

if x > 10:
    # we are inside the if-block; this line starts with four blank spaces
    x = x + 1
# we are outside of the if-block; there are no leading whitespace characters
x = x + 3
```

Look to the example at the beginning of this section to see the bodies of the function definition, the for-loop, and the subsequent if-else block were all separated by increasing levels of indentation.

Python's syntax is quite flexible in terms of what it defines as a whitespace delimiter. Its rules are that:

- One or more whitespace characters (spaces or tabs) is sufficient to serve as indentation.
- A given indented block must use a uniform level of indentation. E.g. if the first line of an indented block has two leading spaces, all subsequent lines in that block must lead with exactly two white spaces.

While Python's syntax is relatively forgiving, I am not: the [standard style](https://www.python.org/dev/peps/pep-0008/#indentation) for indenting in Python is to **use four space characters** for each level of indentation. It is strongly advised that you adhere to this standard. Most IDEs and consoles (including Jupyter notebooks) will automatically add a four-space indentation for you when you enter into the body of one of the aforementioned constructs.

Let's review these ruled by considering a few simple examples (including incorrect examples) of delimiting scope in Python.

```python
# OK, but gross: The use of a single whitespace 
# makes the indentation hard to see. Use four spaces.
if True:
 x = 1  # one space
 y = 2  # one space
```
<!-- #endregion -->

<!-- #region -->
```python
# BAD: the inconsistent level of indentation in this
# single block will cause this code to raise an IndentationError
def my_func(x):
    x = x + 1  # four spaces
       y = 3   # eight spaces
    z = x + y  # four spaces
    return z   # four spaces
```

```python
# OK, but gross: The if-block uses four spaces as a delimiter.
# The else-block uses two spaces as a delimiter. This is technically 
# okay since indentation is consistent within each block. One should 
# always use four spaces for indentation.
if True:
    x = 3  # four spaces
    y = 2  # four spaces
else:
  x = 2  # two spaces
  y = 1  # two spaces
```

```python
# Good! The for-loop's body is defined by one level
# of four-space indentation, and the contained if-else
# blocks each have their own additional four-space indentations.
for i in [1, 2, 3, 4]:
    if i == 2 or i == 4:  # four spaces
        x = "even"        # eight spaces
    else:                 # four spaces
        x = "odd"         # eight spaces
```
<!-- #endregion -->
