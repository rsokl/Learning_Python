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

<!-- #raw raw_mimetype="text/restructuredtext" -->
.. meta::
   :description: Topic: Data Structures, Difficulty: Medium, Category: Section
   :keywords: Big-O, complexity, efficiency, algorithm, interview preparation, list, tuple, sequence
<!-- #endraw -->

<!-- #region -->
# Data Structures (Part I): Introduction
Here we survey Python's built-in data structures. You should already be familiar with its lists and tuples, two data structures that facilitate working with sequential data. Two other critical, built-in data structures to be introduced are:

- dictionary: a mapping from "keys" to "values"
- sets: an unordered collection of items that can be used to perform set-algebraic operations (e.g. union and intersection) 

These data structures are not merely convenient constructs with some nice pre-written functionality; they also provide an interface to some optimized core utilities that have been written in C (or whatever language your Python interpreter is written in). For example, let's write a function that checks if an item is contained within an iterable:

```python
def is_in(seq, target):
    """ Returns True if `target` is contained in `seq`."""
    for item in seq:
        if item == target:
            return True
    return False
```

This function mirrors the C-algorithm that Python uses "under the hood" for checking for membership in a list (assuming you are using the CPython interpreter, which you almost definitely are). Because their function is implemented "at a lower level", and need not be interpreted, we expect it to be faster than ours:
```python
>>> x = [1, "moo", 3, True, 5, None, 7, 8]

>>> is_in(x, -1)  # takes 980 nanoseconds on my machine
False

>>> -1 in x       # takes 320 nanoseconds on my machine
False
```
Here, Python's built-in sequence-membership function is 3x faster than using our own function. Furthermore, it will be important to know the advantages provided by each of the data structures. For instance, testing for membership in a set is even faster than is checking for membership in a list:

```python
# test for membership in a list
>>> -1 in [1, "moo", 3, True, 5, None, 7, 8]  # takes 295 nanoseconds on my machine
False

# test for membership in a set
>>> -1 in {1, "moo", 3, True, 5, None, 7, 8}  # takes 65 nanoseconds on my machine
False
```
We get a 4.5x speedup in our membership test just by using a set instead of a list, because the use of a set permits Python to use an entirely different algorithm for checking for membership. On our end, we merely replaced square brackets with curly braces! Hopefully this is sufficient motivation for learning about Python's data structures and the algorithms that they utilize "under the hood".

<div class="alert alert-info">

**Takeaway**: 

Python's data structures come with a wealth of built-in functionality. Furthermore, understanding where each data structure "shines" is critical for writing efficient Python code. It is not necessary to memorize this information, but you should know that it exists and should be referenced frequently.
</div>
<!-- #endregion -->

<!-- #region -->
## Describing Algorithm Complexity
In order to meaningfully compare the relative efficiency of algorithms, it is useful to summarize how algorithms "scale" with problem size. Two sorting algorithms may be comparable when sorting tens of items, and yet they may have wildly different performances when sorting thousands of items. 

"Big-O" notation allows us to denote how an algorithm's run time scales against problem size. Specifically, it signifies the "worst-case scenario" performance of an algorithm. 

Let's take, for instance, the `is_in` function that we wrote at the beginning of this section. In it, we iterate over a collection to check if it contains a specific item. The worst-case scenario for this algorithm is when the item is not a member of the collection at all - we have to iterate over the entire collection before we can conclude that it does not possess our item. So if we increase the collection to be $n$ times larger in size, it should take $n$ times as long to iterate over it to determine that the item is not a member of the collection (again, dealing with the worst-case scenario). Because the worst-case scenario run time of `is_in` scales linearly with the size of the collection, $n$, we denote it's run time complexity, using big-O notation, as $\mathcal{O}(n)$.

Now suppose we did a truly terrible job writing a membership algorithm, and performed a nested iteration over our collection:

```python
def is_in_slow(seq, target):
    """ Returns True if `target` is contained in `seq`."""
    for item in seq:
        # for each item in seq, iterate over seq in its entirety!
        for item2 in seq:
            if item == target:
                return True
    return False
```

For each item in `seq` we iterate over `seq` again, thus in the worst-case scenario we need to iterate over $n$ items, $n$ separate times - a total of $n^{2}$ "steps" in our algorithm. Thus we would say that `is_in_slow` is a $\mathcal{O}(n^{2})$ algorithm: whereas doubling size of `seq` would increase the run time of our $\mathcal{O}(n)$ algorithm by a factor of 2 (linear scaling), it would increase the run time of this $\mathcal{O}(n^{2})$ algorithm by 4 (quadratic scaling).

Here is a more formal description of this notation:
<div class="alert alert-block alert-info"> 
**"Big-O" Notation**: Suppose that $n$ denotes the "size" of the input to an algorithm, and that the mathematical expression $f(n)$ describes how many computational steps the algorithm must take in its *worst-case scenario*, given that input. Then the algorithm's run time complexity can be denoted using the **"Big-O"** notation: $\mathcal{O}(f(n))$.
</div>

A few important notes:

- We only care about the "highest-order" term in $f(n)$. That is, $\mathcal{O}(n + n^{2})$ should just be written as $\mathcal{O}(n^{2})$.
- We never care about constant factors in our scaling. That is, even if an algorithm iterates over a sequence twice, its big-O complexity should be written as $\mathcal{O}(n)$, rather than $\mathcal{O}(2n)$.
- An algorithm whose run time *does not depend on the size of its input* is a $\mathcal{O}(1)$ algorithm. 
  - Example: a function that returns the second element from a list.
- There are more nuanced methods for analyzing algorithm complexity than solely considering the worst-case scenario, which can be overly pessimistic. Know that  "big-O" notation can be used to convey mean performance, [amortized](https://en.wikipedia.org/wiki/Amortized_analysis) performance, and other types of analysis. Here, we will simply stick to the worst-case analysis.
<!-- #endregion -->

<div class="alert alert-info">

**Takeaway**: 

We will be using the "big-O" notation, $\mathcal{O}(f(n))$, to summarize the performance of the algorithms used by Python's data structures. 
</div>


## Sequential Data Structures: Lists and Tuples
The "Sequence Types" section already introduced lists and tuples. Recall that both provide the same interface for accessing and summarizing the contents of a heterogeneous sequence of objects. However, a list can be mutated - updated, removed from, and added to - whereas a tuple cannot be mutated. Thus a list is *mutable*, whereas a tuple is *immutable*. Here you will find a summary of the algorithmic complexities of many of the built-in functions that work on sequential data structures.

For a complete rundown of the functions available to Python's list, go [here](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).

#### List/Tuple Complexities
Let `seq` represent a **list or tuple** of length $n$; $i$ and $j$ are integers drawn randomly from the interval $[0, n-1]$; $k$ is the length of any subsequence involved in the operation. The following is a summary of the complexities associated with various common operations using lists and tuple (according to their implementations in CPython):

|Operation| Complexity | Explanation |
|---|---|---|
|`len(seq)`|O(1)| Return the number of items in the sequence |
|`seq[i]`| O(1) | Retrieve any item from the sequence |
|`seq[i:j]`| O(k) | Retrieve a length-k slice from the sequence |
|`for item in seq..`| O(n) | Iterate over the sequence |
|`obj in seq`| O(n) | Check if `obj` is a member of `seq` |
|`seq.count(obj)`| O(n) | Count the number of occurrences of `obj` in `seq` |
|`seq.index(obj)`| O(n)| Return position-index of `obj` in `seq` |


#### List Complexities
Here we consider some mutating operations, like `append`, that are available to lists and not tuples. It is important to note that lists are implemented such that: 

- operations that add-to or remove-from the *end* of the list are $\mathcal{O}(1)$
- operations that add-to or remove-from the *beginning* of the list are $\mathcal{O}(n)$

Let `my_list` represent a list of length $n$, and `i` is an integer drawn randomly from the interval $[0, n-1]$. The following is a summary of the complexities associated with various operations using a list (according to its implementation in CPython):

|Operation| Complexity | Explanation |
|---|---|---|
|`my_list[i] = obj`| O(1) | Set the ith entry of the list with a new object. |
|`my_list.append(obj)`| O(1) | Append a new object to the end of the list. |
|`my_list.pop()`| O(1) | Remove the object from the *end* of the list. |
|`my_list.pop(0)`| O(n) | Remove the object from the *beginning* of the list. |
|`my_list.sort()`| O(nlog(n)) | Return a sorted version of the list. |

