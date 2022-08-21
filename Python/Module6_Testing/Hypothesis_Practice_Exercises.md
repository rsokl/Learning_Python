---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.0
  kernelspec:
    display_name: Python [conda env:scicomp]
    language: python
    name: conda-env-scicomp-py
---

<!-- #raw raw_mimetype="text/restructuredtext" -->
.. meta::
   :description: Practice exercises using the Hypothesis testing library
<!-- #endraw -->

# Additional Practice Exercises Using Hypothesis

Hypothesis will not only improve the quality of our tests, but it should also save us time and cognitive load as it simplifies the process for describing the data that we want to pass to our code.
That being said, it can take some practice to learn one's way around [Hypothesis' core strategies](https://hypothesis.readthedocs.io/en/latest/data.html#core-strategies);
thus this section is dedicated to providing some useful exercises towards this end.


<div class="alert alert-info">

**Exercise: Describing data with `st.lists`**

Write a strategy that generates lists of even-valued integers, ranging from length-0 to length-10. 

Write a test that checks these properties and run the test.

</div>



<div class="alert alert-info">

**Exercise: Using Hypothesis to learn about floats.. Part 1**

Use the `st.floats` strategy to identify which float(s) violate the identity: `x == x`.
That is, write a hypothesis-driven test for which `assert x == x` *fails*, run the test, and identify the input that causes the failure. 

Then, revise your usage of `st.floats` such that it only describes values that satisfy the identity.
Run the test to ensure that your assumptions are correct. 
</div>


<!-- #region -->
<div class="alert alert-info">

**Exercise: Using Hypothesis to learn about floats.. Part 2**

Use the `st.floats` strategy to identify which **positive** float(s) violate the inequality: `x < x + 1`.

(To interpret your findings, it is useful to know that a double-precision (64-bit) binary floating-point number, which is representative of Python's `float`, has a coefficient of 53 bits (which actually only takes 52 bits to represent), an exponent of 11 bits, and 1 sign bit.) 


Then, revise your usage of `st.floats` such that it only describes values that satisfy the identity. **Use the `example` decorator to ensure that the identified boundary case is tested every time**.
</div>

<!-- #endregion -->

<div class="alert alert-info">

**Exercise: Stitching together strategies for rich behavior**

Write a strategy that draws a tuple of two perfect squares (integers) or three perfect cubes (integers)

Use view some examples to examine the behavior of your strategy.
</div>



<div class="alert alert-info">

**Exercise: Describing objects that evaluate to `False`**

Write a strategy that can return the boolean, integer, float, string, list, tuple, or dictionary that evaluates to `False` (when called on by `bool`)

</div>



## Solutions

<!-- #region -->
**Describing data with `st.lists`**
    
```python

# generates "any" integer and then multiplies that value
# by two, ensuring that it is an even number
even_integers = st.integers().map(lambda x: 2 * x)

# Recall that `st.lists(...)` can take any strategy. Thus
# we feed it our `even_integers` strategy 
@given(x=st.lists(even_integers, min_size=0, max_size=10))
def test_even_lists(x):
    assert isinstance(x, list) and 0 <= len(x) <= 10
    assert all(isinstance(i, int) for i in x)
    assert all(i % 2 == 0 for i in x)

```

```python
# running the test
>>> test_even_lists()
```
<!-- #endregion -->

<!-- #region -->
**Exercise: Using Hypothesis to learn about floats.. Part 1**

```python
# using `st.floats` to find value(s) that violate `x == x`

@given(x=st.floats())
def test_broken_identity(x):
    assert x == x
```

Running this test reveals..

```python
>>> test_broken_identity()
Falsifying example: test_broken_identity(
    x=nan,
)
```

that "NaN" (which stands for [Not a Number](https://en.wikipedia.org/wiki/NaN)) is not equal to itself.
This is, in fact, [the designed behavior of NaN](https://en.wikipedia.org/wiki/NaN#Comparison_with_NaN) in the specification for floating point numbers.

Now let's updated our strategy for describing floating point numbers to exclude this.

```python
@given(x=st.floats(allow_nan=False))
def test_fixed_identity(x):
    assert x == x
```

Assuming that NaN is the only floating point that violates the self-identity, this test should now pass.

```python
>>> test_fixed_identity()
```
<!-- #endregion -->

<!-- #region -->
**Exercise: Using Hypothesis to learn about floats.. Part 2**

```python
# using `st.floats` to find value(s) that violate `x < x + 1`

@given(x=st.floats(min_value=0))
def test_broken_inequality(x):
    assert x < x + 1
```
```python
>>> test_broken_inequality()
Falsifying example: test_broken_inequality(
    x=9007199254740992.0,
)
```
We can check that:

```python
>>> import math
>>> math.log2(9007199254740992)
53
```

Recall that `2 ** 53` is the maximum size that the coefficient of a floating point double can take on. Thus Hypothesis is pointing out that `2 ** 53 + 1` can't be represented as a 64-bit floating point number.
Let's see what happens when we do try to add one to `2 ** 53`:

```python
>>> x = 2.0 ** 53; x
9007199254740992.0

>>> x + 1
9007199254740992.0
```

The value doesn't change at all because we would have to exceed 64-bits allotted to represent a floating point number.
Thus `x < x + 1` fails to hold for `x = 2.0 ** 53`. 


Now let's update our test to test everything up to this maximum value.
Note that we want to ensure that we are testing the maximum permitted value every time we run the test as hypothesis does not guarantee that it will do so.
We leverage the `example` decorator to accomplish this.

```python
# updating our usage of `st.floats` to generate only values that satisfy `x < x + 1`
from hypothesis import example


@example(x=2.0 ** 53 - 1)  # ensures that maximum permissible value is tested
@given(x=st.floats(min_value=0, max_value=2.0 ** 53, exclude_max=True))
def test_fixed_inequality(x):
    assert x < x + 1
```

```python
# running our test
>>> test_fixed_inequality()
```
<!-- #endregion -->

<!-- #region -->
**Stitching together strategies for rich behavior**

```python
squares = st.integers().map(lambda x: x ** 2)
cubes = st.integers().map(lambda x: x ** 3)

# Recall that the pipe operator, `|`, is a convenient way for 
# calling `st.one_of(...)` on strategies
squares_or_cubes = st.tuples(squares, squares) | st.tuples(cubes, cubes, cubes)
```
<!-- #endregion -->

<!-- #region -->
**Describing objects that evaluate to `False`**

```python
falsies = st.sampled_from([False, 0, 0.0, "", [], tuple(), {}])
```
<!-- #endregion -->
