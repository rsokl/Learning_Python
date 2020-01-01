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
   :description: Topic: Numpy array attributes, Difficulty: Easy, Category: Section
   :keywords: ndim, shape, size, itemsize, dtype, examples
<!-- #endraw -->

<!-- #region -->
# Basic Array Attributes
Armed with our understanding of multidimensional NumPy arrays, we now look at methods for programmatically inspecting an array's attributes (e.g. its dimensionality). It is especially important to understand what an array's "shape" is.

We will use the following array to provide context for our discussion:
 
```python
>>> import numpy as np
>>> example_array = np.array([[[ 0,  1,  2,  3],
...                            [ 4,  5,  6,  7]],
...
...                           [[ 8,  9, 10, 11],
...                            [12, 13, 14, 15]],
...
...                           [[16, 17, 18, 19],
...                            [20, 21, 22, 23]]])
```
According to the preceding discussion, it is a 3-dimensional array structured such that:

 - axis-0 discerns which of the  **3 sheets** to select from.
 - axis-1 discerns which of the **2 rows**, in any sheet, to select from.
 - axis-2 discerns which of the **4 columns**, in any sheet and row, to select from.

**ndarray.ndim**: 

The number of axes (dimensions) of the array.

```python
# dimensionality of the array
>>> example_array.ndim
3
```
<!-- #endregion -->

<!-- #region -->
**ndarray.shape**:

A tuple of integers indicating the number of elements that are stored along each dimension of the array. For a 2D-array with $N$ rows and $M$ columns, shape will be $(N, M)$. The length of this shape-tuple is therefore equal to the number of dimensions of the array.

```python
# shape of the array
>>> example_array.shape
(3, 2, 4)
```

**ndarray.size**:

The total number of elements of the array. This is equal to the product of the elements of the array's shape.
```python
# size of the array: the number of elements it stores
>>> example_array.size
24
```

**ndarray.dtype**:

An object describing the data type of the elements in the array. Recall that NumPy's ND-arrays are *homogeneous*: they can only posses numbers of a uniform data type. 

```python
# `example_array` contains integers, each of which are stored using 32 bits of memory
>>> example_array.dtype
dtype('int32') 
```

**ndarray.itemsize**:

The size, in bytes (8 bits is 1 byte), of each element of the array. For example, an array of elements of type `float64` has itemsize 8 $(= \frac{64}{8})$, while an array of type `complex32` has itemsize 4 $(= \frac{32}{8})$.
```python
# each integer in `example_array` is represented using 4 bytes (32 bits) of memory
>>> example_array.itemsize
4
```
<!-- #endregion -->

## Links to Official Documentation

- [Array attributes](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html#array-attributes)
