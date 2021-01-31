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
   :description: Topic: the basics of iterables in python, Difficulty: Medium, Category: Section
   :keywords: iterables, max, min, sum, all, any, itertools, enumerate, unpack
<!-- #endraw -->

# Iterables
Our encounter with for-loops introduced the term *iterable* - an object that can be "iterated over", such as in a for-loop.

<div class="alert alert-info">

**Definition**: 

An **iterable** is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop. 
</div>

Familiar examples of iterables include lists, tuples, and strings - any such sequence can be iterated over in a for-loop. We will also encounter important non-sequential collections, like dictionaries and sets; these are iterables as well. It is also possible to have an iterable that "generates" each one of its members upon iteration - meaning that it doesn't ever store all of its members in memory at once. We dedicate an entire section to generators, a special type of iterator, because they are so useful for writing efficient code.

The rest of this section is dedicated to working with iterables in your code.

<div class="alert alert-warning">

**Note**:

"Under the hood", an iterable is any Python object with an `__iter__()` method or with a `__getitem__()` method that implements `Sequence` semantics. These details will become salient if you read through the Object Oriented Programming module.
</div>

<!-- #region -->
## Functions that act on iterables
Here are some useful built-in functions that accept iterables as arguments:

 - `list`, `tuple`, `dict`, `set`: construct a list, tuple, [dictionary](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_II_Dictionaries.html), or [set](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_III_Sets_and_More.html#The-%E2%80%9CSet%E2%80%9D-Data-Structure), respectively, from the contents of an iterable
 - `sum`: sum the contents of an iterable.
 - `sorted`: return a list of the sorted contents of an interable
 - `any`: returns `True` and ends the iteration immediately if `bool(item)` was `True` for *any* item in the iterable.
 - `all`: returns `True` only if `bool(item)` was `True` for *all* items in the iterable.
 - `max`: return the largest value in an iterable.
 - `min`: return the smallest value in an iterable.
 
```python
# Examples of built-in functions that act on iterables
>>> list("I am a cow")
['I', ' ', 'a', 'm', ' ', 'a', ' ', 'c', 'o', 'w']

>>> sum([1, 2, 3])
6

>>> sorted("gheliabciou")
['a', 'b', 'c', 'e', 'g', 'h', 'i', 'i', 'l', 'o', 'u']

# `bool(item)` evaluates to `False` for each of these items
>>> any((0, None, [], 0))
False

# `bool(item)` evaluates to  `True` for each of these items
>>> all([1, (0, 1), True, "hi"])
True

>>> max((5, 8, 9, 0))
9

>>> min("hello")
'e'
```
<!-- #endregion -->

<!-- #region -->
## Tricks for working with iterables
Python provides some syntactic "tricks" for working with iterables: "unpacking" iterables and "enumerating" iterables. Although these may seem like inconsequential niceties at first glance, they deserve our attention because they will help us write clean, readable code. Writing clean, readable code leads to bug-free algorithms that are easy to understand. Furthermore, these tricks will also facilitate the use of other great Python features, like comprehension-statements, which will be introduced in the coming sections.

### "Unpacking" iterables
Suppose that you have three values stored in a list, and that you want to assign each value to a distinct variable. Given the lessons that we have covered thus far, you would likely write the following code:

```python
# simple script for assigning contents of a list to variables
>>> my_list = [7, 9, 11]

>>> x = my_list[0]
>>> y = my_list[1]
>>> z = my_list[2]
```

Python provides an extremely useful functionality, known as **iterable unpacking**, which allows us to write the simple, elegant code:

```python
# assigning contents of a list to variables using iterable unpacking
>>> my_list = [7, 9, 11]

>>> x, y, z = my_list
>>> print(x, y, z)
7 9 11
```

That is, the Python interpreter "sees" the pattern of variables to the left of the assignment, and will "unpack" the iterable (which happens to be a list in this instance). It may not seem like it from this example, but this is an *extremely* useful feature of Python that greatly improves the readability of code! 

Iterable unpacking is particularly useful in the context of performing for-loops over iterables-of-iterables. For example, suppose we have a list containing tuples of name-grade pairs:

```python
>>> grades = [("Ashley", 93), ("Brad", 95), ("Cassie", 84)]
```

Recall from the preceding section that if we loop over this list, that the iterate-variable will be assigned to each of these tuples:

```python
for entry in grades:
    print(entry)
```
will print:
```
('Ashley', 93)
('Brad', 95)
('Cassie', 84)
```

It is likely that we will want to work with the student's name and their grade independently (e.g. use the name to access a log, and add the grade-value to our class statistics); thus we will need to index into `entry` twice to assign its contents to two separate variables. However, because each iteration of the for-loop involves an assignment of the form `entry = ("Ashley", 93)`, we can make use of iterable unpacking! That is, we can replace `entry` with `name, grade` and Python will intuitively do an unpacking upon each assignment of the for-loop.

```python
# The first iteration of this for-loop performs
# the unpacking assignment: name, grade = ("Ashley", 93)
# then the second iteration: name, grade = ("Brad", 95)
# and so-on
for name, grade in grades: 
    print(name)
    print(grade)
    print("\n")
```
prints:
```
Ashley
93

Brad 
95

Cassie 
84
```
This for-loop code is concise and supremely readable. It is highly recommended that you make use of iterable unpacking in such contexts.

Iterable unpacking is not quite as simple as it might seem. What happens if you provide 4 variables to unpack into, but use an iterable containing 10 items? Although what we have covered thus far conveys the most essential use case, it is good to know that [Python provides an even more extensive syntax for unpacking iterables](https://www.python.org/dev/peps/pep-3132/#specification). We will also see that unpacking can be useful when creating and using functions.

<div class="alert alert-info">

**Takeaway**: 

Python provides a sleek syntax for "unpacking" the contents of an iterable - assigning each item to its own variable. This allows us to write intuitive, highly-readable code when performing a for-loop over a collection of iterables. 
</div>
<!-- #endregion -->

<!-- #region -->
### Enumerating iterables
The built-in [enumerate](https://docs.python.org/3/library/functions.html#enumerate) function allows us to iterate over an iterable, while keeping track of the iteration count:

```python
# basic usage of `enumerate`
>>> for entry in enumerate("abcd"):
...    print(entry)
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
```

In general, the `enumerate` function accepts an iterable as an input, and returns a new iterable that produces a tuple of the iteration-count and the corresponding item from the original iterable. Thus the items in the iterable are being enumerated. To see the utility of this, suppose that we want to record all of the positions in a list where the value `None` is stored. We can achieve this by tracking the iteration count of a for-loop over the list. 

```python
# track which entries of an iterable store the value `None`
none_indices = []
iter_cnt = 0  # manually track iteration-count

for item in [2, None, -10, None, 4, 8]:
    if item is None:
        none_indices.append(iter_cnt)
    iter_cnt = iter_cnt + 1

# `none_indices` now stores: [1, 3]
```

We can simplify this code, and avoid having to initialize or increment the `iter_cnt` variable, by utilizing `enumerate` along with tuple-unpacking.

```python
# using the `enumerate` function to keep iteration-count
none_indices = []

# note the use of iterable unpacking! 
for iter_cnt, item in enumerate([2, None, -10, None, 4, 8]):  
    if item is None:
        none_indices.append(iter_cnt)
        
# `none_indices` now stores: [1, 3]
```

<div class="alert alert-info">

**Takeaway**: 

The built-in [enumerate](https://docs.python.org/3/library/functions.html#enumerate) function should be used (in conjunction with iterator unpacking) whenever it is necessary to track the iteration count of a for-loop. It is valuable to use this in conjunction with tuple unpacking.  
</div>
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: enumerate**

Use the iterable `"abcd"`, the `enumerate` function, and tuple-unpacking in a for-loop to create the list: `[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]`

</div>


<div class="alert alert-info">

**Reading Comprehension: Is it sorted?**

Use control flow and looping tools to see if an iterable of numbers is sorted. 

The variable `unsorted_index` should be initialized to `None`. If the iterable is *not* sorted, `unsorted_index` should store the index where the sequence *first* fell out of order. If the iterable is sorted, then `unsorted_index` should remain `None` and your code should print "sorted!".

For instance: 

 - given the iterable `my_list = [0, 1, -10, 2]`, `unsorted_index` should take the value `2`. 
 - given the iterable `my_list = [-1, 0, 3, 6]`, `unsorted_index` should be `None` and your code should print "sorted!". 

</div>


## Links to Official Documentation

- [Iterable Definition](https://docs.python.org/3/glossary.html#term-iterable)
- [Functions on iterables](https://docs.python.org/3/howto/functional.html#built-in-functions)
- [enumerate](https://docs.python.org/3/library/functions.html#enumerate)

<!-- #region -->
## Reading Comprehension Exercise Solutions:
**enumerate: Solution**

```python
out = []
for num, letter in enumerate("abcd"):
    out.append((num, letter))
```

**Is it sorted?: Solution**
```python
my_list = [0, 1, -10, 2]
unsorted_index = None

for index, current_num in enumerate(my_list):
    if index == 0:
        prev_num = current_num
    elif prev_num > current_num:
        unsorted_index = index
        break
    prev_num = current_num
else:
    print("sorted!")
```
<!-- #endregion -->
