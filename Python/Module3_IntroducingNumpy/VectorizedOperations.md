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
   :description: Topic: Vectorized operations with numpy arrays, Difficulty: Easy, Category: Section
   :keywords: vectorize, optimized, calculation, numpy, fast, C routine, MKL, sum, linear algebra, optimized
<!-- #endraw -->

<!-- #region -->
# "Vectorized" Operations: Optimized Computations on NumPy Arrays

In this section, we will:

- Define the term vectorization, as it is used in the context of Python/NumPy.
- Prescribe the use of NumPy's vectorized functions for performing optimized numerical computations on arrays.
- Compare the performance of a simple non-vectorized computation to a vectorized one.
- Describe how unary, binary, and sequential functions are defined on NumPy arrays.
- Provide a brief overview of linear algebra functions and logical operations.

## Basic Mathematical Operations Using Arrays
The ND-array can be utilized in mathematical expressions to perform mathematical computations using an array's entries. In general, NumPy implements mathematical functions such that, when a function acts on an array, the mathematical operation is applied to *each* entry in the array.   
```python
# Demonstrating the application of common
# mathematical operations to a NumPy array
>>> import numpy as np

>>> x = np.array([[ 0.,  1.,  2.],
...               [ 3.,  4.,  5.],
...               [ 6.,  7.,  8.]])

# `x ** 2` squares each entry in the array `x`
>>> x ** 2
array([[  0.,   1.,   4.],
       [  9.,  16.,  25.],
       [ 36.,  49.,  64.]])

# `np.sqrt(x)` takes the square-root
# of each entry in the array `x`
>>> np.sqrt(x)
array([[ 0.        ,  1.        ,  1.41421356],
       [ 1.73205081,  2.        ,  2.23606798],
       [ 2.44948974,  2.64575131,  2.82842712]])

# Slices return arrays, thus you can operate
# on these too. Add .5 to each entry in row-0
# of `x`
>>> .5 + x[0, :]
array([ 0.5,  1.5,  2.5])
```
<!-- #endregion -->

<!-- #region -->
Similarly, mathematical operations performed between two arrays are designed to act on the corresponding pairs of entries between the two arrays:
```python
# Demonstrating mathematical operations between two arrays
>>> x = np.array([[ 0.,  1.,  2.],
...               [ 3.,  4.,  5.],
...               [ 6.,  7.,  8.]])

>>> y = np.array([[-4. , -3.5, -3. ],
...               [-2.5, -2. , -1.5],
...               [-1. , -0.5, -0. ]])

# `x + y` will add the corresponding entries of
# the arrays `x` and `y`
>>> x + y
array([[-4. , -2.5, -1. ],
       [ 0.5,  2. ,  3.5],
       [ 5. ,  6.5,  8. ]])

>>> x * y
array([[-0. , -3.5, -6. ],
       [-7.5, -8. , -7.5],
       [-6. , -3.5, -0. ]])
```

There are also mathematical operations which are designed to operate on sequences of numbers, such as the sum function. NumPy's sequential functions can act on an array's entries as if they form a single sequence, or act on subsequences of the array's entries, according to the array's axes.
```python
# applying the sequential function, `np.sum`
# on an array
>>> x = np.array([[ 0.,  1.,  2.],
...               [ 3.,  4.,  5.],
...               [ 6.,  7.,  8.]])

# summing over all of the array's entries
>>> np.sum(x)
36.0

# summing over the rows, within each column
# of the array
>>> np.sum(x, axis=0)
array([  9.,  12.,  15.])
```

We will use this section to provide a more thorough overview of the various mathematical functions that are provided by NumPy, as well as the behavior of its sequential mathematical operations. However, we must first understand that NumPy performs these "vectorized operations" in a highly-optimized fashion, such that pure Python code can never rival its efficiency. By the end of this section, "vectorized operation" will become a phrase of endearment.

<!-- #endregion -->

<!-- #region -->
## Vectorized Operations
Recall that NumPy's ND-arrays are *homogeneous*: an array can only contain data of a single type. For instance, an array can contain 8-bit integers or 32-bit floating point numbers, but not a mix of the two. This is in stark contrast to Python's lists and tuples, which are entirely unrestricted in the variety of contents they can possess; a given list could simultaneously contain strings, integers, and other objects. This restriction on an array's contents comes at a great benefit; in "knowing" that an array's contents are homogeneous in data type, NumPy is able to delegate the task of performing mathematical operations on the array's contents to optimized, compiled C code. This is a process that is referred to as **vectorization**. The outcome of this can be a *tremendous* speedup relative to the analogous computation performed in Python, which must painstakingly check the data type of *every* one of the items as it iterates over the arrays, since Python typically works with lists with unrestricted contents.    

<div class="alert alert-info"> 

**Definition**: 

In the context of high-level languages like Python, Matlab, and R, the term **vectorization** describes the use of optimized, pre-compiled code written in a low-level language (e.g. C) to perform mathematical operations over a sequence of data. This is done in place of an explicit iteration written in the native language code (e.g. a "for-loop" written in Python). 

</div>

Consider, for instance, the task of summing the integers 0-9,999 stored in an array. Calling NumPy's `sum` function cues optimized C code to iterate over the integers in the array and tally the sum. `np.sum` is therefore a "vectorized" function. Let's time how long it takes to compute this sum: 

```python
>>> import numpy as np

# sum an array, using NumPy's vectorized 'sum' function
>>> np.sum(np.arange(10000))  # takes 11 microseconds on my computer
49995000
```

Now let's compare this to the time required to *explicitly* loop over the array in Python and tally up the sum. Python is unable to take advantage of the fact that the array's contents are all of a single data type - it has to check, for every iteration, if it is dealing with an integer, a string, a floating point number, etc, just as it does when iterating over a list. This will slow down the computation massively.

```python
# sum an array by explicitly looping over the array in Python
# this takes 822 microseconds on my computer
>>> total = 0
>>> for i in np.arange(10000):
...     total = i + total
>>> total
49995000
```
<!-- #endregion -->

<!-- #region -->
Timed on my computer, the sum is **over 50 times faster when performed in using NumPy's vectorized function**! This should make it clear that, whenever computational efficiency is important, one should avoid performing explicit for-loops over long sequences of data in Python, be them lists or NumPy arrays. NumPy provides a whole suite of vectorized functions. In fact, the name of the game when it comes to leveraging NumPy to do computations over arrays of numbers is to exclusively leverage its vectorized functions. The following computations all invoke vectorized functions: 

```python
>>> import numpy as np

# multiply 2 with each number in the array
>>> 2 * np.array([2, 3, 4]) 
array([4, 6, 8])

# subtract the corresponding entries of the two arrays
>>> np.array([10.2, 3.5, -0.9]) - np.array([8.2, 3.5, 6.5])
array([ 2. ,  0. , -7.4])

# Take the "dot product" of the two arrays 
# "dot product" means: multiply their corresponding entries and sum the result
>>> np.dot(np.array([1, -3, 4]), np.array([2, 0, 1]))
6
```

All of the mathematical functions that are introduced in the remainder of this section perform vectorized operations.
<!-- #endregion -->

<div class="alert alert-info">

**Takeaway**: 

NumPy provides highly-optimized functions for performing mathematical operations on arrays of numbers. Performing extensive iterations (e.g. via 'for-loops') in Python to perform repeated mathematical computations should nearly always be replaced by the use of vectorized functions on arrays. This informs the entire design paradigm of NumPy.  

</div>

<!-- #region -->
## NumPy's Mathematical Functions
We will now take some time to survey the various types of vectorized mathematical functions that NumPy supplies, and how these mathematical operations, which traditionally are defined on individual numbers, are applied to arrays of numbers. We will look at

- unary functions: $f(x)$
- binary functions: $f(x,y)$
- functions that operate on sequences of numbers: $f(\{x_i\}_{i=0}^{n-1})$ 

These represent a substantial portion of the essential mathematical tools in the NumPy library. An exhaustive list of NumPy's mathematical functions is available in the [official documentation](https://docs.scipy.org/doc/numpy/reference/ufuncs.html#math-operations).

### Unary Functions
A unary function is a mathematical function that only accepts one operand (i.e. argument): $f(x)$. NumPy supplies many familiar unary functions:

| Unary Function: $f(x)$    | NumPy Function |
| ------------- |:-------------:|
| $\vert x \vert$ | `np.absolute` |   
| $\sqrt{x}$ | `np.sqrt` | 
| **Trigonometric Functions** | <br> | 
| $\sin{x}$ | `np.sin` |   
| $\cos{x}$ | `np.cos` | 
| $\tan{x}$ | `np.tan` | 
| **Logarithmic Functions** | <br> | 
| $\ln{x}$ | `np.log` |   
| $\log_{10}{x}$ | `np.log10` | 
| $\log_{2}{x}$ | `np.log2` | 
| **Exponential Functions** | <br> | 
| $e^{x}$ | `np.exp` |   

This is by no means an exhaustive list of the available unary functions, for example the hyperbolic and inverse trigonometric functions are available too. These familiar functions are defined to work on individual numbers (i.e. "scalars"), not sequences of numbers. How, then, does NumPy implement these functions so that they behave in a coherent way when operating on arrays? The answer is that it **maps** the function over the array - applying $f(x)$ to each element within the array, and producing a new array as a result (i.e. the input array is not overwritten).

```python
import numpy as np
>>> x = np.array([0., 1., 2.])

# produces array([exp(0.), exp(1.), exp(2.)])
# x is not overwritten by this; a new array
# is created
>>> np.exp(x) 
array([ 1. ,  2.71828183,  7.3890561 ])
```

This process generalizes to arrays of any dimensionality and shape.

```python
# example of a unary function operating on a 2D array
>>> x = np.array([[-1, 2], [-3, 4]])
>>> x
array([[-1,  2],
       [-3,  4]])

>>> np.square(x)  # equivalent to: `x**2`
array([[ 1,  4],
       [ 9, 16]])
```

Because slicing returns an array, you can utilize these in mathematical operations as well
```python
# square column-0 of `x`
>>> x[:, 0] ** 2
array([1, 9])
```
<!-- #endregion -->

<div class="alert alert-info">

**Takeaway**: 

Applying a unary NumPy function, $f(x)$, to an N-dimensional array will apply $f(x)$ elementwise on the array. 

</div>

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Unary Functions**

Given the 2D array:
```python
>>> x = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11],
...               [12, 13, 14, 15]])
```

Take the natural-logarithm of the 1st and 3rd element in the 3rd-row of `x`, producing a shape-(2,) result. 

</div>
<!-- #endregion -->

### Binary Functions
A binary function has the form $f(x,y)$. The arithmetic operations are all binary functions:

| Binary Function: $f(x, y)$    | NumPy Function | Python operator |
| ------------- |:-------------:|:-------------:|
| $x\cdot y$ | `np.multiply` | `*`|   
| $x\div y$ | `np.divide` | `/`|   
| $x+y$ | `np.add` | `+`|
| $x-y$ | `np.subtract` | `-`|
| $x^{y}$ | `np.power` | `**`|
| $x \% y$ | `np.mod` | `%`|

<div class="alert alert-warning"> 

**Recall**: 

The "modulo" function ("mod" for short), denoted by $\%$, is defined to return the *remainder* of division: $5 \% 3 = 2$

</div>

As indicated in this table, these NumPy functions can be called by invoking the familiar Python math-operators, when used in the context of NumPy arrays.

Here are some other common binary functions:

| Binary Function: $f(x, y)$    | NumPy Function | 
| ------------- |:-------------:|
| $\max(x, y)$ | `np.maximum` |
| $\min(x, y)$ | `np.minimum` |   

There are two cases that we must consider when working with binary functions, in the context of NumPy arrays:

  1. When both operands of the function are arrays (of the same shape).
  2. When one operand of the function is a scalar (i.e. a single number) and the other is an array.
  

<!-- #region -->
Similar to the behavior of unary functions applied to an array, a binary function will operate on two same-shape arrays by applying the function to their pairwise elements.

```python
>>> x = np.array([0., 1., 2.])
>>> y = np.array([-1., 1., -2.])

# pair-wise addition of elements in `x` and `y`
>>> x + y  # convenient notation for calling `np.add(x, y)`
array([-1.,  2.,  0.])
```

This process generalizes to arrays of any dimensionality and shape, as long as the two operands have the same shape.
<!-- #endregion -->

<div class="alert alert-warning"> 

**Important Note**: 

You *can* apply binary NumPy functions to arrays of unlike shapes. For instance, you may want to add a single shape-(2,) array with ten of such arrays, which are stored as a single shape-(10,2) array. This process is known as **broadcasting**, and will be covered in detail in a later section.  

</div>


<!-- #region -->
```python
# example of a binary function operating on two 2D arrays
>>> x = np.array([[10,  2],
...               [ 3,  5]])

>>> y = np.array([[ 1,   0],
...               [ -4,  -1]])

>>> np.add(x, y)  # equivalent to `x + y`
array([[11,  2],
       [-1,  4]])

# add column-0 of `x` and row-1 of `y`
>>> x[:, 0] + y[1, :]
array([6, 2])
```
<!-- #endregion -->

<div class="alert alert-info"> 

**Takeaway**: 

Applying a binary NumPy-function, $f(x,y)$, to two same-shape arrays will apply $f(x,y)$ to each of their pairwise elements, producing an array of the same shape as either of the operands.  

</div>

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Binary Functions**

Given the 2D array:
```python
>>> x = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11],
...               [12, 13, 14, 15]])
```

Add the four quadrants of `x`, producing a shape-(2, 2) output. 

</div>
<!-- #endregion -->

<!-- #region -->
By now, you may be able to guess NumPy's behavior when you perform feed a binary function a scalar (i.e. a single number) and an array: the function is applied elementwise on the array, with each application filling one of the function's arguments, and the single scalar provided everywhere as the other operand. This matches exactly the behavior seen in traditional linear algebra.

```python
>>> 3 * np.array([0., 1., 2.])  # convenient notation for calling `np.multiply(3, x)`
array([ 0.,  3.,  6.])

>>> np.array([1., 2., 3.]) ** 2  # convenient notation for calling `np.power(x, 2)`
array([ 1.,  4.,  9.])
```

This process generalizes to an array of any dimensionality and shape. 


```python
# examples of a binary function operating on a scalar & an array
>>> x = np.array([[10,  2],
...               [ 3,  5]])

>>> np.maximum(4, x)
array([[10,  4],
       [ 4,  5]])

# a 3D array of shape-(2, 2, 8)
>>> y = np.array([[[ 0,  1,  2,  3,  4,  5,  6,  7],
...                [ 8,  9, 10, 11, 12, 13, 14, 15]],
...                  
...               [[16, 17, 18, 19, 20, 21, 22, 23],
...                [24, 25, 26, 27, 28, 29, 30, 31]]])

>>> y[0, :, ::2] * -1
array([[  0,  -2,  -4,  -6],
       [ -8, -10, -12, -14]])
```

<!-- #endregion -->

<div class="alert alert-info">

**Takeaway**: 

Applying a binary NumPy function, $f(x,y)$, to an array and a scalar amounts to "distributing" the function elementwise over the array, everywhere utilizing the scalar as the other operand for the binary function.

</div>

<!-- #region -->
### Sequential Functions
A sequential function expects a variable-length sequence of numbers as an input, and produces a single number as an output: $f(\{x_i\}_{i=0}^{n-1})$. The following are some sequential NumPy functions:

| Sequential Function: $f(\{x_i\}_{i=0}^{n-1})$    | NumPy Function |
| ------------- |:-------------:|
| Mean of $\{x_i\}_{i=0}^{n-1}$ | `np.mean` |
| Median of $\{x_i\}_{i=0}^{n-1}$ | `np.median` | 
| Variance of $\{x_i\}_{i=0}^{n-1}$ | `np.var` | 
| Standard Deviation of $\{x_i\}_{i=0}^{n-1}$ | `np.std` | 
| Maximum Value of $\{x_i\}_{i=0}^{n-1}$ | `np.max` |
| Minimum Value of $\{x_i\}_{i=0}^{n-1}$ | `np.min` |
| Index of the Maximum Value of $\{x_i\}_{i=0}^{n-1}$ | `np.argmax` |
| Index of the Minimum Value of $\{x_i\}_{i=0}^{n-1}$ | `np.argmin` |
| Sum of $\{x_i\}_{i=0}^{n-1}$ | `np.sum` | 

The implementation of sequential NumPy functions is straightforward when working with 1-dimensional arrays:
```python
# demonstrating sequential functions
>>> x = np.array([0., 2., 4.])
>>> np.sum(x)  # can also be invoked as `x.sum()`
6.
>>> np.mean(x)  # can also be invoked as `x.mean()`
2.
```
How do these functions behave when they are fed multi-dimensional arrays? By default, NumPy's sequential functions treat any multidimensional array as if it had been reshaped to a 1-dimensional array. For example:

```python
>>> x = np.array([[0, 1],
...               [2, 3],
...               [4, 5]])

# `sum`  will treat a multidimensional array 
# as if it is a single sequence of numbers, by default
>>> np.sum(x)
15
```

This default behavior of sequential NumPy functions can be overwritten by specifying the keyword argument `axis` within the sequential function. This is a very useful and common thing to do. We will carefully study what the axis argument is used for in these and other NumPy functions.
<!-- #endregion -->

<!-- #region -->
### Specifying the `axis` Keyword Argument in Sequential NumPy Functions
Let's delve into the meaning of the `axis` argument by first seeing it in action:

```python
# creating a shape-(3,2) array
>>> x = np.array([[0, 1],
...               [2, 3],
...               [4, 5]])

# sum over axis-0, within axis-1
# i.e. sum over the rows, within each column
>>> np.sum(x, axis=0)  # equivalent: x.sum(axis=0)
array([6, 9])

# sum over axis-1, within axis-0
# i.e. sum over the columns, within each row
>>> np.sum(x, axis=1)  # equivalent: x.sum(axis=1)
array([1, 5, 9])

# negative axis-indices can be used too
>>> np.sum(x, axis=-1)  # equivalent: np.sum(x, axis=1)
array([1, 5, 9])

# sum over axis-0 and axis-1
# i.e. sum the array as if it were a 1D sequence (default behavior)
>>> np.sum(x, axis=(0, 1))  # equivalent: x.sum(axis=(0, 1))
15

```

The `axis` argument thus specifies which axis or axes are traversed to produce the input sequences for the sequential function to act on. One sequence is designated for each valid combination of indices of the non-traversed axes. For example, `np.sum(x, axis=0)` says: "for each of the columns of `x`, sum over its rows". Thus the following sequences are summed over:

```
x[:, 0] -> array([0, 2, 4])  # traverse all rows within column-0
x[:, 1] -> array([1, 3, 5])  # traverse all rows within column-1
```
Thus each column of `x` is summed over, producing a shape-(2,) array containing the result of the two sums. Similarly, `np.sum(x, axis=1)` produces a shape-(3,) array, which stores the sum along each of the three rows in `x`. 

You can also supply *multiple* axes to the keyword argument by specifying them in a "tuple" of integers (using a list instead of a tuple will *not* work). `np.sum(x, axis=(0,1))` cues NumPy to traverse *both* of `x`'s axes, designating the entirety of `x`'s contents as the sequence, and summing to the single sequence into one number. Recall that this matches the default behavior when no `axis` keyword argument is specified.
<!-- #endregion -->

<div class="alert alert-info">

**Takeaway**: 

All sequential NumPy functions have an `axis` keyword argument that can be specified. `axis` is to be fed a single integer or a tuple of integers, which indicate which array axes are to be traversed to designate the sequences of array data to be operated on. A sequence is generated for each valid combination of indices for the non-traversed axes. By default, **all** of the input-array's axes are included, thus the entire content of the array is treated as a single sequence.

</div>

<!-- #region -->
#### Understanding the `axis` argument with a  Multi-Dimensional Array
The key to understanding the `axis` keyword argument, when working with multi-dimensional arrays, is to be comfortable with how array traversal works in NumPy. Refer to Section 5 of this module for a refresher on this topic. Consider the following shape-(4,2,3) array:

```python
>>> x = np.arange(24).reshape(4,2,3)
>>> x
array([[[ 0,  1,  2],
        [ 3,  4,  5]],

       [[ 6,  7,  8],
        [ 9, 10, 11]],

       [[12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23]]])
```

We can think of this array as possessing four, 2x3 sheets of numbers. Traversing along axis-0 of `x` amounts to stepping from sheet to sheet, given each valid combination of axis-1 and axis-2 indices. Thus `np.mean(x, axis=0)` says: "for each combination of row and column, take the mean along the sheets of `x`". Therefore six distinct sequences within `x` are designated for this sequential function to act on:
```
x[:, 0, 0] -> array([ 0,  6, 12, 18])  {mean =  9}
x[:, 0, 1] -> array([ 1,  7, 13, 19])  {mean = 10}
x[:, 0, 2] -> array([ 2,  8, 14, 20])  {mean = 11}
x[:, 1, 0] -> array([ 3,  9, 15, 21])  {mean = 12}
x[:, 1, 1] -> array([ 4, 10, 16, 22])  {mean = 13}
x[:, 1, 2] -> array([ 5, 11, 17, 23])  {mean = 14}
```

Also, notice that the set of valid combinations of axis-1 and axis-2 indices corresponds to the two-by-three grid associated with they layout of a sheet. NumPy will return the six mean values in a shape-(2,3) array, so that the correspondence between each sequence and its mean-value is unambiguous:

```python
>>> np.mean(x, axis=0)
array([[  9.,  10.,  11.],
       [ 12.,  13.,  14.]])
```

<div class="alert alert-warning"> 

**Recall**: 

Recall that NumPy uses row-major ordering (a.k.a C-ordering) when traversing arrays.

</div>

Suppose we specify two axes, say axis-0 and axis-2; traversing these two axes amounts to stepping along the sheets and columns of `x`, for each axis-1 index. Thus two sequences are produced:

```
x[:, 0, :] -> array([ 0,  1,  2,  6,  7,  8, 12, 13, 14, 18, 19, 20])  {mean = 10}
x[:, 1, :] -> array([ 3,  4,  5,  9, 10, 11, 15, 16, 17, 21, 22, 23])  {mean = 13}
```

```python
>>> np.mean(x, axis=(0, 2))
array([ 10.,  13.])
```
These observations lead us to the following general result:

<div class="alert alert-info"> 

**Result**: 

If $X$ is an $N$-dimensional array, and $j$ (with $j \leq N$) axes are specified in the `axis` keyword argument for a sequential NumPy function, then a $N-j$-dimensional array will be produced by this function. The shape of the result will be that of $X$, but with the entries associated with those $j$ axes removed.

</div>
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Basic Sequential Functions**

A digital image is simply an array of numbers, which instructs a grid of pixels on a monitor to shine light of specific colors, according to the numerical values in that array. 

An RGB-image can thus be stored as a 3D NumPy array of shape-$(V, H, 3)$. $V$ is the number of pixels along the vertical direction, $H$ is the number of pixels along the horizontal, and the size-3 dimension stores the red, blue, and green color values for a given pixel. Thus a $(32, 32, 3)$ array would be a 32x32 RBG image.

It is common to work with a collection of images. Suppose we want to store N images in a single array; thus we now consider a 4D shape-$(N, V, H, 3)$ array. 

Let's collect some statistics on a collection of images. For the sake of convenience, let's simply generate a 4D-array of random numbers as a placeholder for real image data. We will generate 100, 32x32 RGB images:

```python
>>> images = np.random.rand(100, 32, 32, 3)
```

Now, compute the following:

1\. The average 32x32 RGB image.

2\. The total sum of all the values in the array.

3\. The minimum blue value, respective to each image.

4\. The standard deviation among all the RGB values in all the images, respective to each pixel position (thus you should produce a shape-(32, 32) array of values).

5\. The maximum red-value in the top-left quadrant, respective to each image.

</div>
<!-- #endregion -->

<!-- #region -->
## Logical Operations
NumPy provides [a suite of logical operations](https://docs.scipy.org/doc/numpy/reference/routines.logic.html) that can operate on arrays. Many of these map logical operations over array entries in the same fashion as NumPy's mathematical functions. These functions return either a single boolean object, or a boolean-type array.

```python
# check which entries of `x` are less than 6
>>> x = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11],
...               [12, 13, 14, 15]])

# returns a boolean-type array
>>> x < 6  # equivalent to `np.less(x, 6)`
array([[ True,  True,  True,  True],
       [ True,  True, False, False],
       [False, False, False, False],
       [False, False, False, False]], dtype=bool)

# performing a logical comparison between two arrays
>>> np.array([1, 5, 10]) <=  np.array([1, 5, -1]) 
array([ True,  True, False], dtype=bool)
```
<!-- #endregion -->

<!-- #region -->
Recall from the Essentials of Python module that, due to effect of floating point numbers having limited numerical precision, that you should never rely on two floating point numbers being exactly equal. Rather, you should require that they are sufficiently "close" in value. In this same vein, you ought not check that the entries of two float-type arrays are precisely equal. Towards this end, the function `allclose` can be used to verify that all corresponding pairs of entries between two arrays are approximately equal in value:

```python
# checking if two arrays match, using `np.allclose`
>>> x = np.array([0.1, 0.2, 0.3])
>>> y = np.array([1., 2., 3.]) / 10

>>> np.allclose(x, y)
True
```
<!-- #endregion -->

## Linear Algebra
Lastly, we note that NumPy provides a suite of functions that can perform optimized computations and routines relevant to linear algebra. Included here are functions for performing matrix products and tensor products, solving eigenvalue problems, inverting matrices, and computing vector normalizations. Please refer to the [official NumPy documentation](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html) for a full listing of these functions.




## Conclusion
NumPy provides users with a wide variety of functions capable of performing operations on arrays of data. Its use of **vectorization** makes these functions incredibly fast, when compared to the analogous computations performed in pure Python. Although the preceding discussion laid out a substantial number of rules for how these functions work, one should not worry about memorizing them. Rather, it is best to apply these functions to arrays of various dimensionality, and build an intuition for them. You may be pleasantly surprised by how easy it is to get a hang of this material by simply putting it to practice.


## Links to Official Documentation

- [Math functions](https://docs.scipy.org/doc/numpy/reference/ufuncs.html#math-operations)
- [Logic functions](https://docs.scipy.org/doc/numpy/reference/routines.logic.html)
- [Linear algebra functions](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)


## Reading Comprehension Solutions

<!-- #region -->
**Unary Functions: Solution**

Take the natural-logarithm of the 1st and 3rd element in the 3rd-row of `x`, producing a shape-(2,) result. 

```python
>>> x = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11],
...               [12, 13, 14, 15]])

>>> np.log(x[2, 0::2])
array([ 2.07944154,  2.30258509])
```
<!-- #endregion -->

<!-- #region -->
**Binary Functions: Solution**

Add the four quadrants of `x`, producing a shape-(2, 2) output.

```python
>>> x = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11],
...               [12, 13, 14, 15]])

    # top-left  top-right    bottom-left  bottom-right
>>> x[:2, :2] + x[:2, -2:] + x[-2:, :2] + x[-2:, -2:]
array([[20, 24],
       [36, 40]])
```
<!-- #endregion -->

<!-- #region -->
**Basic Sequential Functions: Solutions**
```python
>>> images = np.random.rand(100, 32, 32, 3)

# 1. The average 32x32 RGB image. 
>>> mean_imag = images.mean(axis=0)
>>> mean_imag.shape
(32, 32, 3)

# 2. The total sum of all the values in the array.
>>> images.sum()
153422.97903817348

# 3. The minimum blue value, respective to each image.
# the colors are ordered red-blue-green along axis-3
>>> min_blue = images[:, :, :, 2].min(axis=(1, 2))
>>> min_blue.shape
(100,)

# 4. The standard deviation among all the RGB values in all the images, 
#    respective to each pixel.
>>> pixel_std_dev = images.std(axis=(0, 3))
>>> pixel_std_dev.shape
(32, 32)

# The maximum red-value in the top-left quadrant, respective to each image.
>>> max_red_quad = images[:, :16, :16, 0].max(axis=(1, 2))
>>> max_red_quad.shape
(100,)
```
<!-- #endregion -->
