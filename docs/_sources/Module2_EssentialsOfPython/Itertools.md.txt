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
   :description: Topic: simple use cases of python itertools, Difficulty: Easy, Category: Tutorial
   :keywords: itertools, examples, zip, range, enumerate, chain, combinations
<!-- #endraw -->

<!-- #region -->
# Python's "Itertools"
Python has an [itertools module](https://docs.python.org/3/library/itertools.html), which provides a core set of fast, memory-efficient tools for creating iterators. We will briefly showcase a few itertools here. The majority of these functions create [generators](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html), thus we will have to iterate over them in order to explicitly demonstrate their use. It is hard to overstate the utility of this module - it is strongly recommended that you take some time to see what it has in store.

There are three built-in functions, `range`, `enumerate`, and `zip`, that belong in itertools, but they are so useful that they are made accessible immediately and do not need to be imported. It is essential that `range`, `enumerate`, and `zip` become tools that you are comfortable using.

**range**

Generate a sequence of integers in the specified "range":
```python
# will generate 0.. 1.. 2.. ... 8.. 9
>>> range(10)
range(0, 10)

>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# will generate 0.. 3.. 6.. 9
>>> range(0, 10, 3)
range(0, 10, 3)

>>> list(range(0, 10, 3))
[0, 3, 6, 9]
```

**enumerate**

Enumerates the items in an iterable: yielding a tuple containing the iteration count (starting with 0) and the corresponding item from the the iterable.
```python
# will generate (0, 'apple').. (1, 'banana').. (2, 'cat').. (3, 'dog')]
>>> enumerate(["apple", "banana", "cat", "dog"])
<enumerate at 0x23e3557b3f0>

>>> list(enumerate(["apple", "banana", "cat", "dog"]))
[(0, 'apple'), (1, 'banana'), (2, 'cat'), (3, 'dog')]
```

**zip**

Zips together the corresponding elements of several iterables into tuples. This is valuable for "pairing" corresponding items across multiple iterables. 
```python
>>> names = ["Angie", "Brian", "Cassie", "David"]
>>> exam_1_scores = [90, 82, 79, 87]
>>> exam_2_scores = [95, 84, 72, 91]

# will generate ('Angie', 90, 95).. ('Brian', 82, 84).. ('Cassie', 79, 72).. ('David', 87, 91)]
>>> zip(names, exam_1_scores, exam_2_scores)
<zip at 0x20de1082608>

>>> list(zip(names, exam_1_scores, exam_2_scores))
[('Angie', 90, 95), ('Brian', 82, 84), ('Cassie', 79, 72), ('David', 87, 91)]
```
***
The following are some of the many useful tools provided by the `itertools` module:

**itertools.chain**

Chains together multiple iterables, end-to-end, forming a single iterable:
```python
>>> from itertools import chain
>>> gen_1 = range(0, 5, 2)               # 0.. 2.. 4
>>> gen_2 = (i**2 for i in range(3, 6))  # 9.. 16.. 25 
>>> iter_3 = ["moo", "cow"]
>>> iter_4 = "him"

# will generate: 0.. 2.. 4.. 9.. 16.. 25.. 'moo'.. 'cow'.. 'h'.. 'i'.. 'm'
>>> chain(gen_1, gen_2, iter_3, iter_4)
<itertools.chain at 0x20de109ec18>
```

**itertools.combinations**
Generate all length-n tuples storing "combinations" of items from an iterable:
```python
>>> from itertools import combinations

# will generate: (0, 1, 2).. (0, 1, 3).. (0, 2, 3).. (1, 2, 3)
>>> combinations([0, 1, 2, 3], 3)  # generate all length-3 combinations from [0, 1, 2, 3]
<itertools.combinations at 0x20de10a7728>
```
<!-- #endregion -->

<div class="alert alert-info">

**Reading Comprehension: Itertools I**

Using the `itertools.combinations` function, find the probability that two randomly drawn items from the list `["apples", "bananas", "pears", "pears", "oranges"]` would yield a combination of "apples" and "pears".

</div>


<div class="alert alert-info">

**Reading Comprehension: Itertools II**

Given the list `x_vals = [0.1, 0.3, 0.6, 0.9]`, create a generator, `y_gen`, that will generate the y-value $y = x^2$ for each value of $x$. Then, using `zip`, create a list of the $(x, y)$ pairs, each pair stored in a tuple.

</div>


## Links to Official Documentation

- [range](https://docs.python.org/3/library/stdtypes.html#typesseq-range)
- [enumerate](https://docs.python.org/3/library/functions.html#enumerate)
- [zip](https://docs.python.org/3/library/functions.html#zip)
- [itertools](https://docs.python.org/3/library/itertools.html)

<!-- #region -->
## Reading Comprehension: Solutions

**Itertools I: Solution**

```python
>>> from itertools import combinations
>>> ls = ["apples", "bananas", "pears", "pears", "oranges"]
>>> comb_ls = list(combinations(ls, 2))
>>> comb_ls.count(("apples", "pears")) / len(comb_ls)
0.2
```

<!-- #endregion -->

<!-- #region -->
**Itertools II: Solution**

```python
>>> x_vals = [0.1, 0.3, 0.6, 0.9]
>>> y_gen = (x**2 for x in x_vals)
>>> list(zip(x_vals, y_gen))
[(0.1, 0.01), (0.3, 0.09), (0.6, 0.36), (0.9, 0.81)]
```

In this instance, the use of `zip` is a bit contrived. We could have foregone creating `y_gen` by just using the following list-comprehension:
```python
>>> x_vals = [0.1, 0.3, 0.6, 0.9]
>>> [(x, x**2) for x in x_vals]
[(0.1, 0.01), (0.3, 0.09), (0.6, 0.36), (0.9, 0.81)]
```
<!-- #endregion -->
