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
   :description: Topic: Introduction to Dictionaries, Difficulty: Medium, Category: Section
   :keywords: dictionary, complexity, key, value, iteration, get item, hashing, lookup, interview preparation
<!-- #endraw -->

#  Data Structures (Part II): Dictionaries
Python's dictionary allows you to store key-value pairs, and then pass the dictionary a key to quickly retrieve its corresponding value. Specifically, you construct the dictionary by specifying one-way mappings from key-objects to value-objects. **Each key must map to exactly one value**, meaning that a key must be unique. 


<!-- #region -->
Let's create the following mapping of grocery-to-price:

- "cheese" $\rightarrow$ 2.53, 
- "milk" $\rightarrow$ 3.40, 
- "frozen pizza" $\rightarrow$ 8.01

```python
# use a dictionary to map groceries to prices: item-name -> price 
>>> items_to_prices = {"cheese": 2.53, "milk": 3.40, "frozen pizza": 8.01}

# looking up the price of "frozen pizza"
>>> items_to_prices["frozen pizza"]
8.01
```

Python's dictionary is a shining star among its data structures; it is compact, fast, versatile, and extremely useful. It can be used to create a wide variety of mappings.

```python
# keep track of whether or not a 3D coordinate fell into some region in space
# map (x, y, z) coordinates to "is in a region": (x, y, z) -> True/False
>>> point_to_region = {(0.1, 2.2, 3):False, (-10., 0, 4.5):True, (4.3, 1.0, 9.5):False}
>>> point_to_region[(-10., 0, 4.5)]
True

# map student-name to exam scores: name -> scores
>>> name_to_scores = {"Ryan S": [65, 50, 80], "Nick S": [100, 99, 90]}
>>> name_to_scores["Ryan S"]
[65, 50, 80]
```

 It is important to note outright that the time it takes for dictionary to take a key and retrieve a value *does not depend on the size of the dictionary.* That is the complexity for a dictionary look-up is $\mathcal{O}(1)$! It accomplishes this by making use of a technique known as [hashing](https://en.wikipedia.org/wiki/Hash_function).

These are all instances of the built-in `dict` type:
```python
>>> type(items_to_prices)
dict
```
We will be discussing the essentials of the dictionary. It is highly recommended that you refer to the official Python documentation for a [complete rundown of all the functions available to the dictionary](https://docs.python.org/3/library/stdtypes.html#dict).
<!-- #endregion -->

<!-- #region -->
## Dictionary Basics
### Constructing a dictionary
A nice syntax for creating a dictionary is to specify key-value pairs inside "curly braces": `{key1:value1, key2:value2, ...}`. As an example, let's construct a dictionary that maps types of foods to "fruit" or "vegetable". We'll start by mapping "apple" to "fruit", and "carrot" to "vegetable"
```python
# use `{key1:value1, key2:value2, ...} to create a dictionary that maps:
#  "apple" -> "fruit"
# "carrot" -> "vegetable
>>> fruit_or_veggie = {"apple":"fruit", "carrot":"vegetable"} 

# create an empty dictionary
>>> {}
{}
```
You can also use `dict` as a constructor to create the dictionary. It can be fed an iterable of key-value pairs, each of which is packed in a sequence, such as a tuple. 

```python
# use `dict` to create a dictionary that maps:
#  "apple" -> "fruit"
# "carrot" -> "vegetable
>>> fruit_or_veggie = dict([("apple", "fruit"), ("carrot", "vegetable")])

# use `dict` to create an empty dictionary:
>>> dict()
{}
```
Lastly, Python also supports a dictionary-comprehension syntax, which mirrors the generator/list comprehension syntax covered earlier in this module:

```
{key:value for key, value in <iterable of key-value pairs> [if bool(<condition>)]}
```

```python
# use the 'dictionary comprehension' syntax to create a dictionary that maps:
#  "apple" -> "fruit"
# "carrot" -> "vegetable
>>> {k:v for k,v in [("apple", "fruit"), ("carrot", "vegetable")]}
{'apple': 'fruit', 'carrot': 'vegetable'}
```

### Retrieving a value, given a key
Now we can use this dictionary to "look up" if an item is a fruit or a veggie. Dictionaries support the same square-bracket "get-item" syntax as a list/tuple, but here a valid key is used as the index:
```python
# get the value associated with the key "apple"
>>> fruit_or_veggie["apple"]
"fruit"
```

`KeyError` will be raised if you try to look-up a key that doesn't exist:
```python
# "grape" hasn't been specified as a key
>>> fruit_or_veggie["grape"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-30-74c002a67890> in <module>()
----> 1 fruit_or_veggie["grape"]

KeyError: 'grape'
```

### Adding more key-value mappings
Once created, a dictionary can have a new key-value pair be "set" using `my_dict[new_key] = new_value`:
```python
# set the mapping "banana" -> "fruit"
>>> fruit_or_veggie["banana"] = "fruit"
>>> fruit_or_veggie
{'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}
```
If the key already exists, the mapping for that key will simply be updated.

The `update` function can be used to add multiple key-value pairs at once. This function can be passed another dictionary or an iterable of key-value sequences
```python
# adding multiple key-value pairs to the dictionary
>>> fruit_or_veggie.update([("grape", "fruit"), ("onion", "vegetable")])
>>> fruit_or_veggie
{'apple': 'fruit',
 'banana': 'fruit',
 'carrot': 'vegetable',
 'grape': 'fruit',
 'onion': 'vegetable'}
```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Dictionary Basics**

Given the tuple of student names `("Ashley", "David", "Edward", "Zoe")`, and their corresponding exam grades `(0.92, 0.72, 0.88, 0.77)`, create a dictionary that maps: name $\rightarrow$ grade. Then, update Zoe's grade to `.79`. Lastly, add a new student, Ryan, whose grade is 0.34. 

</div>

<!-- #region -->
## What Can a Dictionary Store?
Although the preceding example only involves a mappings from strings to strings, *the keys and values of a dictionary can be heterogeneous in type*:

```python
# demonstrates the wide variety of object types that can be used as
# keys and values in a dictionary
>>> example_dict = {-1:10, "moo":True, (1, 2):print, 3.4:"cow", False:[]}
>>> example_dict[-1]
10

>>> example_dict["moo"]
True

>>> example_dict[(1, 2)]
<function print>

>>> example_dict[3.4]
"cow"

>>> example_dict[False]
[]
```

To be specific, a dictionary's contents are dictated by the following rules:

- A dictionary *key* must be an *immutable* object (more precisely, it must be [hashable](https://docs.python.org/3/glossary.html#term-hashable); don't worry about this detail). 
- A dictionary *value* can be any object (even the dictionary itself! Try this, it's cool!)

<div class="alert alert-warning">

**Recall**: 

A mutable object can be changed after it is created. An immutable object cannot be changed.
</div>

Thus valid keys can be the following types:

 - numbers (integers, floating-point numbers, complex numbers)
 - strings
 - tuples (if the tuple contains anything, it must be other immutable objects)
 - boolean values
 - [frozenset](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_III_Sets_and_More.html#Set-operations) objects
 
Trying to use a mutable object as a key is problematic since that object could be changed *after* it was already used as a key. Thus the dictionary would have to "detect" this change and recreate its "lookup scheme" for the changed key. Values, on the other hand, can be mutable because the details of a given value-object have no impact on how the dictionary retrieves it.
 
In accordance with this discussion will get a `TypeError` if you try to use a list as a key, since lists are mutable:
```python
# trying to use a list as a key 
# this raises an error because lists are mutable
>>> bad_dict = {[]:1}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-50-e7cf39509d06> in <module>()
----> 1 bad_dict = {[]:1}

TypeError: unhashable type: 'list'
```

### Numerical Precision & Dictionary Keys
Care must be taken when using floating-point numbers as a key in a dictionary, [due to its limited numerical precision](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Understanding-Numerical-Precision). For the same reason that you ought not rely on two floats being equal, you should not assume that two floats will produce the same hash, when stored as a key:

```python
# the folly of using a floating-point number as a key
# in a dictionary
>>> x = {}
>>> x[(0.1 + 0.1 + 0.1) - 0.3] = "apple"
>>> x[0.0]
KeyError: 0
```

An acceptable way of accommodating the use of a float as a key, depending on the use case, is to first round the floating point number to normalize it to a lower precision:

```python
# rounding a float before using it as a key
>>> x = {}

# round the float to its 2nd decimal place
>>> float_key = round((0.1 + 0.1 + 0.1) - 0.3, 2)
>>> x[float_key] = "apple"
>> x[0.0]
'apple'
```

<div class="alert alert-info">

**Takeaway**: 

A dictionary key must be an immutable object. A dictionary value can be any object.
</div>
<!-- #endregion -->

<!-- #region -->
### Inspecting a Dictionary
The dictionary provides tooling for inspecting and iterating over its keys and values. We will use the following dictionary for our examples:

```python
>>> example_dict = {"key1":"value1", "key2":"value2", "key3":"value3"}
```

**Inspecting a dictionary's keys**

The dictionary itself can be used to iterate over its keys:
```python
# iterating over a dictionary produces its keys
>>> [i for i in example_dict]
['key1', 'key2', 'key3']
```

You can also use the dictionary to test for membership among its keys:

```python
# checking if an object is among a dictionary's keys
>>> "key3" in example_dict
True

# you *cannot* use this to check for membership among its valus
>>> "value3" in example_dict
False
```
`len` counts the number of keys in the dictionary:
```python
>>> len(example_dict)
3
```

`example_dict.keys()` also returns an iterable over the dictionary's keys, and thus can be used to exactly the same effect as the dictionary itself in these preceding examples.

**Inspecting a dictionary's values**

`example_dict.values()` can be iterated over to produce that dictionary's values:
```python
# iterating over a dictionary's values
>>> [i for i in example_dict.values()]
['value1', 'value2', 'value3']
```

You can also use this to test for membership among the dictionary's values:

```python
# checking if an object is among a dictionary's values
>>> "value1" in example_dict.values()
True
```

**Inspecting a dictionary's key-value pairs**

`example_dict.items()` can be iterated over to produce that dictionary's key-value pairs (which are packed into tuples):
```python
# iterating over a dictionary produces its keys
>>> [i for i in example_dict.items()]
[('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]
```

You can also use this to test for membership among the dictionary's key-value pairs:

```python
# checking if a key-value pair exists in a dictionary
>>> ('key1', 'value1') in example_dict.items()
True
```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Inverting a Dictionary**

Write a function that inverts a dictionary. For example, if you were given `x = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}`, you would produce the dictionary `inverted_x = {'v1': 'k1', 'v2': 'k2', 'v3': 'k3'}`.

</div>


<div class="alert alert-info">

**Reading Comprehension: Inspecting a Dictionary**

Assume we are working with a dictionary whose values are all *unique* numbers. Write a function that returns the *key* that maps to the *largest* value in the dictionary. 

Next, generalize your solution for a dictionary whose values are not necessarily unique. Return a tuple of all of the keys that map to that max value.
</div>


### Time Complexities of the Dictionary's Functions
In addition to being flexible and versatile, the dictionary's functions manage to be quite efficient as well. The following is a summary of the time complexities associated with various common operations using a dictionary (according to its implementation in CPython) - note all the $\mathcal{O}(1)$ operations!

Let `example_dict` represent a dictionary with $n$ key-value pair mappings.

The following are $\mathcal{O}(1)$ operations:

- Return the number of keys in the dictionary: `len(example_dict)` 
- Check if the key is in the dictionary, and return the value if it is: `example_dict[key]` 
- Set a key-value mapping: `example_dict[key] = value` 
- Check if an object is among the dictionary's keys: `obj in example_dict` 
- Check if a pair of objects are among the dictionary's key-value pairs: `(obj1, obj2) in example_dict.items()`

The following are $\mathcal{O}(n)$ operations:

- Check if an object is among the dictionary's values: `obj in example_dict.values()`
- Iterate over the dictionary's keys/values/key-value pairs

<!-- #region -->
### Are Dictionaries Ordered? A Word of Warning
Unlike Python's sequences, the dictionary has no inherent ordering... that is, until Python 3.6 came out. 

Prior to Python 3.6, a dictionary had no ordering associated with it. If you iterated over a dictionary's keys, values, or key-value pairs, you had no guarantee about the *order* in which these items would be produced. `[i for i in example_dict]` could produce a list of keys with different ordering each time the code was run; you were only guaranteed that the list would contain all of the dictionary's keys: 

```python
# in Python 3.5 and earlier, dictionaries were unordered
>>> example_dict = {"key1":"value1", "key2":"value2", "key3":"value3"}

# this can produce lists with different orders
>>> [i for i in example_dict]
["key1", "key3", "key2"]

>>> [i for i in example_dict]
["key2", "key1", "key3"]

>>> [i for i in example_dict]
["key1", "key2", "key3"]

...
```

The dictionary was [reimplemented in Python 3.6](https://docs.python.org/3/whatsnew/3.6.html#new-dict-implementation) so that it will consume roughly 25% less memory than before (which is a big deal!). The catch is that this new implementation entails that the dictionary's various iterables (e.g. `dict.keys()`, `dict.values()`, `dict.items()`) will always yield their items according to the order in which they were added to the dictionary.

```python
# in Python 3.6 and beyond dictionaries are ordered according to the order in
# which key-value pairs were added to the dictionary by the user
>>> example_dict = {"key1":"value1", "key2":"value2", "key3":"value3"}

# this will always produce the same ordering of keys
>>> [i for i in example_dict]
["key1", "key2", "key3"]
```

This is great, right? Wrong! If you write code in Python 3.6 that relies on the fact that dictionaries are ordered, your algorithm will almost certainly produce the wrong results if you run it using Python 3.5 or earlier! Worst of all, it very unlikely that this will raise any error in your code so the bug will persist silently - this is very tough to catch!

**Unless you make explicit that your code is incompatible with versions of Python prior to Python 3.6, write your code as if the dictionary is unordered!** 

If you do want to use an ordered dictionary, make use of `collections.OrderedDict`, which behaves like just like the standard dictionary but is guaranteed to maintain ordering regardless of what version of Python you are using.  

```python
from collections import OrderedDict
>>> ordered = OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

# this will always produce the same result, regardless of what
# version of Python is being used
>>> [i for i in ordered]
["key1", "key2", "key3"]
```

<div class="alert alert-info">

**Takeaway**: 

No matter what version of Python you are using, write your code as if the Python dictionary is unordered. If you do want to use an ordered dictionary, your code should make use of `collections.OrderedDict`.
</div>
<!-- #endregion -->

## Links to Official Documentation

- [Dictionaries](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
  - [Dictionaries tutorial](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Definition of 'hashable'](https://docs.python.org/3/glossary.html#term-hashable)
- [Dictionary view objects](https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects)


## Reading Comprehension Solutions

<!-- #region -->
**Dictionary Basics: Solutions**

Given the tuple of student names `(Ashley, David, Edward, Zoe)`, and their corresponding exam grades `(0.92, 0.72, 0.88, 0.77)`, create a dictionary that maps: name $\rightarrow$ grade. 

Then, update Zoe's grade to `.79`. Lastly, add a new student, Ryan, whose grade is 0.34. 

```python
names = ("Ashley", "David", "Edward", "Zoe")
scores = (0.92, 0.72, 0.88, 0.77)
```

Here is a basic, but verbose solution. It is too long and its logic is complicated by the use of `index`.

```python
# basic solution for creating `grades`
grades = {}
for index in range(len(names)):
    name = names[index]
    value = scores[index]
    grades[name] = value
```

You should make use of the function [zip](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Itertools.html#zip) to pair the names and scores together in an iterable, and create the dictionary using a comprehension expression.

```python
# much better solution for creating `grades`
grades = {student:value for student, value in zip(names, scores)}

# updating Zoe's grade
grades["Zoe"] = 0.79

# adding Ryan's grade
grades["Ryan"] = 0.34
```
<!-- #endregion -->

<!-- #region -->
**Inverting a Dictionary: Solution**
```python
# simple solution: using a for-loop
x = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
inverted_x = {}
for key, value in x.items():
    inverted_x[value] = key
```

```python
# better solution: using a dictionary-comprehension
inverted_x = {value:key for key, value in x.items()}
```
<!-- #endregion -->

<!-- #region -->
**Inspecting a Dictionary: Solution**

Assume we are working with a dictionary whose values are all *unique* numbers. Write a function that returns the key that maps to the *largest* value in the dictionary. 

The solution that you should be able to arrive at is:

```python
# solution
def max_key(x): 
    max_val = max(x.values())
    for key, value in x.items():
        if value == max_val:
            return key
```
```python
>>> max_key({'a': 0, 'b': 2, 'c': 200, 'd': 0})
'c'
```

The downside of this is that it iterates over `x` twice: once via `max` and once via the for-loop. The optimal solution for this only involves a single iteration, however it requires advanced concepts that are beyond the scope of the material presented here. We include the ideal solution for posterity: 

You can provide the `max` function with "key" argument, which accepts the function that should be used to evaluate the "value" for each iteration, which is used to discern the max element. Here, we pass it the built-in dictionary-function [get](https://docs.python.org/3/library/stdtypes.html#dict.get), which takes in a dictionary's key as an argument, and returns the corresponding value from the mapping. Thus `max` will iterate over each key of `x`, and discern the maximum value by comparing the value returned by each `x.get(key)` (which is effectively the same as `x[key]`). 

```python
# optimal solution (for the sake of completeness)
def max_key_optimal(x):
    return max(x, key=x.get)
```
```python
>>> max_key_optimal({'a': -1, 'b': 30, 'c': 10, 'd': 500})
'd'
```

You can read more about this `key` parameter [here](https://docs.python.org/3/howto/sorting.html#key-functions).

Next, generalize your solution for a dictionary whose values are not necessarily unique. Return a tuple of the keys that map to that max value.

```python
def get_maxes(dictionary):
    max_val = max(dictionary.values())
    return tuple(k for k,v in dictionary.items() if v == max_val)

>>> get_maxes(dict(a=1, b=2, c=2, d=1))
('b', 'c')
```


<!-- #endregion -->
