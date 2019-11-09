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
   :description: Topic: Indexing into multi-dimensional numpy arrays, Difficulty: Easy, Category: Section
   :keywords: numpy array, multidimensional, index, slice, negative index, rows, columns
<!-- #endraw -->

<!-- #region -->
#  Accessing Data Along Multiple Dimensions in an Array
In this section, we will: 

 - Define the "dimensionality" of an array.
 - Discuss the usefulness of ND-arrays.
 - Introduce the indexing and slicing scheme for accessing a multi-dimensional array's contents
 
We will encounter arrays of varying dimensionalities:

```python
# A 0-D array
np.array(8)

# A 1-D array, shape-(3,)
np.array([2.3, 0.1, -9.1])

# A 2-D array, shape-(3, 2)
np.array([[93,  95], 
          [84, 100], 
          [99,  87]])

# A 3-D array, shape-(2, 2, 2)
np.array([[[0, 1],
           [2, 3]],
          
          [[4, 5],
           [6, 7]]])
```

Similar to Python's sequences, we use 0-based indices and slicing to access the content of an array. However, we must specify an index/slice for *each* dimension of an array:
```python
>>> import numpy as np

# A 3-D array
>>> x = np.array([[[0, 1],
...                [2, 3]],
...           
...               [[4, 5],
...                [6, 7]]])

# get: sheet-0, both rows, flip order of columns
>>> x[0, :, ::-1]
array([[1, 0],
       [3, 2]])
```
<!-- #endregion -->

<!-- #region -->
## One-dimensional Arrays
Let's begin our discussion by constructing a simple ND-array containing three floating-point numbers. 

```python
>>> simple_array = np.array([2.3, 0.1, -9.1])
```
This array supports the same indexing scheme as Python's sequences (lists, tuples, and strings):

```
 +------+------+------+
 |  2.3 |  0.1 | -9.1 | 
 +------+------+------+
     0      1      2  
    -3     -2     -1       
```
The first row of numbers gives the position of the indices 0…3 in the array; the second row gives the corresponding negative indices. The slice from $i$ to $j$ returns an array containing of all numbers between the edges labeled $i$ and $j$, respectively:

```python
>>> simple_array[0]
2.3

>>> simple_array[-2]
0.1

>>> simple_array[1:3]
array([ 0.1, -9.1])

>>> simple_array[3]
IndexError: index 3 is out of bounds for axis 0 with size 3
```

Given this indexing scheme, only *one* integer is needed to specify a unique entry in the array. Similarly only *one* slice is needed to uniquely specify a subsequence of entries in the array. For this reason, we say that this is a *1-dimensional array*. In general, the *dimensionality* of an array specifies the number of indices that are required to uniquely specify one of its entries.

<div class="alert alert-info"> 

**Definition**: 

The **dimensionality** of an array specifies the number of indices that are required to uniquely specify one of its entries. 

</div>

This definition of dimensionality is common far beyond NumPy; one must use three numbers to uniquely specify a point in physical space, which is why it is said that space consists of three dimensions.
<!-- #endregion -->

## Two-dimensional Arrays
Before proceeding further down the path of high-dimensional arrays, let's briefly consider a very simple dataset where the desire to access the data along multiple dimensions is manifestly desirable. Consider the following table from a gradebook:

<!-- #region -->
|         | Exam 1 (%)           | Exam 2 (%) |
| ------------- |:-------------:| -----:|
| Ashley     | $93$ | $95$ |
| Brad     | $84$      |   $100$ |
| Cassie | $99$      |    $87$ |

This dataset contains 6 grade-values. It is almost immediately clear that storing these in a 1-dimensional array is not ideal:

```python
# using a 1-dimensional array to store the grades
>>> grades = np.array([93, 95, 84, 100, 99, 87])
```

While no data has been lost, accessing this data using a single index is less than convenient; we want to be able to specify both the student and the exam when accessing a grade - it is natural to ascribe *two dimensions* to this data. Let's construct a 2D array containing these grades:

```python
# using a 2-dimensional array to store the grades
>>> grades = np.array([[93,  95], 
...                    [84, 100], 
...                    [99,  87]])
```

NumPy is able to see the repeated structure among the list-of-lists-of-numbers passed to `np.array`, and resolve the two dimensions of data, which we deem the 'student' dimension and the 'exam' dimension, respectively. 

<div class="alert alert-warning">

**Axis vs Dimension**:  

Although NumPy does formally recognize the concept of dimensionality precisely in the way that it is discussed here, its documentation refers to an individual dimension of an array as an **axis**. Thus you will see "axes" (pronounced "aks-ēz") used in place of "dimensions"; however, they mean the same thing.

</div>

NumPy specifies the row-axis (students) of a 2D array as "axis-0" and the column-axis (exams) as axis-1. You must now provide *two* indices, one for each axis (dimension), to uniquely specify an element in this 2D array; the first number specifies an index along axis-0, the second specifies an index along axis-1. The zero-based indexing schema that we reviewed earlier applies to each axis of the ND-array:

```                                                    
                                                  -- axis-1 -> 
                                                    -2  -1    
                                                     0   1 
                                        |          +---+---+  
                                        |    -3, 0 |93 | 95| 
                                        |          +---+---+
                                      axis-0 -2, 1 |84 |100|  
                                        |          +---+---+
                                        |    -1, 2 |99 | 87|
                                        V          +---+---+
```

Because `grades` has three entries along axis-0 and two entries along axis-1, it has a "shape" of `(3, 2)`.

```python
>>> grades.shape
(3, 2)
```

### Integer Indexing
Thus, if we want to access Brad's (item-1 along axis-0) score for Exam  1 (item-0 along axis-1) we simply specify:

```python
# providing two numbers to access an element
# in a 2D-array
>>> grades[1, 0]  # Brad's score on Exam 1
84

# negative indices work as with lists/tuples/strings
>>> grades[-2, 0]  # Brad's score on Exam 1
84
```

### Slice Indexing
We can also uses *slices* to access subsequences of our data. Suppose we want the scores of all the students for Exam 2. We can slice from 0 through 3 along axis-0 (refer to the indexing diagram in the previous section) to include all the students, and specify index 1 on axis-1 to select Exam 2:

```python
>>> grades[0:3, 1]  # Exam 2 scores for all students
array([ 95, 100,  87])
```
As with Python sequences, you can specify an "empty" slice to include all possible entries along an axis, by default: `grades[:, 1]` is equivalent to `grades[0:3, 1]`, in this instance. More generally, withholding either the 'start' or 'stop' value in a slice will result in the use smallest or largest valid index, respectively:  
```python
>>> grades[1:, 1]  # equivalent to `grades[1:3, 1]
array([ 100,  87])

>>> grades[:, :1]  # equivalent to `grades[0:3, 0:1]
array([[93],
       [84],
       [99]])
```
The output of `grades[:, :1]` might look somewhat funny. Because the axis-1 slice only includes one column of numbers, the shape of the resulting array is (3, 1). 0 is thus only valid (non-negative) index for axis-1, since there is only one column to specify in the array.  

You can also supply a "step" value to the slice. `grades[::-1, :]` will returns the array of grades with the student-axis flipped (reverse-alphabetical order).

### Negative Indices
As indicated above, negative indices are valid too and are quite useful. If we want to access the scores of the latest exam for all of the students, you can specify:

```python
# using a negative index and a slice
>>> grades[:, -1]  # Latest exam scores (Exam 2), for all students
array([ 95, 100,  87])
```
Note the value of using the negative index is that it will always provide you with the latest exam score - you need not check how many exams the students have taken.

### Supplying Fewer Indices Than Dimensions 
What happens if we only supply one index to our array? It may be surprising that `grades[0]` does not throw an error since we are specifying only one index to access data from a 2-dimensional array. Instead, NumPy it will return all of the exam scores for student-0 (Ashley):

```python
>>> grades[0] 
array([ 93, 95])
```
This is because NumPy will automatically insert trailing slices for you if you don't provide as many indices as there are dimensions for your array. `grades[0]` was treated as `grades[0, :]`.

<div class="alert alert-info"> 
Suppose you have an $N$-dimensional array, and only provide $j$ indices for the array; NumPy will automatically insert $N-j$ trailing slices for you. In the case that $N=5$ and $j=3$, `d5_array[0, 0, 0]` is treated as  `d5_array[0, 0, 0, :, :]`
</div>
<!-- #endregion -->

Thus far, we have discussed some rules for accessing data in arrays, all of which fall into the category that is designated ["basic indexing"](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#basic-slicing-and-indexing) by the NumPy documentation. We will discuss the details of basic indexing and of ["advanced indexing"](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#advanced-indexing), in full, in a later section. Note, however, that all of the indexing/slicing reviewed here produces a "view" of the original array. That is, *no data is copied* when you index into an array using integer indices and/or slices. Recall that slicing lists and tuples *do* produce copies of the data.



<div class="alert alert-warning">

**FYI**: 

Keeping track of the meaning of an array's various dimensions can quickly become unwieldy when working with real datasets. [xarray](http://xarray.pydata.org/en/stable/) is a Python library that provides functionality comparable to NumPy, but allows users provide *explicit labels* for an array's dimensions; that is, you can *name* each dimension. Using an `xarray` to select Brad's scores could look like `grades.sel(student='Brad')`, for instance. This is a valuable library to look into at your leisure.

</div>

<!-- #region -->
## N-dimensional Arrays
Let's build up some intuition for arrays with a dimensionality higher than 2. The following code creates a 3-dimensional array:
```python
# a 3D array, shape-(2, 2, 2)
>>> d3_array = np.array([[[0, 1],
...                       [2, 3]],
...                         
...                      [[4, 5],
...                       [6, 7]]])
```
You can think of axis-0 denoting which of the 2x2 "sheets" to select from. Then axis-1 specifies the row along the sheets, and axis-2 the column within the row:

**Depicting the layout of a 3D array**
```
                                           sheet 0:
                                                  [0, 1]
                                                  [2, 3]

                                           sheet 1:
                                                  [4, 5]
                                                  [6, 7]                                             
```
```
                                        |       -- axis-2 ->
                                        |    |    
                                        |  axis-1 [0, 1]
                                        |    |    [2, 3]
                                        |    V
                                     axis-0     
                                        |      -- axis-2 ->
                                        |    |    
                                        |  axis-1 [4, 5]
                                        |    |    [6, 7]
                                        V    V

```

Thus `d3_array[0, 1, 0]` specifies the element residing in sheet-0, at row-1 and column-0:
```python
# retrieving a single element from a 3D-array
>>> d3_array[0, 1, 0]
2
```

`d3_array[:, 0, 0]` specifies the elements in row-0 and column-0 of **both** sheets:
```python
# retrieving a 1D sub-array from a 3D-array
>>> d3_array[:, 0, 0]
array([0, 4])
```
`d3_array[1]`, which recall is shorthand for `d3_array[1, :, :]`, selects both rows and both columns of sheet-1:
```python
# retrieving a 2D sub-array from a 3D-array
>>> d3_array[1]
array([[4, 5],
       [6, 7]])
```

In four dimensions, one can think of "*stacks* of sheets with rows and columns" where axis-0 selects the stack of sheets you are working with, axis-1 chooses the sheet, axis-2 chooses the row, and axis-3 chooses the column. Extrapolating to higher dimensions ("collections of stacks of sheets ...") continues in the same tedious fashion.  



<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info">

**Reading Comprehension: Multi-dimensional Indexing**

Given the 3D, shape-(3, 3, 3) array:

```python
>>> arr = np.array([[[ 0,  1,  2],
...                  [ 3,  4,  5],
...                  [ 6,  7,  8]],
...          
...                 [[ 9, 10, 11],
...                  [12, 13, 14],
...                  [15, 16, 17]],
...          
...                 [[18, 19, 20],
...                  [21, 22, 23],
...                  [24, 25, 26]]])
```

Index into the array to produce the following results

```python
#1 
array([[ 2,  5,  8],
       [11, 14, 17],
       [20, 23, 26]])

#2
array([[ 3,  4,  5],
       [12, 13, 14]])

#3
array([2, 5])

#4
array([[11, 10,  9],
       [14, 13, 12],
       [17, 16, 15]])
```

</div>
<!-- #endregion -->

<!-- #region -->
## Zero-dimensional Arrays
A zero dimensional array is simply a single number (a.k.a. a scalar value):
```python
# creating a 0-dimensional array
>>> x = np.array(15.2)
```

This is *not* equivalent to a length-1 1D-array: `np.array([15.2])`. According to our definition of dimensionality, *zero* numbers are required to index into a 0-D array as it is unnecessary to provide an identifier for a standalone number. Thus you cannot index into a 0-D array.
```python
# you cannot index into a 0-D array
>>> x[0]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-10-2f755f117ac9> in <module>()
----> 1 x[0]

IndexError: too many indices for array
    
```

You must use the syntax `arr.item()` to retrieve the numerical entry from a 0D array:
```python
>>> x.item()
15.2
```

Zero-dimensional arrays do not show up in real applications very often. They are, however, important from the point of view of NumPy being self-consistent in how it treats dimensionality in its arrays, and it is important that you are at least exposed to a 0D array and understand its nuances.
<!-- #endregion -->

<div class="alert alert-info">

**Takeaway**: 

Although accessing data along varying dimensions is ultimately all a matter of judicious bookkeeping (you *could* access all of this data from a 1-dimensional array, after all), NumPy's ability to provide users with an interface for accessing data along dimensions is incredibly useful. It affords us an ability to impose intuitive, abstract structure to our data. 

</div> 

<!-- #region -->
## Manipulating Arrays
NumPy provides an assortment of functions that allow us manipulate the way that an array's data can be accessed. These permit us to reshape an array, change its dimensionality, and swap the positions of its axes:

```python
>>> x = np.array([[ 1,  2,  3,  4],
...               [ 5,  6,  7,  8],
...               [ 9, 10, 11, 12]])

# reshaping an array
>>> x.reshape(3, 2, 2)
array([[[ 1,  2],
        [ 3,  4]],

       [[ 5,  6],
        [ 7,  8]],

       [[ 9, 10],
        [11, 12]]])

# Transposing an array: reversing 
# the ordering of its axes. This interchanges
# the rows and columns of `x`
>>> x.transpose()
array([[ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11],
       [ 4,  8, 12]])
```
A complete listing of the available array-manipulation functions can be found in the [official NumPy documentation](https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html). Among these functions, the reshape function is especially useful.   

### Introducing the `reshape` Function
The `reshape` function allows you to change the dimensionality and axis-layout of a given array. This adjusts the indexing interface used to access the array's underlying data, as was discussed in earlier in this module. Let's take a shape-(6,) array, and reshape it to a shape-(2, 3) array:

```python
>>> import numpy as np
>>> x = np.array([0, 1, 2, 3, 4, 5])

# reshape a shape-(6,) array into a shape-(2,3) array
>>> x.reshape(2, 3)
array([[0, 1, 2],
       [3, 4, 5]])
```

You can also conveniently reshape an array by "setting" its shape via assignment:
```python
# equivalent to: x = x.reshape(2, 3)
>>> x.shape = (2, 3)
```

Of course, the size the the initial array must match the size of the to-be reshaped array:

```python
# an array with 5 numbers are cannot be reshaped
# into a (3, 2) array
>>> np.array([0, 1, 2, 3, 4]).reshape(3, 2)
ValueError: total size of new array must be unchanged
```

Multidimensional arrays can be reshaped too:
```python
# reshaping a multidimensional array
>>> x = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11]])

# reshape from (3, 4) to (2, 3, 2)
>>> x.reshape(2, 3, 2)
array([[[ 0,  1],
        [ 2,  3],
        [ 4,  5]],

       [[ 6,  7],
        [ 8,  9],
        [10, 11]]])
```

Because the size of an input array and the resulting reshaped array must agree, you can specify *one* of the dimension-sizes in the reshape function to be -1, and this will cue NumPy to compute that dimension's size for you. For example, if you are reshaping a shape-(36,) array into a shape-(3, 4, 3) array. The following are valid:
```python
# Equivalent ways of specifying a reshape
# np.arange(36) produces the shape-(36,) array ([0, 1, 2, ..., 35])
np.arange(36).reshape(3, 4, 3)   # (36,) --reshape--> (3, 4, 3) 
np.arange(36).reshape(3, 4, -1)  # NumPy replaces -1 with 36/(3*4) -> 3
np.arange(36).reshape(3, -1, 3)  # NumPy replaces -1 with 36/(3*3) -> 4
np.arange(36).reshape(-1, 4, 3)  # NumPy replaces -1 with 36/(3*4) -> 3
```

You can use -1 to specify only one dimension: 
```python
>>> np.arange(36).reshape(3, -1, -1)  # this is an ambiguous specification, and thus
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-3-207d18d18af2> in <module>()
----> 1 np.arange(36).reshape(3, -1, -1)

ValueError: can only specify one unknown dimension
```

<div class="alert alert-info">

**Reshaping Does Not Make a Copy of an Array**: 

For all straightforward applications of reshape, NumPy does not actually create a new copy of an array's data when performing a `reshape` operation. Instead, the original array and the reshaped array reference the same underlying data. The reshaped array simply provides a new index-interface for accessing said data, and is thus referred to as a "view" of the original array (more on this "views" in a later section).

</div>
<!-- #endregion -->

## Links to Official Documentation

- [The N-dimensional array](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html)
- [Array indexing](https://docs.scipy.org/doc/numpy/user/basics.indexing.html#indexing)
- [Indexing routines](https://docs.scipy.org/doc/numpy/reference/routines.indexing.html#indexing-routines)
- [Array manipulation routines](https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html)


## Reading Comprehension Solutions


<!-- #region -->
**Reading Comprehension: Multi-dimensional Indexing**

```python
>>> arr = np.array([[[ 0,  1,  2],
...                  [ 3,  4,  5],
...                  [ 6,  7,  8]],
...          
...                 [[ 9, 10, 11],
...                  [12, 13, 14],
...                  [15, 16, 17]],
...          
...                 [[18, 19, 20],
...                  [21, 22, 23],
...                  [24, 25, 26]]])
```

```python
#1 
>>> arr[:, :, 2]
array([[ 2,  5,  8],
       [11, 14, 17],
       [20, 23, 26]])

#2
>>> arr[0:2, 1, :]
array([[ 3,  4,  5],
       [12, 13, 14]])

#3
>>> arr[0, :2, 2]
array([2, 5])

#4
>>> arr[1, :, ::-1]
array([[11, 10,  9],
       [14, 13, 12],
       [17, 16, 15]])
```

<!-- #endregion -->
