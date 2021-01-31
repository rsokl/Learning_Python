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
   :description: Topic: variable score and namespaces in python, Difficulty: Medium, Category: Section
   :keywords: variable, namespace, function, scope, shadowing
<!-- #endraw -->

# Scope

<!-- #region -->
A valuable aspect of the "encapsulation" provided by functions is that the function's input argument variables, and any variables defined within the function, cannot be "seen" nor accessed outside of the function. That is, these variables are said to have a restricted **scope**.

<div class="alert alert-info">

**Definition**: 

The **scope** of a variable refers to the context in which that variable is visible/accessible to the Python interpreter.
</div>

Until our work with comprehension-statements and functions, we had only encountered variables that have **file scope**. This means that a variable, once defined, is visible to all parts of the code contained in the same file. Variables with file scope can even be accessed *within functions*. By contrast, the variables defined within a function or as input arguments to a function have a **restricted scope** - they can only be accessed within the context of the function:

```python
x = 3  # `x` has file scope. It can be even be accessed
       # within a function, even if it isn't passed to
       # the function as an argument

# `my_func` has file scope (after it is defined)
def my_func(y): 
    func_var = 9 + x  # `x` will have the value 3
    # the scope of `y` and `func_var` is restricted to this function
    return y

# `func_var` and `y` do not exist here
print(func_var)  # raises NameError: name `func_var` not defined
print(y)         # raises NameError: name `y` not defined
```

Python's scoping rules are quite liberal compared to those of other languages, like C++. In most situations, Python will give variables file scope. Let's briefly survey the various contexts in which variables are defined, along with their corresponding scoping rules. Assume that the following code represents the entire contents of the Python script "example_scope.py":
```python
# this demonstrates scope of variables in different contexts
# nothing meaningful is computed in this file

from itertools import combinations  # `combinations` has file scope
 
# `my_func` has file scope
# `in_arg1` has restricted scope
# `in_arg2` has restricted scope
# `func_block` has restricted scope
def my_func(in_arg1, in_arg2="cat"):
    func_block = 1
    return None 

# `file_var` has file scope
# `comp_var` has restricted scope
file_var = [comp_var**2 for comp_var in [-1, -2]]

# `if_block` has file scope
if True:
    if_block = 2
else:
    if_block = 3

# `it_var` has file scope
# `for_block` has file scope
for it_var in [1, 2, 3]:
    for_block = 1

# `while_block` has file scope
while True:
    while_block = None
    break
```

In the preceding code, the following variables have *file scope*:

- `combinations`
- `my_func`
- `file_var`
- `if_block`
- `it_var`
- `for_block`
- `while_block`

whereas the following variables have *restricted scope*:

- `in_arg1`
- `in_arg2`
- `func_block`
- `comp_var`
<!-- #endregion -->

In C++, the variables `if_block`, `it_var`, `for_block`, and `while_block` all would have had restricted scopes - these variables would not be defined outside of their respective if/for/while blocks.

<div class="alert alert-info">

**Takeaway**: 

Variables defined within a function have a *restricted scope* such that they do not exist outside of that function. Most other contexts for defining variables in Python produce variables with *file scope* (i.e. they can be accessed anywhere in the file's code, subsequent to their definition). 
</div>

<!-- #region -->
## Variable Shadowing
What happens when a file-scope variable and a function-scope variable share the same name? This type of circumstance is known as **variable shadowing**. Python resolves this by giving precedence to the variable *with the most restricted scope*, when inside that scope:

```python
x = 2
y = 3

def func(x):
    # input-arg `x` overrides file-scope version of `x` 
    y = 5  # overrides file-scope version of `y`
    return x + y

# `x` is 2 here, once again
# `y` is 3 here, once again

print(func(-5))  # prints 0
print(x, y)      # prints 2  3
```

and similarly,

```python
it = "cow"

def func():
    it = "dog" # overrides file-scope version of `it`
    my_list = [it**2 for it in [1, 2, 3]]  # within the list comprehension, the func-scope `it` is overridden
    # `it` is "dog" here, once again
    return None

# `it` is "cow" here, once again
```
<!-- #endregion -->

## Links to Official Documentation

- [Scopes and namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Python's execution model](https://docs.python.org/3/reference/executionmodel.html)
