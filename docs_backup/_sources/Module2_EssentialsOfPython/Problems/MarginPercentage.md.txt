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
   :description: Topic: Within Margin Exercise, Difficulty: Medium, Category: Practice Problem
   :keywords: function, control flow, comparisons, practice problem
<!-- #endraw -->

<!-- #region -->
# Within Margin Percentage

>An algorithm is required to test out what percentage of the parts that a factory is producing fall within a safety margin of the design specifications. Given a list of values recording the metrics of the manufactured parts, a list of values representing the desired metrics required by the design, and a margin of error allowed by the design, compute what fraction of the values are within the safety margin (`<=`)

``` Python
# example behavior
>>> within_margin_percentage(desired=[10.0, 5.0, 8.0, 3.0, 2.0],
...                          actual= [10.3, 5.2, 8.4, 3.0, 1.2],
...                          margin=0.5)
0.8
```

See that $4/5$ of the values fall within the margin of error: $1.2$ deviates from $2$ by more than $0.5$. 

Complete the following function; consider the edge case where `desired` and `actual` are empty lists.

```python
def within_margin_percentage(desired, actual, margin):
    """ Compute the percentage of values that fall within
        a margin of error of the desired values
        
        Parameters
        ----------
        desired: List[float]
            The desired metrics
        
        actual: List[float]
            The corresponding actual metrics. 
            Assume `len(actual) == len(desired)`
        
        margin: float
            The allowed margin of error
        
        Returns
        -------
        float
            The fraction of values where |actual - desired| <= margin
    """
    # YOUR CODE HERE
    pass
```

You will want to be familiar with [comparison operators](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/ConditionalStatements.html#Comparison-Operations), [control flow](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Introduction.html), and [indexing lists](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/SequenceTypes.html#Introducing-Indexing-and-Slicing) lists to solve this problem.

## Solution
This problem can solved by simply looping over the pairs of actual and desired values and tallying the pairs that fall within the margin:
``` Python
def within_margin_percentage(desired, actual, margin):
    """ Compute the percentage of values that fall within
        a margin of error of the desired values
        
        Parameters
        ----------
        desired: List[float]
            The desired metrics
        
        actual: List[float]
            The actual metrics
        
        margin: float
            The allowed margin of error
        
        Returns
        -------
        float
            The fraction of values where |actual - desired| <= margin
    """
    count = 0  # tally of how values are within margin
    total = len(desired)
    for i in range(total):
        if abs(desired[i] - actual[i]) <= margin:
            count += 1  # Equivalent to `count = count + 1`
    return count / total if total > 0 else 1.0
```

See that we handle the edge case where `desired` and `actual` are empty lists: the [inline if-else statement](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/ConditionalStatements.html#Inline-if-else-statements) `count / total if total > 0 else 1` will return `1` when `total` is 0: 
```python
>>> within_margin_percentage([], [], margin=0.5)
1.0
```
which is arguably the appropriate behavior for this scenario (no values fall outside of the margin). Had we not anticipated this edge case, `within_margin_percentage([], [], margin=0.5)` would raise `ZeroDivisionError`.

It is also possible to write this solution using the built-in `sum` function and a [generator comprehension](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html#Creating-your-own-generator:-generator-comprehensions) that filters out those pairs of items that fall outside of the desired margin:

```python
def within_margin_percentage(desired, actual, margin):
    total = len(desired)
    count = sum(1 for i in range(total) if abs(actual[i] - desired[i]) <= margin)
    return  count / total if total > 0 else 1.0
```

It is debatable whether this refactored solution is superior to the original one - it depends largely on how comfortable you, and anyone else who will be reading your code, are with the generator comprehension syntax.
<!-- #endregion -->
