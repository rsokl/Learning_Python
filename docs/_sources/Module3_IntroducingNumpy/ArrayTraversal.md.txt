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
   :description: Topic: Numpy array traversal ordering, Difficulty: Medium, Category: Section
   :keywords: row-major order, c order, column-major order, f order, traversal, array iteration
<!-- #endraw -->

# Iterating Over Arrays & Array-Traversal Order
In this section, you will learn:

- About NumPy's functions for iterating over an array
- That there is more than one valid way for NumPy to perform this operation, which amounts to how NumPy traverses a multidimensional array.
- The row-major array traversal methodology, which is utilized by NumPy by default.

<!-- #region -->
NumPy provides valuable tools for iterating over any array, such that each element can be visited in the array, regardless of the array's shape. For example, recall that Python's built-in `enumerate` function permits us to produce each item in an iterable, along with its index of iteration:

```python
# enumerating the items in an iterable
>>> [i for i in enumerate("abcdef")]
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f')]
```

Similarly, NumPy provides the [ndenumerate](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate) function, which enumerates each element in an N-dimensional array, specifying the N-dimensional index for each element.
```python
>>> import numpy as np

# Demonstrating `np.ndenumerate`.
# A shape-(2, 2, 3) array
>>> x = np.array([[[ 25,   6, -35],
...                [  9, -40, -29]],
...        
...               [[ -8,   2, -37],
...                [ 17,  10, -45]]])

>>> [i for i in np.ndenumerate(x)]
[((0, 0, 0), 25),
 ((0, 0, 1), 6),
 ((0, 0, 2), -35),
 ((0, 1, 0), 9),
 ((0, 1, 1), -40),
 ((0, 1, 2), -29),
 ((1, 0, 0), -8),
 ((1, 0, 1), 2),
 ((1, 0, 2), -37),
 ((1, 1, 0), 17),
 ((1, 1, 1), 10),
 ((1, 1, 2), -45)]
```

See that each triplet of integers specifies the index for the corresponding array element:

```python
>>> x[0, 0, 0]
25

>>> x[0, 0, 1]
6

>>> x[0, 0, 2]
-35

>>> x[0, 1, 0]
9
```

See [the official NumPy documentation](https://docs.scipy.org/doc/numpy/reference/routines.indexing.html#iterating-over-arrays) for a complete listing of functions that facilitate iterating over arrays. The official documentation also provides [a detailed treatment of array iteration](https://docs.scipy.org/doc/numpy/reference/arrays.nditer.html#iterating-over-arrays), which is far more detailed than is warranted here. Next, we must discuss the default ordering that NumPy uses when traversing a N-dimensional array.


<!-- #endregion -->

<!-- #region -->
## How to Traverse an Array: Row-major (C) vs Column-major (F) Traversal Ordering
Note the order in which `np.ndenumerate` iterated over `x`. It first traversed the columns within row-0 of sheet-0 of `x`, and then it traversed the columns within the row-1 of sheet-0, and so on. What is special about this traversal order? Why, for instance, didn't it traverse the rows within a given column instead? We can also see that there is not a unique ordering for a `reshape` function to adhere to. For example, the following reshape operation could sensibly return either of the following results:
```
  array([0, 1, 2, 3, 4, 5]).reshape(2, 3) -->  array([[0, 1, 2],  or   array([[0, 2, 4],
                                                      [3, 4, 5]])             [1, 3, 5]])
```

Both arrays are of the appropriate shape and preserve the ordering of the original sequence of numbers, depending on how you traverse them. The left array preserves the ordering of the original data if you traverse the columns within a row, and then proceed to the next row. This is known as **row-major** ordering. The array on the right preserves the ordering if you traverse the rows within a given column, and then transition to the next column. This is thus referred to as **column-major** ordering. One ordering is not inherently better than the other. That being said, *NumPy always defaults to row-major ordering whenever one of its functions involves array traversal*.

<div class="alert alert-warning"> 

**Remember This:** 

NumPy utilizes row-major ordering, as a default, for any operation that requires an array to be traversed.

</div>

These two orderings are simple enough to follow for a 2D-array, but how do they manifest in arrays with higher dimensions, where we have to worry not only about rows and columns, but potentially "stacks of sheets with rows and columns" (which would be a 4D array) and so on? The generic rules are as follows:

- **Row-major ordering (C ordering) {NumPy's default}**: traverse an array by advancing the index of the *last axis*, first, until the end of that axis is reached, and then advance the index of the second-to last axis, and so on.
- **Column-major ordering (F ordering)**: traverse an array by advancing the index of the *first axis*, first, until the end of that axis is reached, and then advance the index of the second axis, and so on.

<div class="alert alert-info">

**Note**: 

"Row-major" ordering is also referred to as "C-ordering" because this is the traversal method utilized in the C language. "Column-major" ordering, on the other hand, is also referred to as "F-ordering", because it is used by the Fortran language. NumPy functions, like `reshape` allow you to specify either `order="C"` (which is the default) or `order="F"` to control the order in which an array is traversed; these options thus correspond to row-major and column-major ordering. 

</div>

To make this more concrete, let's consider how NumPy reshapes a shape-(24,) array into a shape-(2,3,4) array:
```python
# reshape a shape-(24,) array into a shape-(2,3,4) array
>>> np.arange(2*3*4).reshape(2,3,4)
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],

       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])
```

Following NumPy's default row-major ordering, we can perform this reshaping by following these steps:

  1. Create an empty array of the desired shape: (2, 3, 4).
  2. Start by inserting the 0th element from the input array into the (0, 0, 0) element of the output array.
  3. Advance the index by *increasing the index of the last axis, first*, and inserting the following element from the input array.
  4. If you reach the end of an axis (axis-2, for instance, only has 4 slots), reset the index for that axis to 0, and advance the index of the preceding axis. Go back to 3.

This traversal process is easier to understand when laid out explicitly:

***
**Reshaping a shape-(24,) array to a shape-(2,3,4) array, using NumPy's default "row-major" ordering**
```

                                Input Array     Output Array
                                -----------    ---------------
                                 entry: 0  ->  entry: (0, 0, 0)
                                 entry: 1  ->  entry: (0, 0, 1)
                                 entry: 2  ->  entry: (0, 0, 2)
                                 entry: 3  ->  entry: (0, 0, 3) *row-0 of sheet 0, filled. go to next row*
                                 entry: 4  ->  entry: (0, 1, 0)
                                 entry: 5  ->  entry: (0, 1, 1)
                                 entry: 6  ->  entry: (0, 1, 2)
                                 entry: 7  ->  entry: (0, 1, 3) *row-1 of sheet 0, filled. go to next row*
                                 entry: 8  ->  entry: (0, 2, 0)
                                 entry: 9  ->  entry: (0, 2, 1)
                                 entry:10  ->  entry: (0, 2, 2)
                                 entry:11  ->  entry: (0, 2, 3) *row-2 of sheet 0, filled. go to next sheet!*

                                 entry:12  ->  entry: (1, 0, 0)
                                 entry:13  ->  entry: (1, 0, 1)
                                 entry:14  ->  entry: (1, 0, 2)
                                 entry:15  ->  entry: (1, 0, 3) *row-0 of sheet 1, filled. go to next row*
                                 entry:16  ->  entry: (1, 1, 0)
                                 entry:17  ->  entry: (1, 1, 1)
                                 entry:18  ->  entry: (1, 1, 2)
                                 entry:19  ->  entry: (1, 1, 3) *row-1 of sheet 1, filled. go to next row*
                                 entry:20  ->  entry: (1, 2, 0)
                                 entry:21  ->  entry: (1, 2, 1)
                                 entry:22  ->  entry: (1, 2, 2)
                                 entry:23  ->  entry: (1, 2, 3) *row-2 of sheet 1, filled. Done!*
```

***

The same process can be extended to reshape one multidimensional array into another multidimensional array of a different shape. The input and output arrays are simply traversed, respectively, according to "row-major" rules. Suppose we want to reshape a shape-(2,3,4) array into a shape-(6,4) array. This process would be carried out as follows:

***
**Reshaping a shape-(2,3,4) into a shape(6,4) array using NumPy's default "row-major" ordering**
```

                                     Input Array       Output Array
                                  ----------------    ---------------
                                  entry: (0, 0, 0) -> entry: (0, 0)
                                  entry: (0, 0, 1) -> entry: (0, 1)
                                  entry: (0, 0, 2) -> entry: (0, 2)
                                  entry: (0, 0, 3) -> entry: (0, 3)
                                  entry: (0, 1, 0) -> entry: (1, 0)
                                  ...
                                  ...
                                  entry: (1, 2, 3) -> entry: (5, 3)
```
<!-- #endregion -->

Although this bookkeeping may seem a bit tedious at first glance, you will likely find that you are able to build up enough intuition for row-major ordering, to the point where you never need to write out these tables in full! The ability to reshape an array to adjust the way you can access an array's data is commonly used in data science applications. Furthermore, understanding how NumPy handles array traversal is critical to understanding more advanced concepts like array-broadcasting and advanced indexing. 


<div class="alert alert-info">

**Reshape is its own inverse**: 

According to this discussion, `reshape` can effectively "undo" itself: `np.arange(10).reshape(5,2).reshape(10)` will return `array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`. Take some time to consider why this will always be true, no matter how many intermediary reshapes are performed.

</div>


## Links to Official Documentation

- [Definition of row major ordering](https://docs.scipy.org/doc/numpy/glossary.html#term-row-major)
- [Definition of column major ordering](https://docs.scipy.org/doc/numpy/glossary.html#term-column-major)
- [Routines for iterating over arrays](https://docs.scipy.org/doc/numpy/reference/routines.indexing.html#iterating-over-arrays)
- [Detailed description of array iteration](https://docs.scipy.org/doc/numpy/reference/arrays.nditer.html#iterating-over-arrays)
