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
   :description: Topic: Introduction to numpy arrays, Difficulty: Easy, Category: Section
   :keywords: numpy array, ndarray, introduction, overview
<!-- #endraw -->

<!-- #region -->
# Introducing the ND-array
It is time to start familiarizing ourselves with NumPy, the premiere library for doing numerical work in Python. To use this package, we need to be sure to "import" the NumPy module into our code:

```python
import numpy as np
```

You could have run `import numpy` instead, but the prescribed method allows us to use the abbreviation 'np' throughout our code, instead of having to write 'numpy'. This is a very common  abbreviation to use.

The ND-array (N-dimensional array) is the star of the show for NumPy. This array simply stores a sequence of numbers. Like a Python list, you can access individual entries in this array by "indexing" into the array, and you can access a sub-sequence of the array by "slicing" it. So what distinguishes NumPy's ND-array from a Python list, and why is there a whole numerical library that revolves around this array? There are two major features that makes the ND-array special. It can:

 1. Provide an interface for its underlying data to be accessed along multiple dimensions.
 2. Rapidly perform mathematical operations over all of its elements, or over patterned subsequences of its elements, using compiled C code instead of Python; this is a process called vectorization.
 
Let's take a sneak peek to see what this module has in store. The following code creates an ND-array containing the numbers 0-8:

```python
>>> import numpy as np
>>> x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
```

This object belongs to the NumPy-defined type `numpy.ndarray`.

```python
# An ND-array belongs to the type `numpy.ndarray`
>>> type(x)
numpy.ndarray

>>> isinstance(x, np.ndarray)
True
```
<!-- #endregion -->

<!-- #region -->
We can "reshape" this array so that its contents can be accessed along 2 dimensions:
```python
>>> x = x.reshape(3,3)
>>> x
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
```

We will utilize one of NumPy's "vectorized" functions to square each entry in the array (without us needing to write a for-loop) 
```python
>>> np.power(x, 2)  # can also be calculated using the shorthand: x**2
array([[ 0,  1,  4],
       [ 9, 16, 25],
       [36, 49, 64]], dtype=int32)
```

Let's take the mean value along the three distinct rows of our data:
```python
>>> np.mean(x, axis=1)
array([ 1.,  4.,  7.])
```

We can use broadcasting to raise each column of `x` to a different power:
```python
>>> x ** np.array([0., 1., 2.])
array([[  1.,   1.,   4.],
       [  1.,   4.,  25.],
       [  1.,   7.,  64.]])
```

Basic indexing allows us to access multi-dimensional slices of `x`:
```python
>>> x[:2, :3]
array([[0, 1, 2],
       [3, 4, 5]])
```

Advanced indexing can be used to access all even-valued entries of `x`; let's update `x` so that all of its even-valued entries are multiplied by -1:

```python
>>> x[x % 2 == 0] *= -1
>>> x
array([[ 0,  1, -2],
       [ 3, -4,  5],
       [-6,  7, -8]])
```

By the end of this module, these code snippets should make good sense, and NumPy's tremendous utility should be clear.
<!-- #endregion -->

## Links to Official Documentation

- [The N-dimensional array](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html)
- [NumPy Basics](https://docs.scipy.org/doc/numpy/user/basics.html#numpy-basics)
- [NumPy reference](https://docs.scipy.org/doc/numpy/reference/index.html)
