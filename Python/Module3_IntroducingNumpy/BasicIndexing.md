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
   :description: Topic: Numpy array basic indexing, Difficulty: Medium, Category: Section
   :keywords: basic index, slice, no copy index, multidimensional array, nd array, view, reverse, axis
<!-- #endraw -->

<!-- #region -->
# Introducing Basic and Advanced Indexing

Thus far we have seen that we can access the contents of a NumPy array by specifying an integer or slice-object as an index for each one of its dimensions. Indexing into and slicing along the dimensions of an array are known as basic indexing. NumPy also provides a sophisticated system of "advanced indexing", which permits us powerful means for accessing elements of an array that is flexible beyond specifying integers and slices along axes. For example, we can use advanced indexing to access all of the negative-valued elements from `x`.

```python
# demonstrating basic indexing and advanced indexing
>>> import numpy as np
>>> x = np.array([[ -5,   2,  0, -7],
...               [ -1,   9,  3,  8],
...               [ -3,  -3,  4,  6]])

# Access the column-1 of row-0 and row-2.
# This is an example of basic indexing. 
# A "view" of the underlying data in `x`
# is produced; no data is copied.
>>> x[::2, 1]
array([ 2, -3])

# An example of advanced indexing.
# Access all negative elements in `x`.
# This produces a copy of the accessed data.
>>> x[x < 0]
array([-5, -7, -1, -3, -3])
```

We will see that, where basic indexing provides us with a *view* of the data within the array, without making a copy of it, advanced indexing requires that a copy of the accessed data be made. Here, we will define basic indexing and understand the nuances of working with views of arrays. The next section, then, is dedicated to understanding advanced indexing. 
<!-- #endregion -->

## Basic Indexing
We begin this subsection by defining precisely what basic indexing is. Next, we will touch on each component of this definition, and lastly we will delve into the significance of basic indexing in the way it permits us to reference the underlying data of an array without copying it.

<div class="alert alert-info"> 

**Definition: Basic Indexing**: 

Given an $N$-dimensional array, `x`, `x[index]` invokes **basic indexing** whenever `index` is a *tuple* containing any combination of the following types of objects:

- integers
- [slice](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/SequenceTypes.html#Slicing) objects
- [Ellipsis](https://docs.python.org/3/library/constants.html#Ellipsis) objects
- [numpy.newaxis](http://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/Broadcasting.html#Inserting-Size-1-Dimensions-into-An-Array) objects

Accessing the contents of an array via basic indexing *does not create a copy of those contents*. Rather, a "view" of the same underlying data is produced.
</div>


<!-- #region -->
### Indexing with Integers and Slice Objects
Our discussion of [accessing data along multiple dimensions of a NumPy array](http://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/AccessingDataAlongMultipleDimensions.html) already provided a comprehensive rundown on the use of integers and slices to access the contents of an array. According to the preceding definition, *these were all examples of basic indexing*.

To review the material discussed in that section, recall that one can access an individual element or a "subsection" of an $N$-dimensional array by specifying $N$ integers or slice-objects, or a combination of the two. We also saw that, when supplied fewer-than $N$ indices, NumPy will automatically "fill-in" the remaining indices with trailing slices. Keep in mind that the indices start at 0, such that the 4th column in `x` corresponds to column-3.

```python 
# Accessing the element located
# at row-1, last-column of `x`
>>> x[1, -1]
8

# Access the subarray of `x`
# contained within the first two rows
# and the first three columns
>>> x[:2, :3]
array([[-5,  2,  0],
       [-1,  9,  3]])

# NumPy fills in "trailing" slices
# if we don't supply as many indices
# as there are dimensions in that array
>>> x[0]  # equivalent to x[0, :]
array([-5,  2,  0, -7])
```

Recall that the familiar [slicing](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/SequenceTypes.html#Slicing) syntax actually forms `slice` objects "behind the scenes".

```python
# Reviewing the `slice` object

# equivalent: x[:2, :3]
>>> x[slice(None, 2), slice(None, 3)]
array([[-5,  2,  0],
       [-1,  9,  3]])
```
<!-- #endregion -->

### Using a Tuple as an N-dimensional Index
According to its definition, we must supply our array-indices as a tuple in order to invoke basic indexing. As it turns out, we have been forming tuples of indices all along! That is, every time that we index into an array using the syntax `x[i, j, k]`, we are actually forming a [tuple](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/SequenceTypes.html#Tuples) containing those indices. That is, `x[i, j, k]` is equivalent to `x[(i, j, k)]`.

`x[i, j, k]` forms the tuple `(i, j, k)` and passes that to the array's "get-item" mechanism. Thus, `x[0, 3]` is equivalent to `x[(0, 3)]`. 

<!-- #region -->
```python
# N-dimensional indexing utilizes tuples:
# `x[i, j, k]` is equivalent to `x[(i, j, k)]`

# equivalent: x[1, -1]
>>> x[(1, -1)]  
8

# equivalent: x[:2, :3]
>>> x[(slice(None, 2), slice(None, 3))]  
array([[-5,  2,  0],
       [-1,  9,  3]])

# equivalent: x[0]
>>> x[(0,)]
array([-5,  2,  0, -7])
```

All objects used in this "get-item" syntax are packed into a tuple. For instance, `x[0, (0, 1)]` is equivalent to `x[(0, (0, 1))]`. You may be surprised to find that this is a valid index. However, see that *it does not invoke basic indexing*; the index used here is a tuple that contains an integer *and another tuple*, which is not permitted by the rules of basic indexing.

Finally, note that the rules of basic indexing specifically call for a *tuple* of indices. Supplying a list of indices triggers advanced indexing rather than basic indexing!

```python
# basic indexing specifically requires a tuple
>>> x[(1, -1)]  
8

# indexing with a list triggers advanced indexing
>>> x[[1, -1]]
array([[-1,  9,  3,  8],
       [-3, -3,  4,  6]])
```
<!-- #endregion -->

<!-- #region -->
### Ellipsis and Newaxis objects
Recall from our discussion of broadcasting, that the `numpy.newaxis` object can be passed as an index to an array, in order to [insert a size-1 dimension into the array](http://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/Broadcasting.html#Inserting-Size-1-Dimensions-into-An-Array).

```python
# inserting size-1 dimensions with `np.newaxis`
>>> x.shape
(3, 4)

>>> x[np.newaxis, :, :, np.newaxis].shape
(1, 3, 4, 1)

# forming the index as an explicit tuple
>>> x[(np.newaxis, slice(None), slice(None), np.newaxis)].shape
(1, 3, 4, 1)
```

We can also use the built-in `Ellipsis` object in order to insert slices into our index such that the index has as many entries as the array has dimensions. In the same way that `:` can be used to represent a `slice` object, `...` can be used to represent an `Ellipsis` object.

```python
>>> y = np.array([[[ 0,  1,  2,  3],
...                [ 4,  5,  6,  7]],
...        
...               [[ 8,  9, 10, 11],
...                [12, 13, 14, 15]],
...        
...               [[16, 17, 18, 19],
...                [20, 21, 22, 23]]])

# equivalent: `y[:, :, 0]`
>>> y[..., 0]
array([[ 0,  4],
       [ 8, 12],
       [16, 20]])

# using an explicit tuple
>>> y[(Ellipsis, 0)]
array([[ 0,  4],
       [ 8, 12],
       [16, 20]])

# equivalent: `y[0, :, 1]`
>>> y[0, ..., 1]
array([1, 5])
```

An index cannot possess more than one `Ellipsis` entry. This can be extremely useful when working with arrays of varying dimensionalities. To access column-0 along all dimensions of an array, `z`, would look like `z[:, 0]` for a 2D array, `z[:, :, 0]` for a 3D array, and so on. `z[..., 0]` succinctly encapsulates all iterations of this. 
<!-- #endregion -->

<div class="alert alert-info"> 

**Takeaway:** 

Basic indexing is triggered whenever a tuple of: integer, `slice`, `numpy.newaxis`, and/or `Ellipsis` objects, is used as an index for a NumPy array. An array produced via basic indexing is a *view* of the same underlying data as the array that was indexed into; no data is copied through basic indexing. 

</div>


<div class="alert alert-info"> 


**Reading Comprehension: Ellipsis**

Given a $N$-dimensional array, `x`, index into `x` such that you axis entry-0 of axis-0, the last entry of axis-$N-1$, slicing along all intermediate dimensions. $N$ is at least $2$.

</div>


<div class="alert alert-info"> 

<!-- #region -->
**Reading Comprehension: Basic Indexing**

Given a shape-(4, 3) array,

```python
>>> arr = np.array([[ 0,  1,  2,  3],
...                 [ 4,  5,  6,  7],
...                 [ 8,  9, 10, 11]])
```

which of the following indexing schemes perform basic indexing? That is, in which instances does the index satisfy the rules of basic indexing?

 - `arr[0]`
 - `arr[:-1, 0]`
 - `arr[(2, 3)]`
 - `arr[[2, 0]]`
 - `arr[np.array([2, 0])]`
 - `arr[(0, 1), (2, 3)]`
 - `arr[slice(None), ...]`
 - `arr[(np.newaxis, 0, slice(1, 2), np.newaxis)]`

</div>
<!-- #endregion -->

<!-- #region -->
## Producing a View of an Array
As stated above, using basic indexing does not return a copy of the data being accessed, rather it produces a *view* of the underlying data. NumPy provides the function `numpy.shares_memory` to determine if two arrays refer to the same underlying data.

```python
>>> z = np.array([[ 3.31,  4.71,  0.4 ],
...               [ 0.21,  2.85,  3.21],
...               [-3.77,  4.53, -1.15]])

# `subarray` is column-0 of `z`, via
# basic indexing
>>> subarray = z[:, 0]
>>> subarray
array([ 3.31,  0.21, -3.77])

# `subarray` is a view of the array data 
# referenced by `z`
>>> np.shares_memory(subarray, z)
True
```

A single number returned by basic indexing *does not* share memory with the parent array.
```python
>>> z[0, 0]
3.31

>>> np.shares_memory(z[0, 0], z)
False
```
The function `numpy.copy` can be used to create a copy of an array, such that it no longer shares memory with any other array.

```python
# creating a distinct copy of an array
>>> new_subarray = np.copy(subarray)
>>> new_subarray
array([ 3.31,  0.21, -3.77])

>>> np.shares_memory(new_subarray, z)
False
```

Utilizing an array in a mathematical expression involving the arithmetic operators (`+, -, *, /, //, **`) returns an entirely distinct array, that does not share memory with the original array.

```python
# mathematical expressions like `subarray + 2`
# produce distinct arrays, not views
>>> np.shares_memory(subarray + 2, subarray)
False
```

Thus updating a variable `subarray` via `subarray = subarray + 2` does *not*  overwrite the original data referenced by `subarray`. Rather, `subarray + 2` assigns that new array to the variable `subarray`. NumPy does provide mechanisms for performing mathematical operations to directly update the underlying data of an array without having to create a distinct array. We will discuss these mechanisms in the next subsection.
<!-- #endregion -->

<div class="alert alert-info"> 

<!-- #region -->
**Reading Comprehension: Views**

Given, 

```python
x = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
```

Which of the following expressions create views of `x`? That is, in which cases do `x` and the created variable reference the same underlying array data? Check your work by using `np.shares_memory`.

- `a1 = x`
- `a2 = x[0, 0]`
- `a3 = x[:, 0]`
- `a4 = x[:, 0] + np.array([-1, -2, -3])`
- `a5 = np.copy(x[:, 0])`
- `a6 = x[np.newaxis]`
- `a7 = x.reshape(2, 3, 2)`
- `a8 = 2 + x`

</div>
<!-- #endregion -->

## Augmenting the Underlying Data of an Array 
Because basic indexing produces a *view* of an array's underlying data, we must take time to understand the ways in which we can *augment* that underlying data, versus performing operations that produce an array with distinct data. Here we will see that:

- in-place assignments 
- augmented assignments
- NumPy functions with the `out` argument 

can all be used to augment array data in-place. 

<!-- #region -->
### In-Place Assignments

The assignment operator, `=`, can be used to update an array's data in-place. Consider the array `a`, and its view `b`.
```python
>>> a = np.array([0, 1, 2, 3, 4])
>>> b = a[:]
>>> np.shares_memory(a, b)
True
```

Assigning a new array to `a` simply changes the data that `a` references, divorcing `a` and `b`, and leaving `b` unchanged.
```python
# `a` is now assigned to reference a distinct array 
>>> a = np.array([0, -1, -2, -3, -4])

# `b` still references the original data
>>> b
array([0, 1, 2, 3, 4])

>>> np.shares_memory(a, b)
False
```

Performing an assignment on a *view* of `a`, i.e. `a[:]`, instructs NumPy to perform the assignment to replace `a`'s data in-place. 

```python
# reinitialize `a` and `b`. 
# `b` is again a view of `a`
>>> a = np.array([0, 1, 2, 3, 4])
>>> b = a[:]

# assigning an array to a *view* of `a` 
# causes NumPy to update the data in-place
>>> a[:] = np.array([0, -1, -2, -3, -4])
>>> a
array([ 0, -1, -2, -3, -4])

# `b` a view of the same data, thus
# it is affected by this in-place assignment
>>> b
array([ 0, -1, -2, -3, -4])

>>> np.shares_memory(a, b)
True
```

This view-assignment mechanism can be used update a subsection of an array in-place.

```python
>>> p = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11]])
>>> q = p[0, :]

# Assign row-0, column-0 the value -40
# and row-0, column-2 the value -50
>>> p[0, ::2] = (-40, -50)

# broadcast-assign -1 to a subsection of `p`
>>> p[1:, 2:] = -1
>>> p
array([[-40,   1, -50,   3],
       [  4,   5,  -1,  -1],
       [  8,   9,  -1,  -1]])
```
Again, this updates the underlying data, and thus all views of this data reflect this change.
```python
# `q` is still a view of row-0 of `p`
>>> q
array([-40,   1, -50,   3])
```
<!-- #endregion -->

<!-- #region -->
### Augmented Assignments
Recall from our discussion of basic mathematical expressions in Python, that [augmented assignment expressions](http://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Augmented-Assignment-Statements) provide a nice shorthand notation for updating the value of a variable. For example, the assignment expression `x = x + 5` can be rewritten using the augmented assignment `x += 5`. 

While `x += 5` is truly only a shorthand in the context of basic Python objects (integers floats, etc.), *augmented assignments on NumPy arrays behave fundamentally different than their long-form counterparts*. Specifically, they directly update the underlying data referenced by the updated array, rather than creating a distinct array, thus affecting any arrays that are views of that data. We will demonstrate this here.

```python
# Demonstrating that augmented assignments on NumPy
# arrays update the underlying data reference by that
# array.
>>> a = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11]])

# `b` and `c` are both views of row-0 of `a`, via basic indexing
>>> b = a[0]
>>> c = a[0]
>>> np.shares_memory(a, b) and np.shares_memory(a, c)
True

# updating `b` using a mathematical expression creates
# a distinct array, which is divorced from `a` and `c`
>>> b = b * -1
>>> b
array([ 0, -1, -2, -3])

>>> np.shares_memory(a, b)
False

# updating `c` using augmented assignment updates the 
# underlying data that `c` is a view of
>>> c *= -2
>>> c
array([ 0, -2, -4, -6])

>>> np.shares_memory(a, c)
True

# note that this update is reflected in `a` as well,
# as it still shares memory with `c`
>>> a
array([[ 0, -2, -4, -6],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```
<!-- #endregion -->

<!-- #region -->
### Specifying `out` to Perform NumPy Operations In-Place 
There is no reason why we should only be able to augment data using arithmetic operations. Indeed, [NumPy's various mathematical functions](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html#NumPy%E2%80%99s-Mathematical-Functions) have an optional keyword argument, `out`, which can be used to specify where to "store" the result of the mathematical operation. By default, the operation will create a distinct array in memory, leaving the input data unaffected.

```python
# Specifying the 'out' argument in a `numpy.exp` 
# to augment the data of an array

# `b` is a view of `a`
>>> a = np.array([0., 0.2, 0.4, 0.6, 0.8, 1.])
>>> b = a[:]
>>> np.shares_memory(a, b)
True

# specifying 'out=a' instructs NumPy
# to overwrite the data referenced by `a`
>>> np.exp(a, out=a)
array([ 1., 1.22140276, 1.4918247, 1.8221188, 2.22554093, 2.71828183])

# `b` is still a view of the now-augmented data
>>> b
array([ 1., 1.22140276, 1.4918247, 1.8221188, 2.22554093, 2.71828183])
```

<!-- #endregion -->

<!-- #region -->
### Benefits and Risks of Augmenting Data In-Place
It is critical to understand the relationship between arrays and the underlying data that they reference. *Operations that augment data in-place are more efficient than their counterparts that must allocate memory for a new array.* That is, an expression like `array += 3` is more efficient than `array = array + 3`. 

That being said, to *unwittingly* augment the data of an array, and thus affect all views of that data, is a big mistake; this produces hard-to-find bugs in the code of novice NumPy users. See that the following function, `add_3`, will change the data of the input array.

```python
# updating an array in-place within a function
def add_3(x):
    x += 3 
    return x

>>> x = np.array([0, 1, 2])
>>> y = add_3(x)
>>> y
array([3, 4, 5])

# `x` is updated each time `f(x)` is called
>>> x
array([3, 4, 5])
```

This is hugely problematic unless you intended for `add_3` to affect the input array. To remedy this, you can simply begin the function by making a copy of the input array; afterwards you can freely augment this copied data.
```python
def add_3(x):
    x = np.copy(x)
    x += 3 
    return x
```
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Augmenting Array Data In-Place**

Given, 

```python
x = np.array([[ 0.,  1.,  2.,  3.],
              [ 4.,  5.,  6.,  7.],
              [ 8.,  9., 10., 11.]])

y = x[0, :]
```

Which of the following expressions updates the data originally referenced by `x`?

```python 
# 1.
>>> x += 3
```

```python 
# 2.
>>> y *= 2.4
```

```python 
# 3.
>>> x = x + 3
```

```python 
# 4.
>>> y = np.copy(y)
>>> y += 3
```

```python 
# 5.
>>> np.log(x[1:3], out=x[1:3])
>>> y += 3
```

```python 
# 6.
>>> y[:] = y + 2
```

```python 
# 7.
>>> y = y + 2
```

```python 
# 8.
>>> x[:] = 0
```

```python 
# 9.
>>> def f(z): z /= 3
>>> f(y)
```

</div>
<!-- #endregion -->

<div class="alert alert-info"> 

**Takeaway:** 

Assignments to views of an array, augmented assignments, and NumPy functions that provide an `out` argument, are all methods for augmenting the data of an array in-place. This will affect any arrays that are views of that data. Furthermore, these in-place operations are more efficient than their counterparts that allocate memory for a new array. That being said, in-place data augmentation must not be used haphazardly, for this will inevitably lead to treacherous bugs in one's code.

</div>


## Links to Official Documentation

- [Basic indexing](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#indexing)
- [Definition of 'view'](https://docs.scipy.org/doc/numpy/glossary.html#term-view)


## Reading Comprehension Solutions


**Ellipsis: Solution**

Given a $N$-dimensional array, `x`, index into `x` such that you axis entry-0 of axis-0, the last entry of axis-$(N-1)$, slicing along all intermediate dimensions. $N$ is at least $2$.

Using an `Ellipsis` object in the index allows us to signal NumPy to insert the slices along the $N - 2$ intermediate axis of `x`:

`x[0, ..., -1]` or `x[0, Ellipsis, -1]`


**Basic Indexing: Solution**

In which instances does the index used satisfy the rules of basic indexing?

 - `arr[0]` ✔
 - `arr[:-1, 0]`  ✔
 - `arr[(2, 3)]`  ✔
 - `arr[[2, 0]]`  ✘ (index is a `list`, not a `tuple`)
 - `arr[np.array([2, 0])]` ✘ (index is a `numpy.ndarray`, not a `tuple`)
 - `arr[:, (2, 3)]`  ✘ (index contains a tuple; only `int`, `slice`, `np.newaxis`, `Ellipsis` allowed)
 - `arr[slice(None), ...]`  ✔
 - `arr[(np.newaxis, 0, slice(1, 2), np.newaxis)]`  ✔

<!-- #region -->
**Views: Solution**

Given, 

```python
x = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
```

Which of the following expressions create views `x`? That is, in which cases do `x` and the created variable reference the same underlying array data? Check your work by using `np.shares_memory`.

- `a1 = x` ✔
- `a2 = x[0, 0]` ✘; when basic indexing returns a single number, that number does not share memory with the parent array.
- `a3 = x[:, 0]` ✔
- `a4 = x[:, 0] + np.array([-1, -2, -3])` ✘; arithmetic operations on NumPy arrays create distinct arrays by default.
- `a5 = np.copy(x[:, 0])` ✘; `numpy.copy` informs NumPy to create a distinct copy of an array.
- `a6 = x[np.newaxis]` ✔
- `a7 = x.reshape(2, 3, 2)` ✔
- `a8 = 2 + x` ✘; arithmetic operations on NumPy arrays create distinct arrays by default.
<!-- #endregion -->

<!-- #region -->
**Augmenting Array Data In-Place: Solution**

Given, 

```python
x = np.array([[ 0.,  1.,  2.,  3.],
              [ 4.,  5.,  6.,  7.],
              [ 8.,  9., 10., 11.]])

y = x[0, :]
```

Which of the following expressions updates the data originally referenced by `x`?

```python 
# 1.
>>> x += 3 ✔
```

```python 
# 2.
>>> y *= 2.4 ✔
```

```python 
# 3.
>>> x = x + 3 ✘
```

```python 
# 4.
>>> y = np.copy(y)
>>> y += 3 ✘
```

```python 
# 5.
>>> np.log(x[1:3], out=x[1:3]) ✔
```

```python 
# 6.
>>> y[:] = y + 2 ✔
```

```python 
# 7.
>>> x = np.square(x) ✘
```

```python 
# 8.
>>> x[:] = 0 ✔
```

```python 
# 9.
>>> def f(z): z /= 3
>>> f(y) ✔
```

```python 
# 10.
>>> np.square(y, out=y) ✔
```
<!-- #endregion -->
