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
   :description: Topic: Advanced indexing with numpy arrays, Difficulty: Hard, Category: Section
   :keywords: numpy array, integer array indexing, boolean array indexing, copy indexing, advanced
<!-- #endraw -->

<!-- #region -->
# Advanced Indexing

We conclude our discussion of indexing into N-dimensional NumPy arrays by understanding advanced indexing. Unlike basic indexing, which allows us to access distinct elements and regular slices of an array, advanced indexing is significantly more flexible. For example, arrays of integers can be used to access arbitrary and even repeated entries from an array,

```python
>>> import numpy as np

>>> x = np.array([[0, 1, 2],
...               [3, 4, 5],
...               [6, 7, 8]])

# Construct the following 2D array
# from the contents of `x`:
#
#     [[x[0, 0], x[0, 1]],
#      [x[2, 2], x[2, 2]]]
>>> rows = np.array([[0, 0], 
...                  [2, 2]])

>>> cols = np.array([[0, 1], 
...                  [2, 2]])

>>> x[rows, cols]
array([[0, 1],
       [8, 8]])
```

Additionally, it permits the use of *boolean-valued* arrays as indices, 

```python
# Use a boolean-valued array to access
# the diagonal values of an array

# Specify `True` wherever we want to access 
# the entry of `x`
>>> bool_index = np.array([[ True, False, False],
...                        [False,  True, False],
...                        [False, False,  True]])

>>> x[bool_index]
array([0, 4, 8])
```

Unlike basic indexing, advanced indexing always produces a copy of the underlying data.
```python
>>> np.shares_memory(x, x[rows, cols])
False

>>> np.shares_memory(x, x[bool_index])
False
```
The flexibility permitted by advanced indexing makes it a difficult topic to treat exhaustively without delving into somewhat terse and abstract notation. It is best to refer to [the official documentation](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#advanced-indexing) for such a treatment of the topic. Here, we will discuss the essential aspects of advanced indexing, with the aim of the discussion being  both thorough and accessible.
<!-- #endregion -->

<div class="alert alert-info"> 

**Advanced Indexing**: 

Given an $N$-dimensional array, `x`, `x[index]` invokes **advanced indexing** whenever `index` is:

- an integer-type or boolean-type `numpy.ndarray`
- a `tuple` with at least one *sequence*-type object as an element (e.g. a list, tuple, or ndarray)

Accessing the contents of an array via advanced indexing *always returns a copy of those contents*, whereas basic indexing returns a view.

</div>

<!-- #region -->
## Integer Array Indexing

### Indexing into 1-Dimensional Arrays
Using an integer-type array as an index allows us to access the contents of an array arbitrarily, permitting items to be accessed out of order, and even repeatedly. Consider the following 1-dimensional array.

```python
y = np.array([ 0, -1, -2, -3, -4, -5])
```

See that we can access an arbitrary number of the array's contents in an unpatterned way, which is not permissible via basic index:

```python
# advanced indexing with an integer-array
>>> index = np.array([2, 4, 0, 4, 4, 4])
>>> y[index]
array([-2, -4,  0, -4, -4, -4])
```

<!-- #endregion -->

The instruction for accessing the contents of `y` in this way is straight-forward to interpret. Each entry of the index-array is used to access an element from `y`, as illustrated here:


\begin{equation}
\left(
\begin{array}{*{6}{X}}
  y[2] & y[4] & y[0] & y[4] & y[4] & y[4]
\end{array}
\right)
% 
\rightarrow
\left(
\begin{array}{*{6}{X}}
  -2 & -4 & 0 & -4 & -4 & -4
\end{array}
\right)
\end{equation}


This returns a *copy* of the data, as do all occurrences of advanced indexing.

<!-- #region -->
```python
# advanced indexing returns a copy
>>> np.shares_memory(y, y[index])
False
```
<!-- #endregion -->

<!-- #region -->
The indexing array can have an arbitrary shape; *the resulting array will match that shape*.

```python
# utilizing a 2D-array as an index
>>> index_2d = np.array([[ 1,  2,  0],
...                      [ 5,  5,  5],
...                      [ 2,  3,  4]])

# the resulting shape matches the shape of the indexing array
>>> y[index_2d]
array([[-1, -2,  0],
       [-5, -5, -5],
       [-2, -3, -4]])
```
<!-- #endregion -->

\begin{equation}
\left(
\begin{array}{*{3}{X}}
  y[1] & y[2] & y[0] \\
  y[5] & y[5] & y[5] \\
  y[2] & y[3] & y[4]
\end{array}
\right)
% 
\rightarrow
\left(
\begin{array}{*{3}{X}}
  -1 & -2 & 0 \\
  -5 & -5 & -5 \\
  -2 & -3 & -4
\end{array}
\right)
\end{equation}

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Integer Array Indexing (1-D)**

Given the following array:

```python
y = np.array([ 0, -1, -2, -3, -4, -5])
```

Use advanced indexing, using an integer-array, to produce the following arrays:

```python
# 1
array([-1])

#2
array([-1, -2, -1, -2])

#3
array([[ 0, -5],
       [-1, -4]])

#4
array([[-2],
       [-3],
       [-2]])
```

</div>
<!-- #endregion -->

<!-- #region -->
### Indexing into N-Dimensional Arrays

In the preceding examples, working with a 1-dimensional array, we specified a single index-array to access the contents along the only dimension of that array. As you may guess, in order to perform this variety of indexing on an $N$-dimensional array, we must specify $N$ index-arrays; one for each dimension. 

Each of the $N$ index-arrays must have the same shape, and their common shape determines the shape of the resulting array. The corresponding entries of each of the $N$ index-arrays are used to specify a specific array element to be accessed. For example, consider the following 3-dimensional array whose elements we will be accessing:

```python
# Indexing a 3D array using integer index-arrays
>>> z = np.array([[[ 0,  1,  2,  3],
...                [ 4,  5,  6,  7],
...                [ 8,  9, 10, 11]],
...
...               [[12, 13, 14, 15],
...                [16, 17, 18, 19],
...                [20, 21, 22, 23]]])
```

We specify three index-arrays; the indices to be accessed along axis-0, axis-1, and axis-2, respectively. Suppose we want to produce the array: `array([ 3, 23,  4])`. The layout of these elements is as follows:

- `3`: sheet-0, row-0, column-3
- `23`: sheet-1, row-2, column-3
- `4`: sheet-0, row-1, column-0

Each index-array must have a shape (3,) in order to produce the result of the appropriate shape. The index-array supplied for axis-0 must be `np.array([0, 1, 0])` in order to select sheet-0 for `3`, sheet-1 for `23`, and then sheet-0 for `4`. The other index-arrays are formed similarly. 

```python
# specifies subsequent sheets to access
>>> ind0 = np.array([0, 1, 0])

# specifies subsequent rows to access
>>> ind1 = np.array([0, 2, 1])

# specifies subsequent columns to access
>>> ind2 = np.array([3, 3, 0])

>>> z[ind0, ind1, ind2]
array([ 3, 23,  4])
```
<!-- #endregion -->

Formally, the index-arrays are traversed simultaneously using [row-major ordering](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/ArrayTraversal.html), and each combination of integer-indices is used to index into `z` and populate the corresponding element in the resulting array.


\begin{equation}
   z\big[ind_0[0], ind_1[0], ind_2[0]\big]
% 
\rightarrow
out[0] \\
   z\big[ind_0[1], ind_1[1], ind_2[1]\big]
% 
\rightarrow
out[1] \\
   z\big[ind_0[2], ind_1[2], ind_2[2]\big] 
% 
\rightarrow
out[2] \\
\end{equation}

\begin{equation}
\left(
\begin{array}{*{3}{X}}
   z[0, 0, 3] & z[1, 2, 3] & z[0, 1, 0] 
\end{array}
\right)
% 
\rightarrow
\left(
\begin{array}{*{3}{X}}
  3 & 23 & 4
\end{array}
\right)
\end{equation}

<!-- #region -->
```python
# Using integer index-arrays to produce a shape(2, 2) result
>>> ind0 = np.array([1, 1, 0, 1]).reshape(2, 2)
>>> ind1 = np.array([1, 2, 0, 0]).reshape(2, 2)
>>> ind2 = np.array([1, 3, 1, 3]).reshape(2, 2)
>>> z[ind0, ind1, ind2]
array([[17, 23],
       [ 1, 15]])
```

\begin{equation}
\left(
\begin{array}{*{3}{X}}
  z[1, 1, 1] & z[1, 2, 3] \\
  z[0, 0, 1] & z[1, 0, 3]
\end{array}
\right)
% 
\rightarrow
\left(
\begin{array}{*{3}{X}}
  17 & 23 \\
  1 & 15 
\end{array}
\right)
\end{equation}
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Integer Array Indexing (N-D)**

Given the following array:

```python
>>> z = np.array([[[ 0,  1,  2,  3],
...                [ 4,  5,  6,  7],
...                [ 8,  9, 10, 11]],
...
...               [[12, 13, 14, 15],
...                [16, 17, 18, 19],
...                [20, 21, 22, 23]]])
```

Use advanced indexing, using integer-arrays, to produce the following arrays:

```python
# 1
array([[ 0,  5, 10],
       [12, 17, 22]])

#2
array([[ 0, 23],
       [23,  0]])

```

</div>
<!-- #endregion -->

<div class="alert alert-info"> 

**Takeaway:**

An $N$-dimensional array's contents can be accessed by supplying $N$ index-arrays of integers; one for each axis of data. The index-arrays must have the same shape as one another, and this common shape determines the shape of the resulting array. This is a form of advanced indexing, and thus a copy of the parent array's data is created.

</div>

<!-- #region -->
## Boolean-Array Indexing
NumPy also permits the use of a boolean-valued array as an index, to perform advanced indexing on an array. In its simplest form, this is an extremely intuitive and elegant method for selecting contents from an array based on logical conditions.

```python
# advanced indexing using a boolean-array
>>> x = np.array([[[-0.26,  0.49,  0.18],
...                [ 0.43,  0.3 ,  0.29]],
...        
...               [[-0.44,  0.3 ,  0.28],
...                [ 0.27, -0.09, -0.13]]])

# `True` wherever `x` is positive
>>> bool_ind = x > 0
>>> bool_ind
array([[[False,  True,  True],
        [ True,  True,  True]],

       [[False,  True,  True],
        [ True, False, False]]], dtype=bool)

>>> x[bool_ind]
array([ 0.49,  0.18,  0.43,  0.3 ,  0.29,  0.3 ,  0.28,  0.27])

>>> np.shares_memory(x, x[bool_ind])
False
```
In its simplest form, boolean indexing behaves as follows: Suppose `x` is an $N$-dimensional array, and `ind` is a boolean-value  array *of the same shape as* `x`. Then `x[ind]` returns a 1-dimensional array, which is formed by traversing `x` and `ind` using [row-major ordering](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/ArrayTraversal.html). Wherever an element of `ind` is `True`, the corresponding entry of `x` is added to the end of the resulting array. Refer to the preceding example and convince yourself that this is the behavior that is exhibited.
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Boolean Indexing**

Given the following array:

```python
>>> h = np.array([[ 0.01,  0.03,  0.1 ,  0.25],
...               [ 0.38,  0.22,  0.15,  0.34],
...               [-0.29,  0.13, -0.26,  0.33]])
```

Use boolean array-indexing and NumPy's [logical functions](https://docs.scipy.org/doc/numpy/reference/routines.logic.html) to select the contents of `h` that satisfy the following conditions. Because you are dealing with floating-point numbers, [you should not require that two values are exactly equal](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html#Understanding-Numerical-Precision); rather, make use of the function [numpy.isclose](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.isclose.html).

1. All negative entries in `h`
2. All entries in `h` "equal" to `0.01` or `0.33`
3. All entries of `h` that fall within the domain `(0.1, 0.3) 

</div>
<!-- #endregion -->

<!-- #region -->
#### Converting a Boolean Index-Array to Integer index-arrays: numpy.where
The function [numpy.where](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html) can be used to take a boolean-valued array, and produce the *tuple* of index-arrays that access the `True` entries of that array, via integer array indexing (discussed at the beginning of this section).

```python
# demonstrating `np.where`
>>> bool_ind
array([[[False,  True,  True],
        [ True,  True,  True]],

       [[False,  True,  True],
        [ True, False, False]]], dtype=bool)

>>> np.where(bool_ind)
(array([0, 0, 0, 0, 0, 1, 1, 1], dtype=int64),
 array([0, 0, 1, 1, 1, 0, 0, 1], dtype=int64),
 array([1, 2, 0, 1, 2, 1, 2, 0], dtype=int64))
```

In this example, a tuple of three integer-valued index-arrays are returned, one for each dimension of `bool_ind`. See that index-arrays indicate the `True` entries of `bool_ind`. Furthermore, recall that `bool_ind` was created to access the positive entries of `x`; the tuple of index-arrays can thus be used to the exact same end.

```python
>>> ind0, ind1, ind2 = np.where(bool_ind)
>>> x[ind0, ind1, ind2]
array([ 0.49,  0.18,  0.43,  0.3 ,  0.29,  0.3 ,  0.28,  0.27])

# unpacking the arrays is not necessary, you can
# use the tuple as an index
>>> x[np.where(bool_ind)]
array([ 0.49,  0.18,  0.43,  0.3 ,  0.29,  0.3 ,  0.28,  0.27])
```

`np.where` is particularly useful when we want insight into *where* specific conditions are met within an array. Suppose, for instance, we want to know which sheets in `x` contain values greater than 0.4:

```python
# which sheets in `x` contain a value
# greater than 0.4?

>>> ind0, ind1, ind2 = np.where(x > 0.4)

# get rid of redundant answers
>>> np.unique(ind0)
array([0], dtype=int64)

# only sheet-0 contains such values
```
<!-- #endregion -->

Armed with NumPy's suite of [logical functions](https://docs.scipy.org/doc/numpy/reference/routines.logic.html), boolean-array indexing provides a sleek interface for accessing the particular contents of an array, irrespective of the array's shape and the layout of its contents. This method of indexing is especially powerful in the context of performing augmented updates to an array, which is the subject of the following subsection.

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: numpy.where**

Given the array 

```python
>>> b = np.array([[False, False,  True],
...               [False,  True, False],
...               [ True,  True, False]], dtype=bool)
```

*Predict* what the output of `np.where(b)` is. 
</div>
<!-- #endregion -->

<!-- #region -->
## In-Place & Augmented Assignments via Advanced Indexing

Although advanced indexing does not produce a [*view* of the underlying data](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/BasicIndexing.html#Producing-a-View-of-an-Array), it can still be used to facilitate in-place and augmented assignments to regions of an array. Suppose, for instance, that you want to threshold the contents of an array such that all of its negative-valued entries are replaced with 0. Boolean indexing makes this task trivial to perform via in-place assignment:

```python
# assignment via advanced indexing
>>> x = np.array([[ 0.38, -0.16,  0.38, -0.41, -0.04],
...               [-0.47, -0.01, -0.18, -0.5 , -0.49],
...               [ 0.02,  0.4 ,  0.33,  0.33, -0.13]])

# set all negative entries of `x` to 0 (broadcasting is used)
>>> x[x < 0] = 0
>>> x
array([[ 0.38,  0.  ,  0.38,  0.  ,  0.  ],
       [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ],
       [ 0.02,  0.4 ,  0.33,  0.33,  0.  ]])
```

We also demonstrate the use of integer-valued index-arrays to perform an augmented assignment.
```python
# augmented assignment via integer-arrays
>>> ind0 = np.array([0, -1])
>>> ind1 = np.array([0, 1])
>>> x[ind0, ind1]
array([ 0.38, 0.4])

# equivalent: x[ 0, 0] *= 100
#             x[-1, 1] *= 100
>>> x[ind0, ind1] *= 100

>>> x
array([[  38.,   0. , 0.38 ,   0.,  0.  ],
       [   0.,   0. ,    0.,   0.,  0.  ],
       [ 0.02,  40. , 0.33,  0.33,  0.  ]])
```
<!-- #endregion -->

<!-- #region -->
Recall that redundant entries in an array can be specified via integer array indexing. An augmented assignment *will only be performed once on redundant entries*.  

```python
>>> y = np.array([4, 6, 8])

# y[0] is accessed three times and y[2] one time
>>> y[np.array([0, 0, 0, 2])]
array([4, 4, 4, 8])

# the augmented update is only applied once to y[0]
>>> y[np.array([0, 0, 0, 2])] += 1
>>> y
array([5, 6, 9])
```
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Assignment via advanced indexing**

Given the array 

```python
>>> x = np.array([[ 0.58,  0.05,  0.84,  0.21],
...               [ 0.88,  0.98,  0.45,  0.13],
...               [ 0.1 ,  0.52,  0.58,  0.38],
...               [ 0.84,  0.76,  0.25,  0.07]])
```

Replace the diagonal elements of `x` with `(-1, -2, -3, -4)`, and add `1` to all values in `x` that are greater than `0.8`.
</div>
<!-- #endregion -->

<!-- #region -->
## Combining Basic and Advanced Indexing Schemes
Integer- and boolean-valued arrays can be used in conjunction with `slice`, `numpy.newaxis`, and `int` objects to form indices that combine basic and advanced indexing schemes. 

```python
# combining advanced and basic indexing techniques
>>> z = np.array([[[ 0,  1,  2,  3],
...                [ 4,  5,  6,  7],
...                [ 8,  9, 10, 11]],
...
...               [[12, 13, 14, 15],
...                [16, 17, 18, 19],
...                [20, 21, 22, 23]]])

>>> ind0 = np.array([True, False])

# select sheet-0, all rows, last column
>>> z[ind0, :, -1]
array([[ 3,  7, 11]])
```
<!-- #endregion -->

The rules for resolving the various possible combinations of basic and advanced indexing are nontrivial. Refer to the [official NumPy documentation](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#combining-advanced-and-basic-indexing) for a detailed description for these rules. In practice, basic and advanced indexing can typically be used independently from one another.


## Links to Official Documentation

- [Advanced Indexing](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#advanced-indexing)
- [Logical Functions](https://docs.scipy.org/doc/numpy/reference/routines.logic.html)
- [numpy.where](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html)
- [Combining Basics and Advanced Indexing](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#combining-advanced-and-basic-indexing)


## Reading Comprehension Solutions

<!-- #region -->
**Integer Array Indexing (1-D): Solution**

```python
y = np.array([ 0, -1, -2, -3, -4, -5])
```

```python
# 1
>>> ind1 = np.array([1])
>>> y[ind1]
array([-1])

#2
>>> ind2 = np.array([1, 2, 1, 2])
>>> y[ind2]
array([-1, -2, -1, -2])

#3
>>> ind3 = np.array([[0, 5],
...                  [1, 4]])
>>> y[ind3]
array([[ 0, -5],
       [-1, -4]])

#4
>>> ind4 = np.array([[2],
...                  [3],
...                  [2]])
>>> y[ind4]
array([[-2],
       [-3],
       [-2]])
```
<!-- #endregion -->

<!-- #region -->
**Integer Array Indexing (N-D): Solution**

```python
>>> z = np.array([[[ 0,  1,  2,  3],
...                [ 4,  5,  6,  7],
...                [ 8,  9, 10, 11]],
...
...               [[12, 13, 14, 15],
...                [16, 17, 18, 19],
...                [20, 21, 22, 23]]])
```

```python
# 1
>>> ind0 = np.array([0, 0, 0, 1, 1, 1]).reshape(2, 3)
>>> ind1 = np.array([0, 1, 2, 0, 1, 2]).reshape(2, 3)
>>> ind2 = np.array([0, 1, 2, 0, 1, 2]).reshape(2, 3)
>>> z[ind0, ind1, ind2]
array([[ 0,  5, 10],
       [12, 17, 22]])

# 2
>>> ind0 = np.array([0, 1, 1, 0]).reshape(2, 2)
>>> ind1 = np.array([0, 2, 2, 0]).reshape(2, 2)
>>> ind2 = np.array([0, 3, 3, 0]).reshape(2, 2)
>>> z[ind0, ind1, ind2]
array([[ 0, 23],
       [23,  0]])
```
<!-- #endregion -->

<!-- #region -->
**Boolean Indexing: Solution**

```python
>>> h = np.array([[ 0.01,  0.03,  0.1 ,  0.25],
...               [ 0.38,  0.22,  0.15,  0.34],
...               [-0.29,  0.13, -0.26,  0.33]])

# 1
>>> h[h < 0]
array([-0.29, -0.26])

# 2
>>> h[np.logical_or(np.isclose(h, 0.01), np.isclose(h, 0.33))]
array([ 0.01,  0.33])

>>> h[np.logical_and(0.1 < h, h < 0.3)]
array([ 0.25,  0.22,  0.15,  0.13])
```
<!-- #endregion -->

<!-- #region -->
**numpy.where: Solution**

Given the array 

```python
>>> b = np.array([[False, False,  True],
...               [False,  True, False],
...               [ True,  True, False]], dtype=bool)
```

*Predict* what the output of `np.where(b)` is. 

This will return a tuple of two integer-valued index-arrays. These contain the indices, along axis-0 and axis-1 respectively, where `b` contains the value `True`. The indices are ordered by traversing `b` in row-major order. It returns:

```python
(array([0, 1, 2, 2], array([2, 1, 0, 1])
```
<!-- #endregion -->

<!-- #region -->
**Assignment via advanced indexing**

```python
>>> x = np.array([[ 0.58,  0.05,  0.84,  0.21],
...               [ 0.88,  0.98,  0.45,  0.13],
...               [ 0.1 ,  0.52,  0.58,  0.38],
...               [ 0.84,  0.76,  0.25,  0.07]])

>>> x[np.arange(4), np.arange(4)] = range(4)
>>> x[0.8 < x] += 1
>>> x
array([[ 0.  ,  0.05,  1.84,  0.21],
       [ 1.88,  2.  ,  0.45,  0.13],
       [ 0.1 ,  0.52,  3.  ,  0.38],
       [ 1.84,  0.76,  0.25,  4.  ]])
```
<!-- #endregion -->
