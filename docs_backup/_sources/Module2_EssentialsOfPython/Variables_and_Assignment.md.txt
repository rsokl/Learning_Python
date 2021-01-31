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
   :description: Topic: variable naming and assignment, Difficulty: Medium, Category: Section
   :keywords: variable naming, valid names, mutable, immutable, reference, pointer
<!-- #endraw -->

# Variables & Assignment

<div class="alert alert-warning">

**Note**: 

There are reading-comprehension exercises included throughout the text. These are meant to help you put your reading to practice. Solutions for the exercises are included at the bottom of this page.
</div>

<!-- #region -->
Variables permit us to write code that is flexible and amendable to repurpose. Suppose we want to write code that logs a student's grade on an exam. The logic behind this process should not depend on whether we are logging Brian's score of 92% versus Ashley's score of 94%. As such, we can utilize variables, say `name` and `grade`, to serve as placeholders for this information. In this subsection, we will demonstrate how to define variables in Python.

In Python, the `=` symbol represents the "assignment" operator. The variable goes to the left of `=`, and the object that is being assigned to the variable goes to the right:
```python
name = "Brian"  # the variable `name` is being assigned the string "Brian"
grade = 92      # the variable `grade` is being assigned the integer 92
```
Attempting to reverse the assignment order (e.g. `92 = name`) will result in a syntax error.  When a variable is assigned an object (like a number or a string), it is common to say that the variable **is a reference to** that object. For example, the variable `name` references the string `"Brian"`. This means that, once a variable is assigned an object, it can be used elsewhere in your code as a reference to (or placeholder for) that object:
```python
# demonstrating the use of variables in code
name = "Brian"
grade = 92
failing = False

if grade < 60:
    failing = True

# writes: name | grade | passing-status
# to the end of the file "student_grades.txt"
with open("student_grades.txt", mode="a") as opened_file:
    opened_file.write("{} | {} | {}".format(name, grade, failing))
```

## Valid Names for Variables
A variable name may consist of alphanumeric characters (`a-z`, `A-Z`, `0-9`) and the underscore symbol (`_`); a valid name cannot begin with a numerical value.

- `var`: valid
- `_var2`: valid
- `ApplePie_Yum_Yum`: valid
- `2cool`: **invalid** (begins with a numerical character)
- `I.am.the.best`: **invalid** (contains `.`)

They also cannot conflict with character sequences that are reserved by the Python language. As such, the following cannot be used as variable names:

- `for`, `while`, `break`, `pass`, `continue`
- `in`, `is`, `not`
- `if`, `else`, `elif`
- `def`, `class`, `return`, `yield`, `raises`
- `import`, `from`, `as`, `with`
- `try`, `except`, `finally`

There are other unicode characters that are permitted as valid characters in a Python variable name, but it is not worthwhile to delve into those details here.
<!-- #endregion -->

<!-- #region -->
## Mutable and Immutable Objects
The **mutability** of an object refers to its ability to have its state changed. A **mutable object** can have its state changed, whereas an **immutable object** cannot. For instance, a list is an example of a mutable object. Once formed, we are able to update the contents of a list - replacing, adding to, and removing its elements.

```python
# demonstrating the mutability of a list
>>> x = [1, 2, 3]
>>> x[0] = -4  # replace element-0 of `x` with -4
>>> x
[-4, 2, 3]
```

To spell out what is transpiring here, we:

1. Create (initialize) a list with the state `[1, 2, 3]`.
2. Assign this list to the variable `x`; `x` is now a reference to that list.
3. Using our referencing variable, `x`, update element-0 of the list to store the integer `-4`. 

This does not create a new list object, rather it *mutates* our original list. This is why printing `x` in the console displays `[-4, 2, 3]` and not `[1, 2, 3]`.

A tuple is an example of an immutable object. Once formed, there is no mechanism by which one can change of the state of a tuple; and any code that appears to be updating a tuple is in fact creating an entirely new tuple.

```python
# demonstrating to the immutability of a tuple
>>> x = (1, 2, 3)
>>> x[0] = -4  # attempt to replace element-0 of `x` with -4
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-a858573fdc63> in <module>()
      1 x = (1, 2, 3)
----> 2 x[0] = -4  # attempt to replace element-0 of `x` with -4

TypeError: 'tuple' object does not support item assignment
```

### Mutable & Immutable Types of Objects
The following are some common immutable and mutable objects in Python. These will be important to have in mind as we start to work with dictionaries and sets. 
<!-- #endregion -->

**Some immutable objects**

 - [numbers](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Number-Types) (integers, floating-point numbers, complex numbers)
 - [strings](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Strings)
 - [tuples](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/SequenceTypes.html#Tuples) 
 - [booleans](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#The-Boolean-Type)
 - ["frozen"-sets](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_III_Sets_and_More.html#The-%E2%80%9CSet%E2%80%9D-Data-Structure)

**Some mutable objects**

 - [lists](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Lists)
 - [dictionaries](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_II_Dictionaries.html)
 - [sets](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_III_Sets_and_More.html#The-%E2%80%9CSet%E2%80%9D-Data-Structure)
 - [NumPy arrays](https://www.pythonlikeyoumeanit.com/module_3.html)

<!-- #region -->
## Referencing a Mutable Object with Multiple Variables
It is possible to assign variables to other, existing variables. Doing so will cause the variables to reference the same object:
```python
# demonstrating the behavior of variables 
# referencing the same object
>>> list1 = [1, 2, 3]  #  `list1` references [1, 2, 3]
>>> list2 = list1      #  `list2` and `list1` now both reference [1, 2, 3]

>>> print(list1)
[1, 2, 3]

>>> print(list2)
[1, 2, 3]
```

What this entails is that these common variables will reference the *same instance* of the list. Meaning that if the list changes, all of the variables referencing that list will reflect this change:

```python
>>> list1.append(4)  # append 4 to the end of [1, 2, 3]
>>> print(list1)
[1, 2, 3, 4]
```

We can see that `list2` is still assigned to reference the *same, updated* list as `list1`:
```python
>>> print(list2)
[1, 2, 3, 4]
```
In general, assigning a variable `b` to a variable `a` will cause the variables to reference the *same* object in the system's memory, and assigning `c` to `a` or `b` will simply have a third variable reference this same object. Then any change (a.k.a *mutation*)  of the object will be reflected in all of the variables that reference it (`a`, `b`, and `c`).

Of course, assigning two variables to identical but *distinct* lists means that a change to one list will not affect the other:

```python
>>> list1 = [1, 2, 3]  #  `list1` references [1, 2, 3]
>>> list2 = [1, 2, 3]  #  `list2` references a *separate* list, whose value is [1, 2, 3]

>>> list1.append(4)  # append 4 to the end of [1, 2, 3]
>>> print(list1)
[1, 2, 3, 4]

>>> print(list2)     # `list2` still references its own list
[1, 2, 3]
``` 
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Does slicing a list produce a reference to that list?**

Suppose `x` is assigned a list, and that `y` is assigned a "slice" of `x`. Do `x` and `y` reference the same list? That is, if you update part of the subsequence common to `x` and `y`, does that change show up in both of them? Write some simple code to investigate this. 

</div>

<!-- #region -->
<div class="alert alert-info">

**Reading Comprehension: Understanding References**

Based on our discussion of mutable and immutable objects, predict what the value of `y` will be in the following circumstance:

```python
>>> x = 3
>>> y = x

# shorthand for: `x = x * 3`
>>> x *= 3
>>> x
9

>>> y
???
```

</div>
<!-- #endregion -->

<!-- #region -->
## Reading Comprehension Exercise Solutions:

**Does slicing a list produce a reference to that list?: Solution**

Based on the following behavior, we can conclude that slicing a list does **not** produce a reference to the original list. Rather, slicing a list produces a copy of the appropriate subsequence of the list:
```python
>>> x = [0, 1, 2, 3]

>>> y = x[:2] 
>>> y      # does `y` reference the same list as `x`?
[0, 1]

>>> x[0] = -1  # update one of the entries of the list that `x` references
>>> x
[-1, 1, 2, 3]

>>> y      # the list that `y` references was unaffected by the update
[0, 1]
```
<!-- #endregion -->

**Understanding References: Solutions**

Integers are immutable, thus `x` must reference an entirely new object (`9`), and `y` still references `3`.
