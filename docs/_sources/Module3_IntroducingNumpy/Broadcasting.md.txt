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
   :description: Topic: Numpy array broadcasting, Difficulty: Medium, Category: Section
   :keywords: broadcasting, vectorization, rules, mismatched shapes, distances
<!-- #endraw -->

<!-- #region -->
# Array Broadcasting
NumPy provides a mechanism for performing mathematical operations on arrays of *unequal* shapes:

```python
>>> import numpy as np

# a shape-(3, 4) array
>>> x = np.array([[-0. , -0.1, -0.2, -0.3],
...               [-0.4, -0.5, -0.6, -0.7],
...               [-0.8, -0.9, -1. , -1.1]])

# a shape-(4,) array
>>> y = np.array([1, 2, 3, 4])

# multiplying a shape-(4,) array with a shape-(3, 4) array
# `y` is multiplied by each row of `x`
>>> x * y
array([[-0. , -0.2, -0.6, -1.2],
       [-0.4, -1. , -1.8, -2.8],
       [-0.8, -1.8, -3. , -4.4]])
```

In effect, NumPy treated `y` as if its contents had been broadcasted along a new dimension, such that `y` was a shape-(3, 4) 2D array, which makes it compatible for multiplying with `x`:

\begin{equation}
\left( \begin{array}{*{3}{X}}
  -0.0 & -0.1 & -0.2 & -0.3 \\
  -0.4 & -0.5 & -0.6 & -0.7 \\
  -0.8 & -0.9 & -1.0 & -1.1
\end{array} \right)
% 
\cdot \left( \begin{array}{*{3}{X}}
   1 & 2 & 3 & 4
\end{array}\right)
% 
\rightarrow \left( \begin{array}{*{3}{X}}
  -0.0 & -0.1 & -0.2 & -0.3 \\
  -0.4 & -0.5 & -0.6 & -0.7 \\
  -0.8 & -0.9 & -1.0 & -1.1
\end{array} \right)
%
\cdot \left( \begin{array}{*{3}{X}}
  1 & 2 & 3 & 4 \\
  1 & 2 & 3 & 4 \\
  1 & 2 & 3 & 4
\end{array}\right)
\
\end{equation}

It is important to note that NumPy doesn't really create this broadcasted version of `y` behind the scenes; it is able to do the necessary computations without having to redundantly copy its contents into a shape-(3,4) array. Doing so would be a waste of memory and computation. That being said, this replication process conveys exactly the mathematics of broadcast operations between arrays; thus the preceding diagram reflects how you should always envision broadcasting.  


Broadcasting is not reserved for operations between 1-D and 2-D arrays, and furthermore both arrays in an operation may undergo broadcasting. That being said, not all pairs of arrays are broadcast-compatible.


```python
# Broadcast multiplications between a 
# shape-(3, 1, 2) array and a shape-(3, 1)
# array.
>>> x = np.array([[[0, 1]],
...
...               [[2, 3]],
...
...               [[4, 5]]])

>>> y = np.array([[ 0],
...               [ 1],
...               [-1]])

# shape-(3, 1, 2) broadcast-multiply with 
# shape-(3, 1) produces shape-(3, 3, 2)
>>> x * y
array([[[ 0,  0],
        [ 0,  1],
        [ 0, -1]],

       [[ 0,  0],
        [ 2,  3],
        [-2, -3]],

       [[ 0,  0],
        [ 4,  5],
        [-4, -5]]])

# an example of broadcast-incompatible arrays
# a shape-(2,) array with a shape-(3,) array
>>> np.array([1, 2]) * np.array([0, 1, 2])
ValueError: operands could not be broadcast together with shapes (2,) (3,) 
```
<!-- #endregion -->

<div class="alert alert-info"> 

**Definition: Array Broadcasting** 

Array Broadcasting is a mechanism used by NumPy to permit vectorized mathematical operations between arrays of unequal, but compatible shapes. Specifically, an array will be treated as if its contents have been replicated along the appropriate dimensions, such that the shape of this new, higher-dimensional array suits the mathematical operation being performed.     

</div>


We will now summarize the rules that determine if two arrays are broadcast-compatible with one another, and what the shape of the resulting array will be after the mathematical operation between the two arrays is performed.


## Rules of Broadcasting
Array broadcasting cannot accommodate arbitrary combinations of array shapes. For example, a (7,5)-shape array is incompatible with a shape-(11,3) array. Trying to add two such arrays would produce a `ValueError`. The following rules determine if two arrays are broadcast-compatible: 

<div class="alert alert-warning"> 

**Definition: Rules of Broadcasting**: 

To determine if two arrays are broadcast-compatible, align the entries of their shapes such that their trailing dimensions are aligned, and then check that each pair of aligned dimensions satisfy either of the following conditions:

- the aligned dimensions have the same size
- one of the dimensions has a size of 1   

The two arrays are broadcast-compatible if either of these conditions are satisfied for each pair of aligned dimensions.

</div>


Note that it is okay to have one array with a higher-dimensionality and thus to have "dangling" leading dimensions. Any size-1 dimension or "missing" dimension will be filled-in by broadcasting the content of that array.

Considering the example from the preceding subsection, let's see that the shape-(4,3) and shape-(3,) arrays satisfy these rules for broadcast-compatibility:
```
     array-1: 4 x 3
     array-2:     3
result-shape: 4 x 3
```

Let's look an assortment of pairs of array-shapes and see whether or not they are broadcast-compatible:

```
     array-1:         8
     array-2: 5 x 2 x 8
result-shape: 5 x 2 x 8

     array-1:     5 x 2
     array-2: 5 x 4 x 2
result-shape: INCOMPATIBLE

     array-1:     4 x 2
     array-2: 5 x 4 x 2
result-shape: 5 x 4 x 2

     array-1: 8 x 1 x 3
     array-2: 8 x 5 x 3
result-shape: 8 x 5 x 3

     array-1: 5 x 1 x 3 x 2
     array-2:     9 x 1 x 2
result-shape: 5 x 9 x 3 x 2

     array-1: 1 x 3 x 2
     array-2:     8 x 2 
result-shape: INCOMPATIBLE

     array-1: 2 x 1
     array-2:     1  
result-shape: 2 x 1
```


<!-- #region -->
NumPy provides the function [broadcast_to](https://docs.scipy.org/doc/numpy/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to), which can be used to broadcast an array to a specified shape. This can help us build our intuition for broadcasting. Let's broadcast a shape-(3,4) array to a shape-(2,3,4) array:

```python
# Demonstrating `np.broadcast_to`
>>> x = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11]])

# Explicitly broadcast a shape-(3,4) array 
# to a shape-(2,3,4) array.
>>> np.broadcast_to(x, (2, 3, 4))
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],

       [[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]]])
```
<!-- #endregion -->

<div class="alert alert-info"> 

**Reading Comprehension: Broadcast Compatibility**

Given the following pairs of array-shapes, determine what the resulting broadcasted shapes will be. Indicate if a pair is broadcast-incompatible. 

1\. `7 x 2` with `7`

2\. `4` with `3 x 4`

3\. `1 x 3 x 1` with `8 x 1 x 1`

4\. `9 x 2 x 5` with `2 x 5`

5\. `3` with `3 x 3 x 2`

</div>

<!-- #region -->
## A Simple Application of Array Broadcasting
Here we provide a simple real-world example where broadcasting is useful. Suppose you have a grade book for 6 students, each of whom have taken 3 exams; naturally, you store these scores in a shape-(6,3) array:

```python
# grades for 6 students who have taken 3 exams
# axis-0 (rows):    student
# axis-1 (columns): exams 
>>> import numpy as np
>>> grades = np.array([[ 0.79,  0.84,  0.84],
...                    [ 0.87,  0.93,  0.78],
...                    [ 0.77,  1.00,  0.87],
...                    [ 0.66,  0.75,  0.82],
...                    [ 0.84,  0.89,  0.76],
...                    [ 0.83,  0.71,  0.85]])
```

We might be interested to see how each of these scores compare to the mean score for that specific exam. Based on our discussion from the last section, we can easily compute the mean-score for each exam (rounded to 2 decimal places):

```python
# compute the mean score for each exam (rounded to 2 decimal places)
>>> mean_exam_scores = grades.mean(axis=0)
>>> mean_exam_scores = np.round(mean_exam_scores, 2)
>>> mean_exam_scores
array([ 0.79,  0.85,  0.82])
```

`grades` is a shape-(6,3) array and `mean_exam_scores` is a shape-(3,) array, and we want to compute the offset of each exam score from its respective mean. At first glance, it seems like we will have to loop over each row of our `grades` array and subtract from it the `mean_exam_scores`, to compute the offset of each exam score from the respective mean-score:
```python
# Using a for-loop to compute score offsets.

# Shape-(6,3) array that will store (score - mean) for each
# exam score.
score_offset = np.zeros_like(grades)

# iterates over each row of `grades`
for n, scores_per_student in enumerate(grades):
    # `scores_per_student` is a shape-(3,) array of exam scores
    # for a given student. This matches the shape of
    # `mean_exam_scores`, thus we can perform this subtraction
    score_offset[n] = scores_per_student - mean_exam_scores
```

Given our discussion of vectorized operations from the last section, you should recoil at the sight of a for-loop in code that is performing array-arithmetic. We might as well get out our abacuses and spreadsheets at this point. Fortunately, we can make use of broadcasting to compute these offsets in a concise, vectorized way:
```python
# Using broadcasting to subtract a shape-(3,) array
# from a shape-(6,3) array.
>>> score_offset = grades - mean_exam_scores
>>> score_offset
array([[ 0.  , -0.01,  0.02],
       [ 0.08,  0.08, -0.04],
       [-0.02,  0.15,  0.05],
       [-0.13, -0.1 ,  0.  ],
       [ 0.05,  0.04, -0.06],
       [ 0.04, -0.14,  0.03]])
```
<!-- #endregion -->

According to the broadcasting rules detailed above, when you invoke `grades - mean_exam_scores`, NumPy will recognize that `mean_exam_scores` has the same shape as each row of `grades` and thus it will apply the subtraction operation on *each* row of `grades` with `mean_exam_scores`. In effect, the content of `mean_exam_scores` has been *broadcasted* to fill a shape-(6,3) array, so that the element-wise subtraction can be performed. Again, we emphasize that NumPy doesn't actually unnecessarily replicate the data of `mean_exam_scores`, and that this model of broadcasting merely conveys the mathematical process that is transpiring.


<div class="alert alert-info"> 

**Reading Comprehension: Basic Broadcasting**

Generate a random array of 10,000 2D points using `np.random.rand`. Compute the "center of mass" of these points, which is simply the average x-coordinate and the average y-coordinate of these 10,000 points. Then, use broadcasting to compute the shape-(10000,2) array that stores the position of the points *relative* to the center of mass. For example, if the center of mass is $(0.5, 1)$, and the absolute position of a point is $(2, 3)$, then the position of that point *relative* to the center of mass is simply $(2, 3) - (0.5, 1) = (1.5, 2)$

</div>

<!-- #region -->
## Size-1 Axes & The `newaxis` Object 

### Inserting Size-1 Dimensions into An Array
As conveyed by the broadcasting rules, dimensions of size-1 are special in that they can be broadcasted to any size. Here we will learn about introducing size-1 dimensions into an array, for the purpose of tailoring its shape for broadcasting. 

You can introduce size-1 dimensions to an array without changing the overall size (i.e. total number of entries in an array. Thus we are free to add size-1 dimensions to an array via the `reshape` function. Let's reshape a shape-(3,) array into a shape-(1, 3, 1, 1) array:
```python
>>> import numpy as np

# Reshaping an array to introduce size-1 dimensions.
# The size of the array is 3, regardless of introducing
# these extra size-1 dimensions.
>>> np.array([1, 2, 3]).reshape(1, 3, 1, 1)
array([[[[1]],

        [[2]],

        [[3]]]])
```

Thus the 1-D array with three entries has been reshaped to possess 4-dimensions: "one stack of three sheets, each containing a single row and column". There is another way to introduce size-1 dimensions. NumPy provides the `newaxis` object for this purpose. Let's immediately demonstrate how `np.newaxis` can be used:
```python
# demonstrating the usage of the `numpy.newaxis` object
>>> x= np.array([1, 2, 3])
>>> y= x[np.newaxis, :, np.newaxis, np.newaxis]
>>> y
array([[[[1]],

        [[2]],

        [[3]]]])
>>> y.shape
(1, 3, 1, 1)
```

Indexing `x` as `x[np.newaxis, :, np.newaxis, np.newaxis]` returns a "view" of `x` as a 4D array with size-1 dimensions inserted as axes 0, 2, and 3. The resulting array is not a copy of `x`; it points to the exact same data as `x`, but merely with a different indexing layout. This is no different than what we achieved via reshaping: `x.reshape(1, 3, 1, 1)`. 
<!-- #endregion -->

<!-- #region -->
### Utilizing Size-1 Dimensions for Broadcasting
Moving on to a more pressing matter: why would we ever want to introduce these spurious dimensions into an array? Let's take an example to demonstrate the utility of size-1 dimensions. 

Suppose that we want to multiply all possible pairs of entries between two arrays: `array([1, 2, 3])` with `array([4, 5, 6, 7])`. That is, we want to perform twelve multiplications, and have access to each result. At first glance, combining a shape-(3,) array with a shape-(4,) array seems inadmissible for broadcasting; we seem to be doomed to perform nested for-loops like a bunch of cavemen and cavewomen. Fortunately, we can make clever use of size-1 dimensions so that we can perform this computation in a vectorized way. 

Let's introduce size-1 dimensions into `x`:

```python
# Inserting size-1 dimensions into `x` and `y` in 
# preparation of broadcasting.
>>> x_1d = np.array([1, 2, 3]) 
>>> x = x_1d.reshape(3, 1)
>>> x
array([[1],
       [2],
       [3]])

>>> y = np.array([4, 5, 6, 7])
```

`x` is now a shape-(3, 1) array and `y` is a shape-(4,) array. According to the broadcasting rules, these arrays are broadcast-compatible and will multiply to produce a shape-(3, 4) array. Let's see that multiplying these two arrays will exactly produce the twelve numbers that we are after:

```python
# broadcast-multiplying `x` and `y`
>>> x * y
array([[ 4,  5,  6,  7],
       [ 8, 10, 12, 14],
       [12, 15, 18, 21]])
```
<!-- #endregion -->

\begin{equation}
\left(
\begin{array}{*{1}{X}}
  1 \\
  2 \\
  3
\end{array} \right)
% 
\cdot \left( \begin{array}{*{4}{X}}
  4 & 5 & 6 & 7
\end{array}\right)
% 
\rightarrow \left( \begin{array}{*{4}{X}}
  1 & 1 & 1 & 1 \\
  2 & 2 & 2 & 2 \\
  3 & 3 & 3 & 3
\end{array}\right)
%
\cdot \left( \begin{array}{*{4}{X}}
  4 & 5 & 6 & 7 \\
  4 & 5 & 6 & 7 \\
  4 & 5 & 6 & 7
\end{array}\right)
%
= \left( \begin{array}{*{4}{X}}
  1\cdot4 & 1\cdot5 & 1\cdot6 & 1\cdot7 \\
  2\cdot4 & 2\cdot5 & 2\cdot6 & 2\cdot7 \\
  3\cdot4 & 3\cdot5 & 3\cdot6 & 3\cdot7
\end{array}\right)
\
\end{equation}


See that entry `(i, j)` of the resulting array corresponds to `x_1d[i] * y[j]`. 

Through the use of simple reshaping, shrewdly inserting size-1 dimensions allowed us to coerce NumPy into performing exactly the combination-multiplication that we desired. Furthermore, a keen understanding of what broadcasting is provides us with a clear interpretation of the structure of the result of this calculation. That is, if I reshape `x` to be a shape-$(M, 1)$ array, and `y` is a shape-$(N,)$ array, then (according to broadcasting rules) `x * y` would produce a shape-$(M, N)$ array storing the product of each of `x`'s $M$ numbers with each of `y`'s $N$ numbers. 

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Basic Broadcasting II**

Given the shape-(2,3,4) array:
```python
>>> x = np.array([[[ 0,  1,  2,  3],
...                [ 4,  5,  6,  7],
...                [ 8,  9, 10, 11]],
...
...               [[12, 13, 14, 15],
...                [16, 17, 18, 19],
...                [20, 21, 22, 23]]])
```

Normalize `x` such that *each of its rows, within each sheet, will sum to a value of 1*. Make use of the sequential function `np.sum`, which should be called only once, and broadcast-division.

</div>
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-info"> 

**Reading Comprehension: Basic Broadcasting III**

A digital image is simply an array of numbers, which instructs a grid of pixels on a monitor to shine light of specific colors, according to the numerical values in that array. 

An RGB-image can thus be stored as a 3D NumPy array of shape-$(V, H, 3)$. $V$ is the number of pixels along the vertical direction, $H$ is the number of pixels along the horizontal, and the size-3 dimension stores the red, blue, and green color values for a given pixel. Thus a $(32, 32, 3)$ array would be a 32x32 RBG image.

You often work with a collection of images. Suppose we want to store N images in a single array; thus we now consider a 4D shape-(N, V, H, 3) array.  For the sake of convenience, let's simply generate a 4D-array of random numbers as a placeholder for real image data. We will generate 500, 48x48 RGB images:

```python
>>> images = np.random.rand(500, 48, 48, 3)

```

Using the sequential function `np.max` and broadcasting, normalize `images` such that the largest value within *each color-channel of each image* is 1.

</div> 
<!-- #endregion -->

<!-- #region -->
## An Advanced Application of Broadcasting: Pairwise Distances
We will conclude this section by demonstrating an important, non-trivial example of array broadcasting. Here, we will find that the most straightforward use of broadcasting is *not* necessarily the right solution for our problem, and we will see that it can be important to first refactor the mathematical approach taken to perform a calculation before using broadcasting. Specifically, we will see that our initial approach for using of broadcasting is memory-inefficient.

Suppose we have two, 2D arrays. `x` has a shape of $(M, D)$ and `y` has a shape of $(N, D)$. We want to compute the Euclidean distance (a.k.a. the $L_2$-distance) between *each pair* of rows between the two arrays. That is, if a given row of `x` is represented by $D$ numbers $(x_0, x_1, \ldots, x_{D-1})$, and similarly, a row `y` is represented by $(y_0, y_1, \ldots, y_{D-1})$, and we want to compute the Euclidean distance between the two rows:

\begin{equation}
\sqrt{(x_{0} - y_{0})^2 + (x_{1} - y_{1})^2 + \ldots + (x_{D-1} - y_{D-1})^2} = \sqrt{\sum_{i=0}^{D-1}{(x_{i} - y_{i})^2}}
\end{equation}

Doing this for each pair of rows should produce a total of $M\times N$ distances. The previous subsection stepped us through a very similar calculation, albeit with lower-dimensional arrays. Let's proceed by performing this computation in three different ways:

1. Using explicit for-loops
2. Using straight-forward broadcasting
3. Refactoring the problem and then using broadcasting

For the sake of being concrete, we will compute all of the pairwise Euclidean distances between the rows of these two arrays: 
```python
# a shape-(5, 3) array
>>> x = np.array([[ 8.54,  1.54,  8.12],
...               [ 3.13,  8.76,  5.29],
...               [ 7.73,  6.71,  1.31],
...               [ 6.44,  9.64,  8.44],
...               [ 7.27,  8.42,  5.27]])

# a shape-(6, 3) array
>>> y = np.array([[ 8.65,  0.27,  4.67],
...               [ 7.73,  7.26,  1.95],
...               [ 1.27,  7.27,  3.59],
...               [ 4.05,  5.16,  3.53],
...               [ 4.77,  6.48,  8.01],
...               [ 7.85,  6.68,  6.13]])

```

Thus we will want to compute a total of 30 distances, one for each pair of rows from `x` and `y`.
<!-- #endregion -->

<!-- #region -->
### Pairwise Distances Using For-Loops
Performing this computation using for-loops proceeds as follows:

```python
def pairwise_dists_looped(x, y):
    """  Computing pairwise distances using for-loops

         Parameters
         ----------
         x : numpy.ndarray, shape=(M, D)
         y : numpy.ndarray, shape=(N, D)

         Returns
         -------
         numpy.ndarray, shape=(M, N)
             The Euclidean distance between each pair of
             rows between `x` and `y`."""
    # `dists[i, j]` will store the Euclidean 
    # distance between  `x[i]` and `y[j]`
    dists = np.empty((5, 6))

    for i, row_x in enumerate(x):     # loops over rows of `x`
        for j, row_y in enumerate(y): # loops over rows of `y`
            # Subtract corresponding entries of the rows,
            # squares each difference, and then sums them. This
            # exactly matches our equation for Euclidean 
            # distance (we will do the square root later)
            dists[i, j] = np.sum((row_x - row_y)**2)

    # we still need to take the square root of
    # each of our numbers
    return np.sqrt(dists)
```

Be sure to step through this code and see that `dists` stores each pair of Euclidean distances between the rows of `x` and `y`.
<!-- #endregion -->

<!-- #region -->
### Pairwise Distances Using Broadcasting (Unoptimized)
Now, let's use of vectorization to perform this distance computation. It must be established immediately that the method that we about to develop here is memory-inefficient. We will address this issue in detail at the end of this subsection.  

We start off our vectorized computation by shrewdly inserting size-1 dimensions into `x` and `y`, so that we can perform $M \times N$ subtractions between their pairs of length-$D$ rows. *This creates a shape-*$(M, N, D)$ *array*.

```python
# subtract shape-(5, 1, 3) with shape-(1, 6, 3)
# produces shape-(5, 6, 3)
>>> diffs = x.reshape(5, 1, 3) - y.reshape(1, 6, 3)
>>> diffs.shape
(5, 6, 3)
```

It is important to see, via broadcasting, that `diffs[i, j]` stores `x[i] - y[j]`. Thus we need to square each entry of `diffs`, sum over its last axis, and take the square root, in order to produce our $M \times N$ Euclidean distances:

```python
# producing the Euclidean distances
>>> dists = np.sqrt(np.sum(diffs**2, axis=2))
>>> dists.shape
(5, 6)
```

Voilà! We have produced the distances in a vectorized way. Let's write this out formally as a function:

```python
def pairwise_dists_crude(x, y):
    """  Computing pairwise distances using vectorization.
         
         This method uses memory-inefficient broadcasting.
         
         Parameters
         ----------
         x : numpy.ndarray, shape=(M, D)
         y : numpy.ndarray, shape=(N, D)
         
         Returns
         -------
         numpy.ndarray, shape=(M, N)
             The Euclidean distance between each pair of
             rows between `x` and `y`."""
    # The use of `np.newaxis` here is equivalent to our 
    # use of the `reshape` function
    return np.sqrt(np.sum((x[:, np.newaxis] - y[np.newaxis])**2, axis=2))
```

Regrettably, there is a glaring issue with the vectorized computation that we just performed. Consider the largest sized array that is created in the for-loop computation, compared to that of this vectorized computation. The for-loop version need only create a shape-$(M, N)$ array, whereas the vectorized computation creates an intermediate array (i.e. `diffs`) of shape-$(M, N, D)$. This intermediate array is even created in the one-line version of the code. This will create a massive array if $D$ is a large number!

Suppose, for instance, that you are finding the Euclidean between pairs of RGB images that each have a resolution of $32 \times 32$ (in order to see if the images resemble one another). Thus in this scenario, each image is comprised of $D = 32 \times 32 \times 3 = 3072$ numbers ($32^2$ pixels, and each pixel has 3 values: a red, blue, and green-color value). Computing all the distances between a stack of 5000 images with a stack of 100 images would form an intermediate array of shape-$(5000, 100, 3072)$. Even though this large array only exists temporarily, it would have to consume over 6GB of RAM! The for-loop version requires $\frac{1}{3027}$ as much memory (about 2MB).

Is our goose cooked? Are we doomed to pick between either slow for-loops, or a memory-inefficient use of vectorization?  No! We can refactor the mathematical form of the Euclidean distance in order to avoid the creation of that bloated intermediate array.    
<!-- #endregion -->

### Optimized Pairwise Distances
Performing the pairwise subtraction between the respective rows of `x` and `y` is what created the over-sized intermediate array in our previous calculation. Thus we want to rewrite the Euclidean distance equation such that none of the terms require broadcasting beyond the size of $M \times N$.

The Euclidean distance equation, ignoring the square root for now, can be refactored by multiplying out each squared term as so:

\begin{equation}
\sum_{i=0}^{D-1}{(x_{i} - y_{i})^2} = \sum_{i=0}^{D-1}{x_{i}^2} + \sum_{i=0}^{D-1}{y_{i}^2} - 2\sum_{i=0}^{D-1}{x_{i} y_{i}}
\end{equation}

Keep in mind that we must compute this for each pair of rows in `x` and `y`. We will find that this formulation permits the use of matrix multiplication, such that we can avoid forming the shape-$(M, N, D)$ intermediate array.

<!-- #region -->
The first two terms in this equation are straight-forward to calculate, and, when combined, will only produce a shape-$(M, N)$ array. For both `x` and `y`, we square each element in the array and then sum over the columns for each row:

```python
# Computing the first two terms of the 
# refactored Euclidean distance equation

# creates a shape-(5,) array
>>> x_sqrd_summed = np.sum(x**2, axis=1)

# creates a shape-(6,) array
>>> y_sqrd_summed = np.sum(y**2, axis=1)
```

We must insert a size-1 dimension in `x` so that we can add all pairs of numbers between the resulting shape-$(M, 1)$ and shape-$(N,)$ arrays. This will compute $\sum_{i=0}^{D-1}{x_{i}^2} + \sum_{i=0}^{D-1}{y_{i}^2}$ for all of the $M \times N$ pairs of rows:

```python
# add a shape-(5, 1) array with a shape-(6, ) array
# to create a shape-(5, 6) array
>>> x_y_sqrd = x_sqrd_summed[:, np.newaxis] + y_sqrd_summed
>>> x_y_sqrd.shape
(5, 6)
```

This leaves the third term to be computed. It is left to the reader to show that computing this sum of products for each pair of rows in `x` and `y` is equivalent to performing the matrix multiplication $-2\;(x \cdot y^{T})$, where `y` has been transposed so that it has a shape of $(D, N)$. This matrix multiplication of a shape-$(M, D)$ array with a shape-$(D, N)$ array produces a shape-$(M, N)$ array. Therefore, we can compute this final term without needing to create a larger, intermediate array.

Thus the third term in our equation, $-2\sum_{i=0}^{D-1}{x_{i} y_{i}}$, for all $M \times N$ pairs of rows, is:

```python
# computing the third term in the distance
# equation, for all pairs of rows
>>> x_y_prod = -2 * np.matmul(x, y.T)  # `np.dot` can also be used to the same effect
>>> x_y_prod.shape
(5, 6)
```

Having accounted for all three terms, we can finally compute the Euclidean distances: 

```python
# computing all the distances
>>> dists = np.sqrt(x_y_sqrd + x_y_prod)
>>> dists.shape
(5, 6)
```
In total, we have successfully used vectorization to compute the all pairs of distances, while only requiring an array of shape-$(M, N)$ to do so! This is the memory-efficient, vectorized form - the stuff that dreams are made of. Let's write the function that performs this computation in full.  

```python
def pairwise_dists(x, y):
    """ Computing pairwise distances using memory-efficient 
        vectorization.

        Parameters
        ----------
        x : numpy.ndarray, shape=(M, D)
        y : numpy.ndarray, shape=(N, D)

        Returns
        -------
        numpy.ndarray, shape=(M, N)
            The Euclidean distance between each pair of
            rows between `x` and `y`."""
    dists = -2 * np.matmul(x, y.T)
    dists +=  np.sum(x**2, axis=1)[:, np.newaxis]
    dists += np.sum(y**2, axis=1)
    return  np.sqrt(dists)
```


<!-- #endregion -->

<div class="alert alert-info">

**Takeaway**: 

The specific form of an equation can have a major impact on the memory-footprint of its vectorized implementation in NumPy. This issue can be safely overlooked in cases where you can be certain that the array shapes at play will not lead to substantial memory consumption. Otherwise, take care to study the form of the equation, to see if it can be recast in a way that alleviates its memory-consumption bottlenecks.

</div>


<div class="alert alert-info"> 

**Reading Comprehension: Checking the equivalence of the three pairwise distance functions**

Use the function [numpy.allclose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html) to verify that the three methods for computing the pairwise distances produce the same numerical results.

</div>


## Links to Official Documentation

- [Basics of broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html#broadcasting)
- [Broadcasting routines](https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html#changing-number-of-dimensions)


## Reading Comprehension Solutions

<!-- #region -->
**Basic Broadcasting: Solution**

Generating the random array of 10,000, 2D points, and their "center-of-mass".
```python
# find the mean x-coord and y-coord of the 10000 points
>>> pts = np.random.rand(10000, 2)
>>> center_of_mass = pts.mean(axis=0)  # -> array([mean_x, mean_y])
>>> center_of_mass.shape
(2,)

# Use broadcasting to compute the position of each point relative
# to the center of mass. The center of mass coordinates are subtracted
# from each of the 10000 points, via broadcast-subtraction
>>> relative_pos = pts - center_of_mass # shape-(10000,2) w/ shape-(2,)
>>> relative_pos.shape
(10000, 2)
```
<!-- #endregion -->

**Broadcast Compatibility: Solution**

1\. Incompatible

2\. `3 x 4`

3\. `8 x 3 x 1`

4\. `9 x 2 x 5`

5\. Incompatible

<!-- #region -->
**Basic Broadcasting II: Solution**

Normalize `x` such that *each of its rows, within each sheet, will sum to a value of 1*. Make use of the sequential function `np.sum`, which should be called only once, and broadcast-division.

```python
# a shape-(2, 3, 4) array
>>> x = np.array([[[ 0,  1,  2,  3],
...                [ 4,  5,  6,  7],
...                [ 8,  9, 10, 11]],
...
...               [[12, 13, 14, 15],
...                [16, 17, 18, 19],
...                [20, 21, 22, 23]]])

# sum along each of the three rows within each sheet
>>> summed_rows = x.sum(axis=2)
>>> summed_rows
array([[ 6, 22, 38],
       [54, 70, 86]])

# this shape-(2, 3) array can be broadcast-divided
# along the sheets and rows of `x`, if we insert a size-1 axis
# at dimension-2 of the summed array, where the columns used to
# be
>>> x_norm = x / summed_rows[:, :, np.newaxis]

# verifying the solution
>>> x_norm.sum(axis=2)
array([[1., 1., 1.],
       [1., 1., 1.]])
```
<!-- #endregion -->

<!-- #region -->
**Basic Broadcasting III: Solution**

```python
# a collection of 500 48x48 RGB images
>>> images = np.random.rand(500, 48, 48, 3)

# finding the max-value within each color-channel of each image
>>> max_vals = images.max(axis=(1,2))
>>> max_vals.shape
(500, 3)

# we can insert size-1 dimensions so that we can
# broadcast-divide these max-values with
# the pixels of the images.
# broadcasting (500, 48, 48, 3) with (500, 1, 1, 3)
>>> normed_images = images / max_vals.reshape(500, 1, 1, 3)

# checking that all the max-values are 1
>>> normed_images.max(axis=(1,2))
array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       ..., 
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.]])

# a rigorous check
>>> np.all(normed_images.max(axis=(1,2)) == 1)
True
```
<!-- #endregion -->

<!-- #region -->
**Checking the equivalence of the three pairwise distance functions: Solution**

`numpy.allclose` returns `True` if all pairwise elements between two arrays are almost-equal to one another.

```python
>>> x = np.array([[ 8.54,  1.54,  8.12],
...               [ 3.13,  8.76,  5.29],
...               [ 7.73,  6.71,  1.31],
...               [ 6.44,  9.64,  8.44],
...               [ 7.27,  8.42,  5.27]])

>>> y = np.array([[ 8.65,  0.27,  4.67],
...               [ 7.73,  7.26,  1.95],
...               [ 1.27,  7.27,  3.59],
...               [ 4.05,  5.16,  3.53],
...               [ 4.77,  6.48,  8.01],
...               [ 7.85,  6.68,  6.13]])

>>> np.allclose(pairwise_dists_looped(x, y), pairwise_dists_crude(x, y))
True

>>> np.allclose(pairwise_dists_crude(x, y), pairwise_dists(x, y))
True
```
<!-- #endregion -->
