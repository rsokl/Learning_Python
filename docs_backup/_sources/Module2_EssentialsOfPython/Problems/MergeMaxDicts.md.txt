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
   :description: Topic: Dictionary Merge Exercise, Difficulty: Easy, Category: Practice Problem
   :keywords: dictionary, merge, practice problem
<!-- #endraw -->

<!-- #region -->
# Merging Two Dictionaries
> Merge two [dictionaries](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_II_Dictionaries.html#Data-Structures-(Part-II):-Dictionaries) together such that the resulting dictionary always retain the *greater* value among mappings with common keys. 

Here's an example:

```python
# merging two dictionaries, retaining the greatest value among
# common keys
>>> dict1 = {'bananas': 7, 'apples': 3, 'pears': 14}
>>> dict2 = {'bananas': 3, 'apples': 6, 'grapes': 9}
>>> merge_max_mappings(dict1, dict2)
{'bananas': 7, 'apples': 6, 'pears': 14, 'grapes': 9}
```

Write a function that accepts two dictionaries and merges them in the fashion shown above. The [dictionaries' keys need not be strings](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_II_Dictionaries.html#What-Can-a-Dictionary-Store?), and the values should be any data type that can be ordered (e.g. can be compared using the inequality operators `<`, `>`, etc.).
<!-- #endregion -->

<!-- #region -->
## A Simple, Buggy Solution
Let's begin by writing a straightforward but flawed solution to our problem. The following function will correctly merge its two input dictionaries and is generally well-written, however, something insidious is afoot... Can you identify the bad behavior that will result from this function? 

```python
def buggy_merge_max_mappings(dict1, dict2):
    # create the output dictionary, which contains all 
    # the mappings from `dict1`
    merged = dict1
     
    # populate `merged` with the mappings in dict2 if:
    #   - the key doesn't exist in `merged`
    #   - the value in dict2 is larger
    for key in dict2: 
        if key not in merged or dict2[key] > merged[key]:
            merged[key] = dict2[key]
    return merged
```
Let's first see what this function does right. Recall that [iterating over a dictionary](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_II_Dictionaries.html#Inspecting-a-Dictionary) will produce each of its keys one-by-one. Thus `for key in dict2` loops over every key in `dict2`. We then set a key-value from `dict2` mapping in `merged` if that key doesn't exist in merged or if the value is larger than the one stored in existing mapping. Given that `merged` is initialized to have the same mappings as `dict1`, this is a correct algorithm for merging our two dictionaries based on max-value.

The problem with our function is that we inadvertently merge `dict2` *into* `dict1`, rather than merging the two dictionaries into a *new* dictionary. Recall that dictionaries are [mutable](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Variables_and_Assignment.html#Referencing-a-Mutable-Object-with-Multiple-Variables) objects and that the statement `merged = dict1` simply assigns a variable that references `dict1` rather than creating a new copy of the dictionary. Thus calling this function will *mutate* (change) the state of `dict1`, as demonstrated here:
```python
>>> exam_1 = dict(Alice=99, Bob=87, Cindy=65)  # equivalent to {'Alice': 99, 'Bob': 87, 'Cindy': 65}
>>> exam_2 = dict(Alice=77, Bob=90, Cindy=78)
>>> buggy_merge_max_mappings(exam_1, exam_2)
{'Alice': 99, 'Bob': 90, 'Cindy': 78}
```
See that the value of `exam_1` has changed, and that it matches the output of our function:
```python
>>> exam_1
{'Alice': 99, 'Bob': 90, 'Cindy': 78}
```

To reiterate, this is because the statement `merged = dict1` found at the beginning of our function *merely creates a reference to* `dict1`, not a copy of it. In the above example `exam_1` stored a class' exam-1 scores for each student. After passing it to our function, it now stores the max score for each student across two exams! 

While we are likely to have tested that our function properly merges dictionaries as we desire, we are less likely to test that it leaves its inputs unchanged. This is a valuable lesson to be l
<!-- #endregion -->

<div class="alert alert-info">

**Takeaway**

- Be mindful of [object mutability](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Variables_and_Assignment.html#Mutable-&-Immutable-Types-of-Objects) and take care never to unwittingly mutate an input variable or global scope variable within a function. 
- When testing a function, include a check that the function does not mutate its inputs.

</div>

<!-- #region -->
## A Simple, Correct Solution

We can easily stomp the bug in the previous function; updating `merged = dict1` with either `merged = dict(dict1)` or `merged = dict1.copy()` will ensure that `merged` references a *new* dictionary, which we are free to update:

```python
def simple_merge_max_mappings(dict1, dict2):
    """ Merges two dictionaries based on the largest value in a given mapping.

    Parameters
    ----------
    dict1 : Dict[Any, Comparable]
    dict2 : Dict[Any, Comparable]
    
    Returns
    -------
    Dict[Any, Comparable]
        The merged dictionary
    """
    merged = dict(dict1)
    for key in dict2: 
        if key not in merged or dict2[key] > merged[key]:
            merged[key] = dict2[key]
    return merged
```

Note the use of simple and descriptive variables (e.g. we use the variable name `key` when we iterate over the keys of a dictionary). This, along with a good docstring, makes our code easy to read, understand, and debug. Also note that our code is general: it makes no presumptions about the dictionaries' keys - they need not be strings nor of any other particular type. Similarly, the only constraint on the dictionaries' values is that they can be compared against one another. This is reflected in the docstring of our function.

Consider the importance of the ordering of the conditional statement:

```python
if key not in merged or dict2[key] > merged[key]:
```

What is different if we flip the ordering of the terms? I.e.:

```python
if dict2[key] > merged[key] or key not in merged:
```

The problem with this flipped ordering is that the given key may not exist in `merged` yet, thus `dict2[key] > merged[key]` will raise a `KeyError`. Using the original ordering, such a case would cause `key not in merged` to return `True`, and the overall expression will return `True` without evaluating the second part of the expression (convince yourself that `True or <whatever>` will always return `True`). 
<!-- #endregion -->

<!-- #region -->
## A Minor Optimization

Supposing that your code makes heavy use of dictionary merging and that its performance is a bottleneck for the overall performance of your code, then there is a minor optimization that we can implement.

Consider a case of extreme imbalance in the sizes of our dictionaries; suppose `dict1` is contains one key while `dict2` contains 10,000. It would be preferable for our solution to manually iterate over the smaller of these two dictionaries. We can easily accommodate this in our function by choosing `merged` to be the longer of the two dictionaries and iterating over the other dictionary:

```python
def opt_merge_max_mappings(dict1, dict2):
    """ Merges two dictionaries based on the largest value in a given mapping.

    Parameters
    ----------
    dict1 : Dict[Any, Comparable]
    dict2 : Dict[Any, Comparable]

    Returns
    -------
    Dict[Any, Comparable]
        The merged dictionary
    """
    # we will iterate over `other` to populate `merged`
    merged, other = (dict1, dict2) if len(dict1) > len(dict2) else (dict2, dict1) 
    merged = dict(merged)
    
    for key in other: 
        if key not in merged or other[key] > merged[key]:
            merged[key] = other[key]
    return merged
```

Here, we make keen use of a [inline if-else statement](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/ConditionalStatements.html#Inline-if-else-statements) and [iterable unpacking](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html#%E2%80%9CUnpacking%E2%80%9D-iterables), which helps keep our code succinct despite the logic that we have added to it. See that

```python
merged, other = (dict1, dict2) if len(dict1) > len(dict2) else (dict2, dict1) 
```

is equivalent to:
```python
if len(dict1) < len(dict2):
    merged = dict1
    other = dict2
else:
    merged = dict2
    other = dict1
```

We can use the `timeit` [magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html) in either a Jupyter  notebook or an IPython console to time our functions (Note: each `timeit` must be run in a separate notebook cell, and `%%timeit` must be the topmost command in the cell).

```python
a = {}
b = dict(zip(range(10000), range(10000)))  # {1 : 1, 2: 2, ..., 9999:9999}
```

```python
%%timeit
simple_merge_max_mappings(a, b)
2.05 ms ± 90.6 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

```python
%%timeit
opt_merge_max_mappings(a, b)
455 µs ± 12.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

This is a relatively small speedup despite the rather stark example we cooked up.
<!-- #endregion -->

<!-- #region -->
## Extended Problem: Merging Arbitrary Numbers of Dictionaries

There is no reason that our function should only be able to merge two dictionaries, it should be easy to accommodate an arbitrary number of inputs:

```python
>>> a = dict(a=0, b=100, c=3)
>>> b = dict(a=10, b=10)
>>> c = dict(c=50)
>>> d = dict(d=-70)
>>> e = dict()
>>> merge_max_mappings(a, b, c, d, e)
{'a': 10, 'b': 100, 'c': 50, 'd': -70}
```

Before you write your solution, consider the following:
1. How do you write a function signature so that it can handle an arbitrary number of input dictionaries?
2. How should your function handle zero inputs? How about one input?
<!-- #endregion -->

<!-- #region -->
## Generalized Solution
Addressing point #1, we will want to use the `*args` syntax in our function signature so that [it can accommodate an arbitrary number of dictionaries](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Functions.html#Accommodating-an-Arbitrary-Number-of-Positional-Arguments). Thus all of the dictionaries fed to our function will be packed into a tuple that can be accessed via `args` (or whatever variable name we use in our signature).

Regarding point #2, we can handle the case of receiving no inputs by simply returning an empty dictionary. We will also see that handling the case of a single input is more subtle than one might guess. This point will be discussed further once the solution is presented.

Our solution is to create an empty dictionary, `merged`, and to simply iterate over each mapping of each input dictionary and perform our merging as we did above:

```python
def merge_max_mappings(*dicts):
    """ Merges an arbitrary number of dictionaries based on the 
    maximum value in a given mapping.
    
    Parameters
    ----------
    dicts : Dict[Any, Comparable]
    
    Returns
    -------
    Dict[Any, Comparable]
        The merged dictionary
    """
    merged = {}
    for d in dicts:  # `dicts` is a tuple storing the input dictionaries
        for key in d: 
            if key not in merged or d[key] > merged[key]:
                merged[key] = d[key]
    return merged
```
<!-- #endregion -->

<!-- #region -->
### Handling Zero Inputs
See that our function returns an empty dictionary if it is not passed any inputs, this is because `dicts` will be an empty tuple and thus our loop over it will immediately exit, returning an unpopulated `merged`:
```python
>>> merge_max_mappings()
{}
```
While you may have thought to have returned `None` in the case of there being no dictionaries to merge, returning an empty dictionary is much better behavior as code downstream from our function will only need to accommodate one type of output. Additionally, our function's docstring promises that it will return a dictionary and we should always abide by this contract.

### Handling One Input
In the case that our function is passed a single dictionary, our function effectively makes a (shallow) copy of that dictionary and returns it. Suppose we tried to be clever and wrote our function to pass a single dictionary through; e.g.

```python
def bad_merge_max_mappings(*dicts):
    if len(dicts) == 1:
        return dicts[0]
    merged = {}
    for d in dicts:
        for key in d: 
            if key not in merged or d[key] > merged[key]:
                merged[key] = d[key]
    return merged
```

What is wrong with this solution? The problem is similar to the one that we considered above; our function always returns a dictionary that is independent from its inputs, meaning that mutating the merged dictionary has no impact on any of the inputs dictionaries. This is no longer the case when we receive a single dictionary - here the "merged" dictionary is simply a reference to the input. Any subsequent mutation of the output dictionary will also mutate the input dictionary, and vice versa. This unanticipated behavior could create very hard-to-find bugs in your code!

It is best to not try to handle specialized cases like this, when the general code behaves appropriately to begin with.
<!-- #endregion -->

## Extra Challenges
- Write tests for your functions where the dictionary keys aren't strings and the values aren't numbers. 
- What if you wanted to merge values based on a criterion other than the maximum value? Try rewriting the function so that a comparison function can passed in as an argument. Remember that functions, once defined, are objects just like integers and strings - they can be passed as arguments into other functions.

<!-- #region -->
The following code is correct, but really bad:

```python
def gross_merge_max_mappings(*dicts):
    """merges dicts"""
    merged = {}
    for i in range(len(dicts)):
        for j in dicts[i]: 
            if not (j in list(merged)):
                merged[j] = dicts[i][j]
            elif dicts[i][j] > merged[j]:
                merged[j] = dicts[i][j]
            else:
                continue
    return merged
```
Compare this code to the solution that we devised, and enumerate all of the stylistic mistakes that are made here. Appreciate how simple and readable our code is by comparison and make a promise to yourself that you will not write code like this.
<!-- #endregion -->
