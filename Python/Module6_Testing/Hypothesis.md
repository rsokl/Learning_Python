---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.0
  kernelspec:
    display_name: Python [conda env:.conda-jupy] *
    language: python
    name: conda-env-.conda-jupy-py
---

<!-- #raw raw_mimetype="text/restructuredtext" -->
.. meta::
   :description: Topic: Writing tests for your code, Difficulty: Easy, Category: Section
   :keywords: test, automated, pytest, parametrize, fixture, suite, decorator, clean directory  
<!-- #endraw -->

<!-- #region -->
# Describing Data with Hypothesis

It is often the case that the process of *describing our data* is by far the heaviest burden that we must bear when writing tests. This process of assessing "what variety of values should I test?", "have I thought of all the important edge-cases?", and "how much is 'enough'?" will crop up with nearly every test that we write.
Indeed, these are questions that you may have been asking yourself when writing `test_count_vowels_basic` and `test_merge_max_mappings` in the previous sections of this module.

[Hypothesis](https://hypothesis.readthedocs.io/) is a powerful Python library that empowers us to write a _description_ (specification, to be more precise) of the data that we want to use to exercise our test.
It will then *generate* test cases that satisfy this description and will run our test on these cases.

Let's look at a simple example of Hypothesis in action.
In the preceding section, we learned to use pytest's parameterization mechanism to test properties of code over a set of values.
For example, we wrote the following trivial test:

```python
import pytest

# A simple parameterized test that only tests a few, conservative inputs.
# Note that this test must be run by pytest to work properly
@pytest.mark.parametrize("size", [0, 1, 2, 3])
def test_range_length(size):
    assert len(range(size)) == size
```

which tests the property that `range(n)` has a length of `n` for any non-negative integer value of `n`.
Well, it isn't *really* testing this property for all non-negative integers; clearly it is only testing the values 0-3.
We should probably also check much larger numbers and perhaps traverse various orders of magnitude (i.e. factors of ten) in our parameterization scheme.
No matter what set of values we land on, it seems like we will have to eventually throw our hands up and say "okay, that seems good enough."

Instead of manually specifying the data to pass to `test_range_length`, let's use Hypothesis to simply describe the data:
<!-- #endregion -->

<!-- #region -->
```python
from hypothesis import given

# Hypothesis provides so-called "strategies" for us
# to describe our data
import hypothesis.strategies as st

# Using hypothesis to test any integer value in [0, 10 ** 10]
@given(size=st.integers(min_value=0, max_value=1E10))
def test_range_length(size):
    assert len(range(size)) == size
```
<!-- #endregion -->

<!-- #region -->
Here we have specified that the `size` value in our test should take on any integer value within $[0, 10^{10}]$.
We did this by using the `integers` "strategy" that is provided by Hypothesis: `st.integers(min_value=0, max_value=1E10)`.
When we execute the resulting test (which can simply be run within a Jupyter cell or via pytest), this will trigger Hypothesis to generate test cases based on this specification;
by default it will generate 100 test cases - an amount that we can configure - and will evaluate our test for each one of them.

```python
# Running this test once will trigger Hypothesis to
# generate 100 values based on the description of our data,
# and it will execute the test using each one of those values
>>> test_range_length()
```

With great ease, we were able to replace our pytest-parameterized test, which only very sparsely tested the property at hand, with a much more robust, hypothesis-driven test.
This will be a recurring trend: we will generally produce much more robust tests by _describing_ our data with Hypothesis, rather than manually specifying test values.

The rest of this section will be dedicated to learning about the Hypothesis library and how we can leverage it to write powerful tests.
<!-- #endregion -->

<!-- #region -->
<div class="alert alert-warning">

**Hypothesis is _very_ effective...**: 

You may be wondering why, in the preceding example, I arbitrarily picked $10^{10}$ as the upper bound to the integer-values to feed to the test.
I actually didn't write the test that way initially.
Instead, I wrote the more general test:

```python
@given(size=st.integers(min_value=0))
def test_range_length(size):
    assert len(range(size)) == size
```

which places no formal upper bound on the integers that Hypothesis will generate.
However, this test immediately found an issue (I hesitate to call it an outright bug):

```python
Falsifying example: test_range_length(
    size=9223372036854775808,
)

----> 3     assert len(range(size)) == size

OverflowError: Python int too large to convert to C ssize_t
```

This reveals that the implementation of the built-in `len` function is such that it can only handle non-negative integers smaller than $2^{63}$ (i.e. it will only allocate 64 bits to represent a signed integer - one bit is used to store the sign of the number).
Hypothesis revealed this by generating the failing test case `size=9223372036854775808`, which is exactly $2^{63}$.
I did not want this error to distract from what is otherwise merely a simple example, but it is very important to point out.

Hypothesis has a knack for catching these sorts of unexpected edge cases.
Now we know that `len(range(size)) == size` _does not_ hold for "arbitrary" non-negative integers!
(I wonder how many of the Python core developers know about this 😄).


</div>
<!-- #endregion -->

## Links to Official Documentation

- [Hypothesis](https://hypothesis.readthedocs.io/)


## Reading Comprehension Solutions
