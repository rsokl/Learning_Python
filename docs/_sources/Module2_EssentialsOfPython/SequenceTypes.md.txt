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
   :description: Topic: understanding python sequences, Difficulty: Easy, Category: Section
   :keywords: list, tuple, string, slice, index, negative index, get item, pop, append, examples
<!-- #endraw -->

<!-- #region -->
# Sequence Types

<div class="alert alert-warning">

**Note**: 

There are reading-comprehension exercises included throughout the text. These are meant to help you put your reading to practice. Solutions for the exercises are included at the bottom of this page.
</div>

The following objects are all example of sequences:
```python
# examples of sequences

# a list
[0, None, -2, 1]

# a string
"hello out there"

# a tuple
("a", False, 0, 1)

# a NumPy array
numpy.ndarray([0.2, 0.4, 0.6, 0.8])
```

Being able to work with sequences of objects/data is so important that it warrants us to take our first (relatively) deep dive into Python. The preceding reading introduced Python lists and strings, two important objects that are built into the Python language. Although quite distinct from one another in terms of what they can contain, *lists and strings are both types of sequences* - they store a finite collection of objects whose ordering matters (e.g. `"cat"` and `"tac"` should be considered distinct strings). As such, lists, strings, and the other sequence types in Python all share a common interface for allowing users to inspect, retrieve, and summarize their contents.

In this section, we will:

- Introduce tuples, the last built-in sequence type that we have yet to encounter. 
- Demonstrate the common interface that can be used to inspect and summarize the contents of a sequence.
- Detail the all-important indexing scheme used by Python, which will allow us to access specific items or subsequences from a sequence.
<!-- #endregion -->

<!-- #region -->
## Tuples
The last built-in sequence type that we have yet to encounter is the `tuple` type. A tuple is very similar to a list, in that it can store a sequence of arbitrary objects (a mix of numbers, strings, lists, other tuples, etc.). Where lists are constructed using square-brackets, tuples use parentheses:

```python
# creating a tuple
>>> x = (1, "a", 2)  # tuple with 3 entries

# (3) does not make a tuple with one entry
# you must provide a trailing comma in this 
# instance 
>>> y = (3,)         # a tuple with 1 entry

>>> type(x)
tuple

>>> isinstance(y, tuple)
True
```

<div class="alert alert-warning">

**Checking multiple types**: 

`isinstance` can be used to check multiple types at once, by supplying it a tuple of types. That is,
```python
isinstance(x, (tuple, list, str))
```

Will check if `x` is a tuple *or* a list *or* a string. 
</div>
<!-- #endregion -->

<!-- #region -->
Unlike a list, *once a tuple is formed, it cannot be changed*. That is, a tuple is *immutable*, whereas a list is *mutable*. Tuples generally consume less memory than do lists, since it is known that a tuple will not change in size. Furthermore, tuples come in handy when you want to ensure that a sequence of data cannot be changed by subsequent code.

```python
# the contents of a list can be changed: it is "mutable"
>>> x = [1, "moo", None] 
>>> x[0] = 2
>>> x
[2, 'moo', None]

# the contents of a tuple cannot be changed: it is "immutable"
>>> y = (1, "moo", None)  # (a, b, ...) creates a tuple
>>> y[0] = 2
TypeError: 'tuple' object does not support item assignment
```

`tuple` can be used to convert other sequences (other iterables, more generally) into tuples. `str` and `list` behave similarly.
```python
# `tuple` can create a tuple out of other sequences
>>> x = [2, 4, 8]
>>> y = tuple(x)

>>> x 
[2, 4, 8]

>>> y
(2, 4, 8)
```
<!-- #endregion -->

<!-- #region -->
## Working with sequences
The following summarizes the common interface that is shared by Python's different types of sequence, which includes lists, tuples, and strings. This interface allows you to inspect, summarize, join, and retrieve members from any variety of sequence.

**Checking if an object is contained within a sequence:** `obj in seq`
```python
# using 'in' and 'not in' for membership checking
>>> x = (1, 3, 5)

>>> 3 in x
True

>>> 0 in x
False

>>> 0 not in x
True

# strings can also test for sub-sequence membership
>>> "cat" in "the cat in the hat"
True

# you cannot test for sub-sequence membership in other
# types of sequences
>>> [1, 2] in [1, 2, 3, 4]
False

# the list [1, 2] must be an element of the list
# to be seen as a member
>>> [1, 2] in [None, [1, 2], None]
True
```

**Concatenating sequences:** `seq1 + seq2`
```python
# concatenating sequences with '+'
>>> [1, 2] + [3, 4]  # creates a new list
[1, 2, 3, 4]

>>> "c" + "at"
"cat"
```

**Repeated concatenation of a sequence:** `n*seq1` or `seq1*n`
```python
# equivalent to `cat + cat + cat`
>>> "cat" * 3   # creates a new string
'catcatcat'

>>> 4 * (1, 5)  # creates a new tuple
(1, 5, 1, 5, 1, 5, 1, 5)
```

**Asking for the number of members in a sequence:** `len(seq)`
```python
# getting the length of a sequence
>>> len("dog")
3

>>> len(["dog", "dog"])
2

>>> len([])
0
```

**Getting the index of the first occurrence of** `x` **in a sequence**: `seq.index(x)`
```python
>>> "cat cat cat".index("t")  # 't' first occurs at index-2 
2

# `index` doesn't look within sequences contained by the outer sequence
# e.g. it sees 1, 2, and "moo", not 1, 2, "m", "o", "o"
>>> [1, 2, "moo"].index("m")
ValueError: 'm' is not in list
```

**Counting the number of occurrences of** `x` **in a sequence**: `seq.count(x)`
```python
>>> "the cat in the hat".count("h")
3

# `count` doesn't look within sequences contained by the outer sequence
# thus is doesn't "see" the 1 within `[1, 2]`.
>>> [1, [1, 2], "111", 1].count(1)  
2
```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Basics of sequences**

1\. Change the list `[True, None, 22]` into a tuple.

2\. How many sequence-types have we discussed thus far? Which of these produce objects that are immutable? Which of these produce objects that are mutable? For those types that are mutable, write a piece of example code that mutates an object.

</div>

<!-- #region -->
### Introducing Indexing and Slicing
We can access individual items from a sequence by specifying the *index* of that item. Python ascribes the 1st entry in a sequence index-0, the second entry index-1, and so on.
```python
# accessing individual items from a sequence via indexing
>>> x = "abcdefg"
>>> x[0]
"a"

>>> x[2]
"c"
```

We can also "slice" a sequence, specifying a start-index and stop-index, and return a subsequence of the items contained within the slice:
```python
# "slicing" a sequence produces a subsequence of its contents 
>>> x[0:3] # include items 0, 1, 2 (3 is excluded) 
"abc"
```
It is critical to have a good grasp of how to access a sequence's members and subsequences by using indexing and slicing. This indexing scheme will also appear in our work with NumPy arrays. We will proceed by providing a detailed rundown of Python's indexing and slicing mechanisms.

### Indexing
Python allows you to retrieve individual members of a sequence by specifying the *index* of that member, which is the integer that uniquely identifies that member's position in the sequence. *Python implements 0-based indexing for its sequences*, and also permits the use of negative integers to count from the end of the sequence. Consider the string `"Python"`. The following diagram displays the indices for this sequence:
```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
   0   1   2   3   4   5  
  -6  -5  -4  -3  -2  -1
```

The first row of numbers gives the position of the indices 0…5 in the string; the second row gives the corresponding negative indices. 

**Positive Indices** 

- 0 $\rightarrow$ P
- 1 $\rightarrow$ y
- 2 $\rightarrow$ t
- 3 $\rightarrow$ h
- 4 $\rightarrow$ o
- 5 $\rightarrow$ n

**Negative Indices** 

- -6 $\rightarrow$ P
- -5 $\rightarrow$ y
- -4 $\rightarrow$ t
- -3 $\rightarrow$ h
- -2 $\rightarrow$ o
- -1 $\rightarrow$ n

Given this indexing scheme, Python reserves the use of square brackets following a variable name or object, as the "get-item" syntax: `seq[index]`.

```python
# Demonstrating indexing into sequences
>>> x = [1, 2, 3, 4]

# this is known as the "get-item" syntax
>>> x[0]     # indexing starts at 0
1

>>> x[-4]    # each entry has a positive index and negative index
1

>>> x[-1]     # negative indexing is relative to the end of the sequence
4

>>> "cat"[2]  # you can index directly into a sequence-object
't'

>>> (True, False)[-1]
False
```

<div class="alert alert-info">

**Takeaway**:

To "index into" a sequence is to retrieve a single member by specifying an integer index, that indicates the place of that member in the sequence: `seq[index]`. Python uses a zero-based indexing system, meaning that the first element in a sequence is located at position 0. Negative indices allow you to refer to an item's position relative to the end of the list.  
</div>
<!-- #endregion -->

<!-- #region -->
### Slicing
Slicing a sequence allows us to retrieve a subsequence of items, based on the indexing scheme that we reviewed in the preceeding subsection. Specifying a slice consists of:

- A start-index: the sequence-position where the slice begins (this item is *included* in the slice).
- A stop-index: the sequence-position where the slice ends (this item is *excluded* from the slice).
- A step-size, which permits us to take every item within the start & stop bounds, or every *other* item, and so on. It is important to note that a negative step-size permits us to traverse a sequence *in reveresed order*. 

The basic syntax for slicing is: `seq[start:stop:step]`, using colons to separate the start, stop, and step values.

```python
# demonstrating the basics of slicing a sequence
>>> seq = "abcdefg"

# start:0, stop:4, step:1
>>> seq[0:4:1]
'abcd'

# start:1, stop:4, step:1
>>> seq[1:4:1]
'bcd'

# start:0, stop:5, step:2
>>> seq[0:5:2] # get every other entry within [start, stop)
'ace'

# starting and stopping at the same index produces an empty sequence
# start:0, stop:0, step:1
>>> seq[0:0:1]
''
```

Slicing provides sensible default start, stop, and step values. Their default values are:

- start: 0
- stop: `len(seq)`
- step: 1

You can omit any of these values or specify `None` in that entry to use the default value. You can omit the second colon entirely, and the slice will use a step-size of 1.  
```python
# using default start, stop, and step values
>>> seq = "abcdefg"

# start: 0, stop: 7, step: 1 
>>> seq[:]  # equivalent: `seq[None:None]`
'abcdefg'

# start: 0, stop: 7, step: 2
>>> seq[::2]
'aceg'
```

Negative values can also be used in a slice. Specifying a negative step-value instructs the slice to traverse the sequence *in reverse order*. In this case, the default start and stop values will change so that `seq[::-1]` produces the sequence in reverse.

```python
# using a negative step size reverses the order of the sequence
>>> seq[::-1]
'gfedcba'
```

As we saw with using negative indices, specifying negative start/stop values in a slice permits us to indicate indices relative to the end of the list. 
```python
# a slice returning the last two values of the sequence
>>> seq[-2:]
'fg'

# a slice returning all but the last two values of the sequence
>>> seq[:-2]
'abcde'
```

Although the colon-syntax for slicing, `seq[start:stop:step]`, appears nearly ubiquitously in Python code, it is important to know that there is a built-in `slice` object that Python uses to form slices. It accepts the same start, stop, and step values, and produces the same sort of slicing behavior:
```python
# using the `slice` object explicitly
>>> seq = "abcdefg"
>>> seq[slice(0, 3, 1)]
'abc'
```

This gives you the ability to work with slices in more creative ways in your code, since it allows you to assign a variable to a slice.
```python
# using the `slice` object to slice several sequences
>>> seq1 = "apple"
>>> seq2 = (1, 2, 3, 4, 5)
>>> seq3 = [True, False, None]

>>> reverse = slice(None, None, -1)

>>> seq1[reverse]
'elppa'

>>> seq2[reverse]
(5, 4, 3, 2, 1)

>>> seq3[reverse]
[None, False, True]
```

<div class="alert alert-info">

**Takeaway**:

To "slice" a sequence is to retrieve a subsequence by specifying a start-index (included), a stop-index (excluded), and a step value. Negative values can be supplied for these, and default values are available as well. The common slicing syntax `seq[start:stop:step]` is actually just a nice shorthand for using a `slice` object: `seq[slice(start, stop, step)]`.  
</div>
<!-- #endregion -->

<!-- #region -->
#### Handling out-of-bounds indices
Attempting to get a member from a sequence using an out-of-bounds index will raise an `IndexError`:
```python
>>> x = [0, 1, 2, 3, 4, 5] # x only contains 6 items
>>> x[6]  # try to access the 7th item in `x`
IndexError: list index out of range

>>> x[-7]
IndexError: list index out of range
```

However, specifying an out-of-bounds start or stop value for a slice does not raise an error. Instead, the nearest valid start/stop value is used instead:
```python
# no bounds checking is used for slicing
>>> x[:10000]
[0, 1, 2, 3, 4, 5]
```

<div class="alert alert-warning">

**Warning!**

The lack of bounds-checking for slices can be a major source of errors when starting out with Python. Just because your code isn't raising an error does not mean that you have computed the correct start/stop values for your slice!
</div>
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info">

**Reading Comprehension: Indexing and Slicing Sequences**

In Python, a **sequence** is any ordered collection of objects whose contents can be accessed via "indexing". A sub-sequence can be accessed by "slicing" the sequence. You saw, in the required reading, that Python's lists and strings are both examples of sequences. The following questions will help you explore the power of sequence indexing and slicing.

Given the tuple: 
```python
x = (0, 2, 4, 6, 8)
```
Slice or index into `x` to produce the following:

1. `0`
2. `8` (using a negative index)
3. `(2, 4, 6)` (using a slice-object)
4. `(4,)`
5. `4` 
6. `4` (using a negative index)
7. `(6, 8)` (using a negative index for the start of the slice)
8. `(2, 6)`
9. `(8, 6, 4, 2)`

</div>
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Checking Your General Understanding**

Write a piece of code for each of the following tasks. If the task is impossible/ill-posed explain why.

1) Using the string "blogosphere", slicing, and repeat-concatenation, create the string: 'boopeeboopeeboopeeboopeeboopee'. (hint: how would you slice "blogosphere" to produce "boopee", think step-size)

2) Assume that a tuple, `x`, contains the item `5` in it at least once. Find where that first entry is, and change it to `-5`. For example `(1, 2, 5, 0, 5)` $\rightarrow$ `(1, 2, -5, 0, 5)`.

3) Given a sequence, `x`, and a valid negative index for `x`, `neg_index`, find the corresponding positive-value for that index. That is, if `x = "cat"`, and `neg_index = -3`, which is the negative index that would return `"c"`, then you would want to return the index `0`. 

</div>


## Links to Official Documentation

- [Sequences](https://docs.python.org/3/library/stdtypes.html#typesseq)
- [Tuples](https://docs.python.org/3/library/stdtypes.html#tuple)
- [Immutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#immutable-sequence-types)
- [Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)

<!-- #region -->
## Reading Comprehension Exercise Solutions:

**Basics of sequences**

```python
# 1. Change the list [True, None, 22] into a tuple.
>>> tuple([True, None, 22])
(True, None, 22)
```

2\. We have been introduced to three Python types that are sequential in nature: strings, lists, and tuples. Among these, lists are the only mutable objects. We can demonstrate this by simply appending a new element to the end of a list that has already been constructed.
```python
>>> x = [1, 2, 3]
>>> x
[1, 2, 3]

>>> x.append("I'm different now")
>>> x
[1, 2, 3, "I'm different now"]
```
<!-- #endregion -->

<!-- #region -->
**Indexing and Slicing Sequences: Solutions**

1. `x[0]`
2. `x[-1]`
3. `x[slice(1, 4, 1)]`
4. `x[2:3]`
5. `x[2]`
6. `x[-3]`
7. `x[-2:]`
8. `x[1:4:2]`
9. `x[:0:-1]`

**Checking Your General Understanding: Solutions**

1) "boopee" is every-other letter in "blogosphere", thus slicing this sequence with a step-size of 2, `"blogosphere"[::2]`, returns "boopee". We can then use `seq*n` to repeat this sequence five times. Thus the solution is
```python
>>> "blogosphere"[::2]*5
'boopeeboopeeboopeeboopeeboopee'
```

2) Tuples are immutable objects. This means that their content cannot be changed once it is created. Thus this question is ill-posed! How clever am I for writing that question? I feel so clever. Wow. I'm great.

If that question was posed in terms of a *list*, then the solution would be:
```python
>>> x = [1, 2, 5, 0, 5]
>>> x[x.index(5)] = -5
>>> x
[1, 2, -5, 0, 5]
```

3) Refer to the "index" diagram to see that this is the simple relationship between positive and negative indices for a given sequence: 
```python
pos_index = neg_index + len(x)
```
<!-- #endregion -->
