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
   :description: Topic: Creating numpy arrays, Difficulty: Easy, Category: Section
   :keywords: create array, ndarray, ones, random, zeros, empty, examples, arange, linspace, reshape, hstack, vstack
<!-- #endraw -->

<!-- #region -->
# Functions for Creating NumPy Arrays 
This section presents standard methods for creating NumPy arrays of varying shapes and contents. NumPy provides a laundry list of functions for creating arrays:

```python
>>> import numpy as np

# creating an array from a Python sequence
>>> np.array([i**2 for i in range(5)])
array([ 0,  1,  4,  9, 16])

# creating an array filled with ones
>>> np.ones((2, 4))
array([[ 1.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.]])

# creating an array of evenly-spaced points
>>> np.linspace(0, 10, 5)
array([  0. ,   2.5,   5. ,   7.5,  10. ])

# creating an array by sampling 10 numbers 
# randomly from a mean-1, std-dev-5 normal
# distribution
>>> np.random.normal(1, 5, 10)
array([ 2.549537  ,  2.75144951,  0.60031823,  3.75185732,  4.65543858,
        0.55779525,  1.15574987, -1.98461337,  5.39771083, -7.81395192])

# creating an array of a specified datatype
>>> np.array([1.5, 3.20, 5.78], dtype=int)
array([1, 3, 5])
```

## Creating Arrays from Python Sequences
You can create an array from a Python `list` or `tuple` by using NumPy's `array` function. NumPy will interpret the structure of the data it receives to determine the dimensionality and shape of the array. For example, a single list of numbers will be used to create a 1-dimensional array: 

```python
# a list of numbers will become a 1D-array
>>> np.array([1., 2., 3.])  # shape: (3,)
array([ 1.,  2.,  3.])
```

Nested lists/tuples will be used to construct multidimensional arrays. For example, a "list of equal-length lists of numbers" will lead to a 2-dimensional array; each of the inner-lists comprises a row of the array. Thus a list of two, length-three lists will produce a (2,3)-shaped array:
 
```python
# a list of lists of numbers will produce a 2D-array
>>> np.array([[1., 2., 3.], [4., 5., 6.]])  # shape: (2, 3)
array([[ 1.,  2.,  3.],
       [ 4.,  5.,  6.]])
```

A "list of equal-length lists, of equal-length lists of numbers" creates a 3D-array, and so on. Recall that using repeated concatenation, `[0]*3` will produce `[0, 0, 0]`. Using this, let's create two lists, each containing three lists, each containing four zeros; feeding this to `np.array` thus produces a 2x3x4 array of zeros:
```python
# A list of lists of lists of zeros creates a 3D-array
>>> np.array([[[0]*4]*3]*2)
array([[[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],

       [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]])
```

You will seldom use lists to form high-dimensional arrays like this. Instead, there are other array-creation functions that are more amendable to generating high-dimensional data, which we will introduce next. For example, we will see that the `np.zeros` function is a much more civilized way to create a high-dimensional array of zeros. 
<!-- #endregion -->

<div class="alert alert-warning"> 

**Warning!** 

You actually *can* create an array from lists of *unequal* lengths. The resulting array is **not** an ND-array as it has no well-defined dimensionality. Instead, something called an *object-array* is produced, which does not benefit from the majority of NumPy's features. This is a relatively obscure feature of the NumPy library, and should be avoided unless you really know what you're doing!

</div>

<!-- #region -->
## Creating Constant Arrays: `zeros` and `ones`
NumPy provides the functions `zeros` and `ones`, which will fill an array of user-specified shape with 0s and 1s, respectively:

```python
# create a 3x4 array of zeros
>>> np.zeros((3, 4))
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])

# create a shape-(4,) array of ones
>>> np.ones((4,))
array([ 1.,  1.,  1.,  1.])
```

NumPy provides additional functions for creating constant-valued arrays. Please refer to [the official documentation](https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html#ones-and-zeros) for a complete listing. 
<!-- #endregion -->

<!-- #region -->
## Creating Sequential Arrays: `arange` and `linspace`
The [arange](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html#numpy.arange) function allows you to initialize a sequence of integers based on a starting point (inclusive), stopping point (exclusive), and step size. This is very similar to the `range` function; however `arange` immediately creates this sequence as an array, whereas `range` produces a generator.
```python
>>> np.arange(0, 10, 1)  # start (included): 0, stop (excluded): 10, step:1 
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# supplying one value to `arange` amounts to specifying the stop value 
# start=0 and step=1 are then used as defaults
>>> np.arange(10)  # equivalent to: start: 0, stop: 10, step:1 
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> np.arange(-5, 6, 2) # start (included): -5, stop (excluded): 6, step:2 
array([-5, -3, -1,  1,  3,  5])
```

The [linspace](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html) function allows you to generate $N$ *evenly-spaced* points within a user-specified interval $[i, j]$ ($i$ and $j$ are included in the interval). This is often used to generate a domain of values on which to evaluate a mathematical function (e.g. if you want to the sine function from $-\pi$ to $\pi$ on a finely-divided grid).

```python
# generate five evenly-spaced points on the interval [-1, 1]
>>> np.linspace(-1, 1, 5)
array([-1. , -0.5,  0. ,  0.5,  1. ])

# generate two evenly-spaced points on the interval [3, 4]
>>> np.linspace(3, 4, 2)
array([ 3.,  4.])

# generate 100 evenly-spaced points on the interval [-pi, pi]
>>> np.linspace(-np.pi, np.pi, 100)
array([-3.14159265, ..., 3.14159265])
```

Numpy has other functions for creating sequential arrays, such as producing an array spaced evenly on a log-scaled interval. See the [official documentation](https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html#numerical-ranges) for a complete listing.
<!-- #endregion -->

<!-- #region -->
## Creating Arrays Using Random Sampling
Several functions can be accessed from `np.random`, which populate arrays of a user-specified shape by drawing randomly from a specified statistical distribution:
```python
# create a shape-(3,3) array by drawing its entries randomly
# from the uniform distribution [0, 1) 
>>> np.random.rand(3,3)
array([[ 0.09542611,  0.13183498,  0.39836068],
       [ 0.7358235 ,  0.77640024,  0.74913595],
       [ 0.37702688,  0.86617624,  0.39846429]])

# create a shape-(5,) array by drawing its entries randomly
# from a mean-0, variance-1 normal (a.k.a. Gaussian) distribution
>>> np.random.randn(5)
array([-1.11262121, -0.35392007,  0.4245215 , -0.81995588,  0.65412323])
```
There are [many more functions](https://docs.scipy.org/doc/numpy/reference/routines.random.html#distributions) to read about that allow you to draw from a wide variety of statistical distributions. This only scratches the surface of random number generation in NumPy.

<!-- #endregion -->

<!-- #region -->
## Creating an Array with a Specified Data Type
Each of the preceding functions used to create an array can be passed a so-called 'keyword' argument, `dtype`, which instructs NumPy to use a specified data type when producing the contents of the array.

```python
# populate an array using 32-bit floating point numbers
>>> np.array([1, 2, 3], dtype="float32") 
array([ 1.,  2.,  3.], dtype=float32)

# default data type produced by `arange` is 32-bit integers
>>> np.arange(0, 4).dtype  
dtype('int32')

# the data type produced by `arange` can be specified otherwise
>>> np.arange(0, 4, dtype="float16")
array([ 0.,  1.,  2.,  3.], dtype=float16)

# generate shape-(4,4) array of 64-bit complex-valued 0s
>>> np.zeros((4, 4), dtype="complex64")
array([[ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j]], dtype=complex64)
```

Refer to [the official NumPy documentation](https://docs.scipy.org/doc/numpy/user/basics.types.html#array-types-and-conversions-between-types) for the complete list of available array datatypes.
<!-- #endregion -->

<!-- #region -->
## Joining Arrays Together
Similar to Python lists and tuples, NumPy arrays can be concatenated together. However, because NumPy's arrays can be multi-dimensional, we can choose the dimension along which arrays are joined. 
```python
# demonstrating methods for joining arrays 
>>> x = np.array([1, 2, 3])
>>> y = np.array([-1, -2, -3])

# stack `x` and `y` "vertically"
>>> np.vstack([x, y])
array([[ 1,  2,  3],
       [-1, -2, -3]])

# stack `x` and `y` "horizontally"
>>> np.hstack([x, y])
array([ 1,  2,  3, -1, -2, -3])
```

A complete listing of functions for joining arrays can be [found in the official NumPy documentation](https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html#joining-arrays). There are also corresponding functions for splitting an array into independent arrays.
<!-- #endregion -->

## Links to Official Documentation

- [Constant arrays](https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html#ones-and-zeros)
- [numpy.array](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy-array)
- [Sequential arrays](https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html#numerical-ranges)
- [Random distributions](https://docs.scipy.org/doc/numpy/reference/routines.random.html#distributions)
- [Array types](https://docs.scipy.org/doc/numpy/user/basics.types.html#array-types-and-conversions-between-types)
- [Joining arrays](https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html#joining-arrays)
