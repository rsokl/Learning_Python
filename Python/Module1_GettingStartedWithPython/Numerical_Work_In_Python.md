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

<!-- #region -->
# Doing Numerical Work in Python

Python's elegant and flexible syntax makes it a particularly attractive language. However, this also makes Python considerably slower than other, more stringent languages (e.g., the C programming language). This is a non-issue in many circumstances. It is, however, a major roadblock when one is doing serious numerical work.

Fortunately, there are several packages that you can use in Python, which allow you to do mathematical computations that are actually executed behind the scenes in a faster language. Offloading the work to a different language allows the computations to become blazingly fast, and we, the programmers, can stick to writing Python. The two best packages for this (both of which are already packaged in Anaconda) are:

### NumPy

The fundamental package for scientific computing with Python. NumPy provides an N-dimensional array that can be used to represent, say, a large matrix of numbers. It also provides a huge number of mathematical functions that can operate on these arrays. It is crucial to note that these functions will actually be executed in C, so they are incredibly fast compared to the same functions written in vanilla Python. NumPy will be used throughout the machine learning component of the course.

Here is example code for summing the numbers 1-100 in NumPy:
```python
import numpy as np
numbers = np.arange(1, 101) # an array storing the numbers 1-100
numpy_result = numbers.sum()
```
<div class="alert alert-warning">

**Note**:

The version of NumPy that comes with Anaconda is further optimized with MKL. It is significantly faster than the version of NumPy that you would obtain by installing the package yourself.
</div>

### Numba

Numba gives you the power to speed up your applications with high-performance functions written directly in Python. Where NumPy restricts you to using NumPy functions on NumPy arrays, Numba allows you to write your own custom functions in Python and it will optimize your functions to get C-like efficiency. This isn't a magic bullet - Numba can "translate" only a small subset of the Python language thus far. You have to tailor your code to be "compatible" with Numba, which can be limiting. 

We will not be using this package in this course, but it is a tremendous tool that is becoming instrumental for doing numerical work in Python.

Here is example code for summing the numbers 1-100 in numba:
```python
import numba
@numba.njit
def sum_func():
    result = 0
    for i in range(1, 101):
        result += i
    return result
numba_result = sum_func()
```

## Ending Remarks and Summary
Using these packages can speed up numerical computations by hundreds or even thousands of times compared to pure Python. Your calculation that was taking an hour to complete now takes 3 seconds!

If you are interested in learning more about computational efficiency and Python, consider reading the article [Why Python is Slow](https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/). Note that this is **not required reading**, and that the article is quite advanced.

### Summary

- Python is slow for large numerical computations.
- Tools like NumPy and Numba allow you do fast numerical computations in Python by "secretly" doing the numerical work behind the scenes in a fast language, like C.
- We will be working with NumPy (but Numba is fantastic and very worthwhile to learn if you do any serious numerical work in Python).
- Both NumPy and Numba came with your installation of Anaconda
<!-- #endregion -->
