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
   :description: Topic: Introduction to Sets, Difficulty: Medium, Category: Section
   :keywords: set, complexity, comparison, union, intersection, membership, hashing, lookup, interview preparation
<!-- #endraw -->


# Data Structures (Part III): Sets & the Collections Module
## The "Set" Data Structure
The `set` type describes an *unordered* collection of *unique* objects. It is useful for:

- Filtering out "repeat" objects in a collection, producing only its unique members.
- Quickly checking for membership, as a $\mathcal{O}(1)$ operation.
- Efficiently comparing two sets of objects; e.g. if one set is a "subset" of another.

A set uses a "hashing" scheme for keeping track of its contents. Thus, like a dictionary's keys, a set can only store *immutable* objects so that its hashes will never become invalid. Unlike the other data structures that we have encountered, *there is no mechanism for retrieving an individual item from a set*. That is, there is no index or key that can be used to retrieve an individual member from a set. 

Python's sets also support many familiar set-algebra operations, like taking the union or intersection of sets, as we will see below. For an exhaustive listing of the functions available to sets, please consult [the official documentation on sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset).

<!-- #region -->
### Creating a set
You can initialize a set using the syntax: `{item1, item2, ...}`. Please note that this is distinct from the the dictionary-initialization syntax, which uses a colon to indicate key-value pairs:

```python
# initializing a set containing various immutable objects
>>> {1, 3.4, "apple", False, (1, 2, 3)}
{False, 1, (1, 2, 3), 3.4, 'apple'}
```
A set can be constructed using the generator-comprehension syntax:
```python
# initialization via set-comprehension
>>> {i**2 for i in range(5) if i != 3}
{0, 1, 4, 16}
```

And, like the `list`, `tuple`, and `dict` types, the `set` type can be used to construct a set from an iterable. Note that you must use `set()` if you want to create an empty set, using `{}` creates an empty *dictionary*:
```python
# introducing the `set` type
>>> type({2, 4, 6})
set

# using `set` to consume an iterable to construct a set
>>> set(range(4))
{0, 1, 2, 3}

# creating an empty set
>>> set()  # specifying `{}` would create an empty *dictionary*
set()
```

Redundant items are "ignored" when constructing or adding to a set. Thus *constructing a set is a great way to extract the unique items from a collection*: 
```python
# filter repeat-items from a collection by feeding it into a set
>>> x = [1, 2, 1, 2, 1, "moo", "moo"]
>>> set(x)
{1, 2, 'moo'}
```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Set Creation**

Use a set to find all of the unique letters in the string `"The cat in the hat"`. Ignore all non-letter characters and lowercase all letters.

</div>

<!-- #region -->
### Set operations
Sets support membership-checking ($\mathcal{O}(1)$) along with iteration ($\mathcal{O}(n)$). Note that sets are unordered; thus the order of iteration is effectively random:
```python
# checking membership in a set
>>> 2 in {1, 2, 3}
True

# iterating over a set (the order of iteration is random)
>>> [i for i in {"a", "b", "c"}]
['b', 'c', 'a']
```
Python also provides the set-theoretic operations of union, intersection, and the relations of set equality and set inclusion. These can be invoked using operator symbols or by calling functions on the set explicitly. 

For an exhaustive list of the functions available to the set, please [refer to the official Python documentation](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset).

```python
# demonstrating set-comparison operations
>>> x = {"a", "b", "c", "d"}
>>> y = {"a", "b", "e"}

# union: items in x or y, or both
>>> x | y  # or x.union(y)
{'a', 'b', 'c', 'd', 'e'}

# intersection: items in both x and y
>>> x & y  # or x.intersection(y)
{'a', 'b'}

# difference: items in x but not in y
>>> x - y  # or x.difference(y)
{'c', 'd'}

# symmetric difference: in x or y, but not in both
>>> x ^ y  # or x.symmetric_difference
{'c', 'd', 'e'}

# check if set_1 is a superset of set_2
>>> {1, 2, 3, 4} >= {1, 2}
True

# check if set_1 and set_2 are equivalent sets
>>> {1, 2, 3, 4} == {1, 2}
False
```

A set is a *mutable* object; it can be updated after it was created:
```python
# sets are mutable

# add a single member to `x`
>>> x.add("dog")

# update `x` by adding members of an iterable
>>> x.update([1, 2, 3])

# remove a member of `x`
>>> x.remove("a")
>>> x
{1, 2, 3, 'b', 'c', 'd', 'dog'}
```
Because it is mutable, a set cannot be used as a dictionary-key, nor can a set be a member of another set. Python provides an immutable version of the set, `frozenset`, which has all of the functions of a set other than those that mutate the set:
```python
# `frozenset` is an immutable version of a Python set
>>> frozenset(x)
frozenset({1, 2, 3, 'b', 'c', 'd', 'dog'})
```

<div class="alert alert-info"> 

**Takeaway**: 

Python's set is an unordered collection of unique, immutable objects. It is an excellent tool for extracting the unique members from a collection of items. The set provides  $\mathcal{O}(1)$ membership-checking along with a suite of set-algebra operations for comparing sets. `frozenset` is an immutable version of the set.
</div>
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info">

**Reading Comprehension: Set Comparisons**

Given the enrollment lists for class-A and class-B, find the students enrolled in both classes. Produce the result as a sorted list of names. 

```python
>>> classA = ["Bohr", "Curie", "David", "Euler", "Fermi", "Feynman", "Gauss", "Heisenberg", "Noether"]
>>> classB = ["Bohm", "Bohr", "Einstein", "Fermi", "Gauss", "Hopper", "Montalcini"]  
```

</div>
<!-- #endregion -->

## The Collections Module
Python provides a number of valuable, optimized data structures in its ["collections" module](https://docs.python.org/3/library/collections.html). It is recommended that the reader take some time to peruse this module. Here, we will briefly show off some of the utilities of its data structures. 

Refer to the [official documentation](https://docs.python.org/3/library/collections.html) for a complete listing of the functions available to these data structures.

<!-- #region -->
### Named-Tuple
A named tuple allows you to form a tuple whose members are named. Thus the user can access a member by name or via index. Otherwise the named tuple behaves just like a typical tuple. This facilitates clean, readable code.

Suppose, for instance, you want to keep track of the 3D-position and time of an event. You can use a named-tuple so that each space and time coordinate can be referenced "by name". In this way, the reader doesn't have to keep in mind that element-3 of your tuple corresponds to time:

```python
# demonstrate the use of named tuple
>>> from collections import namedtuple

# Define a tuple that holds a space-time coordinate.
# Here we define the tuple to have four entries, named 
# 'x', 'y', 'z', and 't', in order.
>>> space_time_coord = namedtuple("space_time_coord", ['x', 'y', 'z', 't'])

# `r` is a particular space-time coordinate (an instance of our named tuple)
>>> r = space_time_coord(1.5, 2.3, 5.1, 100.2)

>>> r.x  # access the x coordinate "by name"; this is more descriptive than `r[0]`
1.5

>>> r.y
2.3

>>> r.z
5.1

>>> r.t  
100.2

# you can also access contents by indexing/slicing
>>> r[3]  
100.2

>>> r[:]
(1.5, 2.3, 5.1, 100.2)
```
<!-- #endregion -->

<!-- #region -->
### Default Dictionary
A default dictionary allows you to specify a Python function, $f$ that will be used as a "default value" for that dictionary. The default value will be whatever $f()$ returns. That is, whenever you try to access a key that does not exist in the dictionary, instead of raising `KeyError`, the mapping $key \rightarrow f()$ will be created in the dictionary:

```python
# demonstrate the behavior of the `defaultdict`
>>> from collections import defaultdict

>>> example_default_dict = defaultdict(list)  # will map any missing key to `list()`
>>> example_default_dict  # an empty default dictionary
defaultdict(list, {})

# "apple" is not a key, so the default mapping "apple" -> list() is created
# and this value is returned
>>> example_default_dict["apple"]  
[]

# this mapping now exists in the dictionary
>>> example_default_dict 
defaultdict(list, {'apple': []})
```

Suppose you want to use a dictionary as a grade book, which maps $name \rightarrow grades$. With a standard dictionary, you have to worry about encountering a student for the first time:
```python
# using a vanilla dictionary to store: name -> list of grades
student = "Ryan"
grade = 52  # I failed the test...

# standard dictionary usage
gradebook = {}

# if student isn't in the gradebook, enter that student 
# along with an empty list as the grades
if student not in gradebook:
    gradebook[student] = []

gradebook[student].append(grade)  # append the grade to that student's list of grades
```
The default dictionary's behavior exactly accommodates this initialization process (when providing `list` as the initialization function):

```python
# using a default dictionary to store: name -> list of grades
>>> gradebook = defaultdict(list)

# Because "Susan" doesn't exist in the dictionary
# `list()` creates an empty list, as a default value,
# which we can immediately append her grade to
>>> gradebook["Susan"].append(84)

>>> gradebook
defaultdict(list, {'Susan': [84]})
```
<!-- #endregion -->

<!-- #region -->
### Counter
Python's counter data structure is designed for tallying the unique objects that it encounters. It essentially creates a dictionary that maps: $obj \rightarrow count$. Suppose you want to study the distribution of words used in a body of text; counter is perfect for this application:
```python
# demonstrate the `Counter` data structure
>>> from collections import Counter

# Note: We will "normalize" our text by making it all lowercase. 
# We will then split the string by its spaces, storing the resulting 
# tokens in a list. For real text, we would also want to remove punctuation
>>> text_1 = "The cat in the hat"
>>> text_1 = text_1.lower().split()
>>> text_1
['the', 'cat', 'in', 'the', 'hat']

>>> word_distr = Counter(text_1)  # tally the unique objects in `text_1`
>>> word_distr
Counter({'cat': 1, 'hat': 1, 'in': 1, 'the': 2})

# feed additional items to the counter by "update"
>>> text_2 = "The apple in the tree"
>>> text_2 = text_2.lower().split()
>>> word_distr.update(text_2)
>>> word_distr
Counter({'apple': 1, 'cat': 1, 'hat': 1, 'in': 2, 'the': 4, 'tree': 1})

# get the top-2 most common words, along with their counts
>>> word_distr.most_common(2)
[('the', 4), ('in', 2)]

# get the count for the word "tree"
>>> word_distr["tree"]
1
```

`Counter` accepts any iterable of immutable objects:
```python
>>> Counter([0, 0, "moo", (None, None), (None, None), (None, None)])
Counter({(None, None): 3, 0: 2, 'moo': 1})
```
Refer to the [official documentation](https://docs.python.org/3/library/collections.html#counter-objects) for a complete listing of all the nice functions that `Counter` has access to.
<!-- #endregion -->

<!-- #region -->
### The deque
Like the list, Python's deque is a mutable, sequential data structure. What distinguishes the deque is that:

 - Mutating either the beginning or the end of a deque is $\mathcal{O}(1)$, whereas mutating the beginning of a list is $\mathcal{O}(n)$. As such, the deque has unique functions to take advantage of this, like `appendleft`.
 - The downside of the preceding feature is that *accessing items near the middle of the deque is* $\mathcal{O}(n)$, whereas it is $\mathcal{O}(1)$ for lists and tuples.

A complete rundown of the deque's functionality can be found [here](https://docs.python.org/3/library/collections.html#deque-objects).

The deque is included in Python's `collections` module, and thus must be imported:
```python
>>> from collections import deque
>>> my_deque = deque([1,2,3])
>>> my_deque.appendleft(0)
>>> my_deque
deque([0, 1, 2, 3])
```
<!-- #endregion -->

## Links to Official Documentation

- [Sets and frozen sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
  - [Tutorial on sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [The collections module](https://docs.python.org/3/library/collections.html)


## Reading Comprehension Solutions

<!-- #region -->
**Set Creation: Solution**

Use a set to find all of the unique letters in the string `"The cat in the hat"`. Ignore all non-letter characters and lowercase all letters.

We can use the built-in string functions [isalpha](https://docs.python.org/3/library/stdtypes.html#str.isalpha) and [lower](https://docs.python.org/3/library/stdtypes.html#str.lower) to filter out non-letter characters, and to lowercase the letters.

```python
>>> sentence = "The cat in the hat"
>>> {char.lower() for char in sentence if char.isalpha()}
{'a', 'c', 'e', 'h', 'i', 'n', 't'}
```
<!-- #endregion -->

<!-- #region -->
**Set Comparisons: Solution**

Given the roster for class-A and class-B, find the students enrolled in both classes. Produce the result as a sorted list.

```python
>>> classA = ["Bohr", "Curie", "David", "Euler", "Fermi", "Feynman", "Gauss", "Heisenberg", "Noether"]
>>> classB = ["Bohm", "Bohr", "Einstein", "Fermi", "Gauss", "Hopper", "Montalcini"]  
```
We can find the entries common to both lists by constructing sets from them, and then taking the intersection of those sets. The result is a set,  which is an iterable. Thus it can be fed to the built-in function [sorted](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html#Functions-that-act-on-iterables), to produce a sorted list of names.

```python
>>> sorted(set(classA) & set(classB))
['Bohr', 'Fermi', 'Gauss']
```
<!-- #endregion -->
